![](https://github.com/dav009/contra/blob/master/logo.gif?raw=true)

Contra es un conjunto de scripts para:  (i) descargar y (ii) extraer informacion de `contratos.gov.co` (Sitio web del gobierno colombiano con informacion contractual)
 
Tener la informacion contractual en un formato procesable es un requirimiento indispensable para usar los datos en la solucion de problemas (i.e: Deteccion de Corrupcion).
 
1. Descarga los contratos de contratos.gov.co (approx 1 millon para Julio 2015)
2. Extrae del html la informacion sobre los contratos y genera un dataset en formato json

# Dataset

El dataset de Contratos(Julio 2015) esta disponible para descargar aqui: <Enlace>

Cada linea del archivo contiene un objecto json. Cada objeto json tiene la siguiente estructura:

```json
{
    "Creación de Proceso": "24 de June      de 2015  10:50 A.M.",
    "Objeto del Contrato": "Prestacion de servicios profesionales como como medico general, en las condiciones, areas y servicios requeridos",
    "Estado del Contrato": "Celebrado",
    "Correo Electrónico": "contratacion@esesanantoniodepadua.gov.co",
    "Fecha de Inicio de Ejecución del Contrato": "02 de mayo de 2015",
    "Grupo": "[F] Servicios",
    "Tipo de Contrato": "Prestación de Servicios",
    "Identificación del Representante Legal": "Cédula de Ciudadanía No. 1.110.479.226 Ibagué",
    "Departamento y Municipio de Ejecución": "Huila : La Plata",
    "Cuantía Definitiva del Contrato": "$12,000,000     Peso Colombiano",
    "documents": [
        {
            "publication_date": "24-06-2015 11:03 AM",
            "url": "/cloud/cloud2/2015/DA/241396015/15-4-3967699/DA_PROCESO_15-4-3967699_241396015_15194469.pdf",
            "name": "Documento Adicional",
            "description": "ACTA INICIO"
        },
        {
            "publication_date": "24-06-2015 11:02 AM",
            "url": "/cloud/cloud2/2015/C/241396015/15-4-3967699/C_PROCESO_15-4-3967699_241396015_15194424.pdf",
            "name": "Contrato",
            "description": ""
        }
    ],
    "Identificación del Contratista": "Cédula de Ciudadanía No. 1.110.479.226 Ibagué",
    "Nombre o Razón Social del Contratista": "GERMAN EDUARDO SILVA BONILLA",
    "País y Departamento/Provincia de ubicación del Contratista": "Colombia : Huila",
    "Nombre del Representante Legal del Contratista": "GERMAN EDUARDO SILVA BONILLA",
    "Segmento": "[85] Servicios de Salud",
    "Plazo de Ejecución del Contrato": "2 Meses",
    "Celebración de Contrato": "24 de June      de 2015  11:04 A.M.",
    "Estado del Proceso": "Celebrado",
    "Clase": "[851016] Personas de soporte de prestación de servicios de salud",
    "Cuantía a Contratar": "$12,000,000",
    "Régimen de Contratación": "ESE HOSPITAL",
    "Destinación del Gasto": "No Aplica",
    "Tipo de Proceso": "Régimen Especial",
    "Detalle y Cantidad del Objeto a Contratar": "Prestacion de servicios profesionales como como medico general, en las condiciones, areas y servicios requeridos",
    "Fecha de Firma del Contrato": "30 de abril de 2015",
    "Familia": "[8510] Servicios integrales de salud",
    "Dirección Física del Contratista": "Avenida Libertadores La Plata"
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

