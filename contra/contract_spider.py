import requests
from multiprocessing import Pool, Value
import codecs

counter = Value('i', 0)

def worker(pair):
	url = pair[0]
	output_folder = pair[1]
	try:
		result = requests.get(url)
		if result.status_code == 200:
			f = codecs.open(output_folder+"/"+(url.replace("/", "_")), 'w', 'utf-8')
			f.write(result.text.replace("\n", " ").replace("\r", " "))
			f.close()
			#print("downloaded.." + url)
		else:
			print("error downloading.." + url)
	except Exception as e:
		print(e.message)
		print("error downloading.." + url)
	global counter
	counter.value += 1
	print("done.." + str(counter.value))


# Downloads a list of links to contract pages
# main <pathToFileWithContractLinkPerLine> <FolderWhereContractLinksWillBeDownloaded>
def main(args):
	file_with_urls = args[0]
	output_folder = args[1]

	f = codecs.open(file_with_urls, 'r', 'utf-8')
	urls = (("https://www.contratos.gov.co" + line.strip(),output_folder) for line in f)
		

	pool = Pool(600)
	pool.map(worker , urls)


#main(["data/all_links", "data/contracts/"])