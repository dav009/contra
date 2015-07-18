import argparse
import contract
import contract_spider
import search_page
import search_page_spider

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("action", help="scrape_searchpages | extract_contracts | scrape_contracts | create-dataset")
	parser.add_argument("--input")
	parser.add_argument("--output")
	args = parser.parse_args()

	action = args.action
	input_arg = args.input
	output_arg = args.output 


	if action=="scrape_searchpages":
		print("downloading search pages to: %s"%(output_arg))
		search_page_spider.main([output_arg])
		
	elif action=="extract_contracts":
		print("Reading pages from: %s"%(input_arg))
		print("Saving extracted urls to: %s"%(output_arg))
		search_page.main([input_arg, output_arg])
		
	elif action=="scrape_contracts":
		print("Reading link list from: %s"%(input_arg))
		print("Download contract html-content: %s"%(output_arg))
		contract_spider.main([input_arg, output_arg])

	elif action=="create-dataset":
		print("Parsing pages in: %s"%(input_arg))
		print("Saving json dataset in: %s"%(output_arg))
		contract.create_data_set_from_files(input_arg, output_arg)
	elif action=="create-single-lined-files":
		print("Parsing pages in: %s"%(input_arg))
		contract.remove_new_lines(input_arg)



# contra  scrape_searchpages --output folder
# contra  extract_contracts --input scrapedSearchPages --output fileWithLinks
# contra  scrape_contracts --input fileWithContractLinks --output folderWithContractPages
#
if __name__ == "__main__":
	main()