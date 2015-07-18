import requests
from multiprocessing import Pool, Value
import codecs
from contract import ContractParser
import json

counter = Value('i', 1)

def worker(pair):
	url = pair[0]
	global counter
	output_folder = pair[1]
	try:
		result = requests.get(url)
		if result.status_code == 200:
			temporalFolder = counter.value % 400
			print("temporal:" + temporalFolder)
			folder = output_folder+"/"+str(temporalFolder)+"/"
			f = codecs.open(folder + (url.replace("/", "_")), 'w', 'utf-8')
			contract = ContractParser(result.text).parse()
			f.write(json.dumps(contract)+"\n")
			f.close()
			#print("downloaded.." + url)
		else:
			print("error downloading.." + url)
	except Exception as e:
		print(e.message)
		print("error downloading.." + url)
	counter.value += 1
	print("done.." + str(counter.value))


# Downloads a list of links to contract pages
# main <pathToFileWithContractLinkPerLine> <FolderWhereContractLinksWillBeDownloaded>
def main(args):
	file_with_urls = args[0]
	output_folder = args[1]

	for i in range(0,400):
		folder = output_folder+"/"+str(i)+"/"
		if not os.path.exists(folder):
			os.makedirs(folder)

	f = codecs.open(file_with_urls, 'r', 'utf-8')
	urls = (("https://www.contratos.gov.co" + line.strip(),output_folder) for line in f)
		

	pool = Pool(600)
	pool.map(worker , urls)


#main(["data/all_links", "data/contracts/"])