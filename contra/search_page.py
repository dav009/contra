# -*- coding: utf-8 -*-
import re
import multiprocessing
from multiprocessing import Pool
import codecs
from os import listdir
import itertools

def extract_links_from_index_page(content):
	pattern = re.compile(r'/consultas/detalleProceso\.do\?numConstancia=[0-9-]+')
	urls = pattern.findall(content)
	return list(set(urls))

def extract_links_from_file(path_to_file):
	print("reading.." + path_to_file)
	f = codecs.open(path_to_file, 'r', 'utf-8')
	content = f.read()
	f.close()
	return extract_links_from_index_page(content)



def extract_all_links(path_to_page_folder):
	all_files_in_folder = [ path_to_page_folder + f for f in listdir(path_to_page_folder)]
	pool = multiprocessing.Pool(50)
	results = pool.map(extract_links_from_file, all_files_in_folder)
	print("concatenating results....")
	results = set(list(itertools.chain(*results)))
	return results

def main(args):
	path_to_folder_with_pages = args[0]
	path_to_output_file = args[1]
	all_links = extract_all_links(path_to_folder_with_pages)

	output = codecs.open(path_to_output_file, 'w', 'utf-8')
	for link in all_links:
		output.write(link+"\n")
	output.close()

# Extracts all the contract urls from a folder filled with contract pages
# <PathToDownloadedSearchPages> <OutputFile>
#main(["/Users/dav009/source/contra/pages/", "/Users/dav009/source/contra/all_links"])
