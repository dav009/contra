
import json
import os
from contra.contract import ContractParser

fixture_file = os.path.dirname(os.path.abspath(__file__))+ "/fixture.json"
fixture = json.load(open(fixture_file,'r'))['fixture_1']

class TestParser:

	def test_parser(self, monkeypatch):
		contract_representation = ContractParser(fixture).parse()
		assert(contract_representation['Segmento']=="[44] Equipos de Oficina, Accesorios y Suministros")
		assert(contract_representation['Cuantía a Contratar']=="$83,668,709")
		assert(contract_representation['Creación de Proceso']=="03 de November  de 2011  06:50 P.M.")
		assert(len(contract_representation['documents'])==22)