import requests
import codecs
import multiprocessing
from multiprocessing import Pool

class Contratos:


	def __init__(self, output_folder):
		self.url = "https://www.contratos.gov.co/consultas/resultadosConsulta.do?&ctl00$ContentPlaceHolder1$hidIDProducto=-1&ctl00$ContentPlaceHolder1$hidRedir=&departamento=&ctl00$ContentPlaceHolder1$hidNombreDemandante=-1&objeto={objeto}&paginaObjetivo={pagina}&cuantia={cuantia}&ctl00$ContentPlaceHolder1$hidNombreProducto=-1&fechaInicial=&ctl00$ContentPlaceHolder1$hidIdEmpresaC=0&ctl00$ContentPlaceHolder1$hidIdOrgV=-1&ctl00$ContentPlaceHolder1$hidIDProductoNoIngresado=-1&ctl00$ContentPlaceHolder1$hidRangoMaximoFecha=&fechaFinal=&desdeFomulario=true&ctl00$ContentPlaceHolder1$hidIdOrgC=-1&ctl00$ContentPlaceHolder1$hidIDRubro=-1&tipoProceso=&registrosXPagina=10&numeroProceso=&municipio=0&estado=0&ctl00$ContentPlaceHolder1$hidNombreProveedor=-1&ctl00$ContentPlaceHolder1$hidIdEmpresaVenta=-1"
		self.output_folder = output_folder

	def generate_base_urls(self):
		cuantias = ["1", "2", "3", "4", "5"]
		objetos = ["10000000", "11000000", "12000000", "15000000", "13000000", "14000000", "27000000", "20000000", "21000000", 
		           "22000000", "26000000", "23000000", "24000000", "25000000", "40000000", "32000000", "31000000", "30000000"
		           "39000000", "41000000", "50000000", "52000000", "43000000", "42000000", "44000000", "46000000", "45000000"
		           "47000000", "49000000", "60000000", "48000000", "51000000", "56000000", "54000000", "55000000", "53000000",
		           "94000000", "81000000", "82000000", "86000000", "84000000", "77000000", "91000000", "93000000", "83000000",
		           "70000000", "92000000", "72000000", "80000000", "76000000", "71000000", "73000000", "85000000", "78000000",
		           "90000000", "95000000"]

		extractors = list()

		for cuantia in cuantias:
			for objeto in objetos:
				extractors.append(UrlExtractor(self.url, 1, objeto, cuantia, self.output_folder))

		return extractors

class UrlExtractor:

	def __init__(self, base_url, pagina, objeto, cuantia, output_folder):
		self.url = base_url
		self.current_pagina = pagina
		self.objeto = objeto
		self.cuantia = cuantia
		self.output_folder = output_folder

	def get_url(self):
		return self.url.format(pagina=str(self.current_pagina), cuantia=self.cuantia, objeto=self.objeto)

	def extract(self):
		try:
			response = requests.get(self.get_url())
			if (response.status_code == 200):
				if not "No existen resultados que cumplan con los" in response.text:
					return response.text
			return ""
		except Exception:
			print("error while grabbing.." + self.get_url())
			return ""

	def extract_all(self):
		html_content = ""
		while True:
			html_content = self.extract()
			if html_content=="":
				break
			filename = self.output_folder+"/{objeto}_{cuantia}_{pagina}".format(objeto=self.objeto, cuantia=self.cuantia, pagina=self.current_pagina)
			print("saving.." + filename)
			f = codecs.open(filename, 'w', 'utf-8')
			f.write(html_content)
			f.close()
			self.current_pagina = self.current_pagina + 1

def worker(extractor):
	extractor.extract_all()
	
def main(args):

	output_folder = args[0]
	extractors = Contratos(output_folder).generate_base_urls()

	pool = multiprocessing.Pool(30)
	pool.map(worker ,extractors)


# uso [PathToOutputFolder]
main(["/Users/dav009/source/contra/pages"])