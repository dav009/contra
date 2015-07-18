from lxml.cssselect import CSSSelector
from lxml import html
from lxml.html.clean import clean_html
import multiprocessing
from multiprocessing import Pool, Value
from os import listdir
import json
import codecs

counter = Value('i', 0)

# Extracts fields from contract pages: 
# i.e: https://www.contratos.gov.co/consultas/detalleProceso.do?numConstancia=15-11-4035910
class ContractParser:

	def __init__(self, html_content):
		self.parsed_content = html.fromstring(html_content)

	def extract_field(self, list_of_tds):
		field_name = ""
		field_value = ""
		for td_tag in list_of_tds:
			if(td_tag.get("class")=="tablaslistOdd"):
				if field_value!="":
					field_name = field_value
				field_value = td_tag.text_content().strip()
				
			if(td_tag.get("class")=="tablaslistEven"):
				field_name = td_tag.text_content().strip()

		return field_name, field_value

	def extract_doc(self, list_of_tds):

		def extract_url(td_tag):
			matches = CSSSelector("input[type=\"hidden\"]")(td_tag)
			url = ""
			for match in matches:
				url = match.get("value").strip()
			return url

		def extract_name(td_tag):
			matches = CSSSelector("input[type=\"submit\"]")(td_tag)
			name = ""
			for match in matches:
				name = match.get("value").strip()
			return name

		name = extract_name(list_of_tds[0])
		url =  extract_url(list_of_tds[0])
		description = list_of_tds[1].text_content().strip()
		publication_date = list_of_tds[5].text_content().strip()

		# Making sure we dont extract the header of the table
		if(name!="" and name!="Nombre"):
			return {"name": name, "url" : url, "description": description, "publication_date": publication_date}
		return None



	def parse(self):
		contract_representation = dict()
		contract_representation['documents'] = list()

		tr_tags = CSSSelector("tr")(self.parsed_content)
		for tr_tag in tr_tags:

			td_tags = CSSSelector("td")(tr_tag)

			# it is a field : field value
			if(len(td_tags) == 2):
				field_name, field_value = self.extract_field(td_tags)
				if field_name and field_value:
					contract_representation[field_name] = field_value		

			# it is one of the linked docs
			if(len(td_tags) == 6):
				document = self.extract_doc(td_tags)
				if document:
					contract_representation['documents'].append(document)
		return contract_representation

def parse_contract_page(page_file):
	f = codecs.open(page_file, 'r', 'utf-8')
	content = "\n".join(f.readlines())
	contract = ContractParser(content).parse()
	f.close()
	global counter
	counter.value += 1
	print("done.." + str(counter.value))
	return contract

def convert_to_single_line(page_file):
	f = codecs.open(page_file, 'r', 'utf-8')
	content = " ".join(f.readlines())
	f.close()

	output = codecs.open(page_file, 'w', 'utf-8')
	output.write(content+"\n")
	output.close()

	global counter
	counter.value += 1
	print("done.." + str(counter.value) )

def remove_new_lines(path_to_folder):
	all_files_in_folder = [ path_to_folder + "/" + f for f in listdir(path_to_folder)]
	pool = multiprocessing.Pool(100)
	pool.map(convert_to_single_line, all_files_in_folder)

def create_data_set_from_files(path_to_folder, output):
	all_files_in_folder = [ path_to_folder + "/" + f for f in listdir(path_to_folder)]
	pool = multiprocessing.Pool(100)
	print("parsing page files....")
	results = pool.map(parse_contract_page, all_files_in_folder)
	print("exporting json to output file....")
	output = codecs.open(output, 'w', 'utf-8')
	for result in results:
		output.write(json.dumps(result)+"\n")
	output.close()




