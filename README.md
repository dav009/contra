![](https://github.com/dav009/contra/blob/master/logo.gif?raw=true)

Contra es un conjunto de scripts para:  (i) descargar y (ii) extraer informacion de `contratos.gov.co` (Sitio web del gobierno colombiano con informacion contractual)
 
Tener la informacion contractual en un formato procesable es un requirimiento indispensable para usar los datos en la solucion de problemas (i.e: Deteccion de Corrupcion).
 
1. Descarga los contratos de contratos.gov.co (approx 1 millon para Julio 2015)
2. Extrae del html la informacion sobre los contratos y genera un dataset en formato json
 
Descargar dataset : <Enlace>
 
# Dataset
 
## Estructura
 
```json
{
  "bla": "bla"
}
```

# Instalando requerimientos

1. `sudo apt-get install libxml2-dev libxslt-dev python-dev zlib1g-dev`
2. `pip install -r requierements.txt`
 
# Running it

### Descargando las paginas de busqueda

Descarga la paginas de busqueda en el directorio especificado en output:

`contra  scrape_searchpages --output <pathToOutputFolder>`

--------------


### Extrayendo URLs de contratos de las paginas de busqueda

Extrae las urls de contratos dentro de las paginas de busqueda. Genera una archivo con cada URL de un contrato.

`contra  extract_contracts --input <PathToFolderWithSearchPages> --output <OutputFileWithAllContractURLS>`

--------------

### Descargando las paginas de contratos

Dada un archivo que contiene en cada linea una url a un contrato. Descarga cada contrato en el folder especificado en output.

`contra  scrape_contracts --input <fileWithContractLinks> --output <folderWithContractPages>`

--------------

### Parseando Paginas de contratos (exportar a json)

Convierte cada pagina del folder de entrada (un contrato) a json y lo exporta a un archivo

`contra  create-dataset --input <folderWithContractPages> --output <jsonFileWithContractData>`

