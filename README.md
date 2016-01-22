![](https://github.com/dav009/contra/blob/master/logo.gif?raw=true)

Contra es un conjunto de scripts para:  (i) descargar y (ii) extraer informacion de `contratos.gov.co` (Sitio web del gobierno colombiano con informacion contractual)
 
Tener la informacion contractual en un formato procesable es un requirimiento indispensable para usar los datos en la solucion de problemas (i.e: Deteccion de Corrupcion).


Este script permite:
 
1. Descargar los contratos de contratos.gov.co (approx 1 millon para Julio 2015)
2. Extraer del html la informacion sobre los contratos y generar un dataset en formato json

# Dataset

## Dump Enero 21 2016

El dataset de Contratos hasta enero 2016 pesa aproximadamente 7G, contiene cerca de 2 millon de entradas esta disponible para descargar aqui:

- [Enero_21_2016 Dataset](http://s3.amazonaws.com/rm-open-data/contract-data-january-21-2016-cleaned.tar.gz) gracias a [@jpmarindiaz](https://twitter.com/jpmarindiaz) por hostearlo

## Dump Julio 18 2015 

El dataset de Contratos hasta Julio 2015 pesa aproximadamente 5G, contiene cerca de 1 millon de entradas.

- [Julio_18_2015 Dataset Torrent](https://github.com/dav009/contra/blob/master/datos_json_contratos_gov_co.torrent?raw=true)

- [Julio_18_2015 Dataset via datahub](http://datahub.io/dataset/dataset-datos-contratacion-estatal-colombia)

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
2. `pip install -r requirements.txt`
 
# Running it

### Descargando las paginas de busqueda

Descarga la paginas de busqueda en el directorio especificado en output:

`python contra  scrape_searchpages --output <pathToOutputFolder>`

--------------


### Extrayendo URLs de contratos de las paginas de busqueda

Extrae las urls de contratos dentro de las paginas de busqueda. Genera una archivo con cada URL de un contrato.

`python contra  extract_contracts --input <PathToFolderWithSearchPages> --output <OutputFileWithAllContractURLS>`

--------------

### Descargando las paginas de contratos

Dada un archivo que contiene en cada linea una url a un contrato. Descarga cada contrato, extrae el contenido, y genera un archivo json en el folder especificado en output.

`python contra  scrape_contracts --input <fileWithContractLinks> --output <folderWithContractJsonPages>`

--------------

Los archivos generados pueden ser concatenados via `cat http* >> dataset.json` para generar el dataset final



### Schema dataset

```
 |-- Actividades o servicios prestados por el inversionista: string (nullable = true)
 |-- Adición al contrato: string (nullable = true)
 |-- Adjudicación: string (nullable = true)
 |-- Beneficios e impactos: string (nullable = true)
 |-- Calificación definitiva de los proponentes - Orden de elegibilidad: string (nullable = true)
 |-- Causal de Otras Formas de Contratación Directa: string (nullable = true)
 |-- Celebración de Contrato: string (nullable = true)
 |-- Clase: string (nullable = true)
 |-- Convocatoria: string (nullable = true)
 |-- Correo Electrónico: string (nullable = true)
 |-- Correo Electrónico para el Envío de Expresiones: string (nullable = true)
 |-- Creación de Proceso: string (nullable = true)
 |-- Cuantía Definitiva del Contrato: string (nullable = true)
 |-- Cuantía a Contratar: string (nullable = true)
 |-- Departamento y Municipio de Ejecución: string (nullable = true)
 |-- Departamento y Municipio de Entrega Documentos: string (nullable = true)
 |-- Departamento y Municipio de Obtención de Documentos: string (nullable = true)
 |-- Descripción del objeto del proyecto: string (nullable = true)
 |-- Destinación del Gasto: string (nullable = true)
 |-- Detalle y Cantidad del Objeto: string (nullable = true)
 |-- Detalle y Cantidad del Objeto a Contratar: string (nullable = true)
 |-- Dirección Fisica de Entrega de Expresiones: string (nullable = true)
 |-- Dirección Física de Entrega de Documentos del Proceso: string (nullable = true)
 |-- Dirección Física de Obtención de Documentos del Proceso: string (nullable = true)
 |-- Dirección Física del Contratista: string (nullable = true)
 |-- Estado del Contrato: string (nullable = true)
 |-- Estado del Proceso: string (nullable = true)
 |-- Familia: string (nullable = true)
 |-- Fecha Inicio de entrega de Expresiones: string (nullable = true)
 |-- Fecha Limite de entrega de Expresiones: string (nullable = true)
 |-- Fecha Límite de Entrega de Documentos Habilitantes: string (nullable = true)
 |-- Fecha Terminación Anormal Después de Convocado: string (nullable = true)
 |-- Fecha de Conformación Dinámica: string (nullable = true)
 |-- Fecha de Firma del Contrato: string (nullable = true)
 |-- Fecha de Inicio de Ejecución del Contrato: string (nullable = true)
 |-- Fecha de Inicio de la subasta: string (nullable = true)
 |-- Fecha de Liquidación del Contrato: string (nullable = true)
 |-- Fecha de Publicación de la Lista Corta: string (nullable = true)
 |-- Fecha de Terminación del Contrato: string (nullable = true)
 |-- Fecha en que se Descartó el Proceso: string (nullable = true)
 |-- Fecha y Hora de Apertura del Proceso: string (nullable = true)
 |-- Fecha y Hora de Audiencia Aclaración: string (nullable = true)
 |-- Fecha y Hora de Audiencia Aclaración de Pliegos: string (nullable = true)
 |-- Fecha y Hora de Audiencia Adjudicación: string (nullable = true)
 |-- Fecha y Hora de Audiencia de Sorteo de Proponentes: string (nullable = true)
 |-- Fecha y Hora de Cierre del Proceso: string (nullable = true)
 |-- Fecha y Hora de Publicación del Proyecto: string (nullable = true)
 |-- Fecha y Hora de Visita de Sitio: string (nullable = true)
 |-- Fecha y Hora de Visita del Lugar Obra: string (nullable = true)
 |-- Grupo: string (nullable = true)
 |-- Identificación del Contratista: string (nullable = true)
 |-- Identificación del Representante Legal: string (nullable = true)
 |-- Liquidación de Contrato: string (nullable = true)
 |-- Lista Corta: string (nullable = true)
 |-- Lista Multiusos: string (nullable = true)
 |-- Lugar Físico o Virtual de la Subasta: string (nullable = true)
 |-- Lugar de Audiencia de Aclaración: string (nullable = true)
 |-- Lugar de Audiencia de Aclaración de Pliegos: string (nullable = true)
 |-- Lugar de Audiencia de Adjudicación: string (nullable = true)
 |-- Lugar de Audiencia de Sorteo de Proponentes: string (nullable = true)
 |-- Modalidad de la Subasta: string (nullable = true)
 |-- Motivo de Terminación Anormal Después de Celebrado: string (nullable = true)
 |-- Motivo de Terminación Anormal Después de Convocado: string (nullable = true)
 |-- Nombre de la APP: string (nullable = true)
 |-- Nombre del Representante Legal del Contratista: string (nullable = true)
 |-- Nombre o Razón Social del Contratista: string (nullable = true)
 |-- Nombre ó Razón Social del proponente seleccionado: string (nullable = true)
 |-- Numero compromiso presupuestal: string (nullable = true)
 |-- Objeto del Contrato: string (nullable = true)
 |-- Origen de los recursos: string (nullable = true)
 |-- País y Departamento/Provincia de ubicación del Contratista: string (nullable = true)
 |-- Plazo de Ejecución del Contrato: string (nullable = true)
 |-- Población beneficiada: string (nullable = true)
 |-- Porcentaje de Anticipo: string (nullable = true)
 |-- Proceso Liquidado: string (nullable = true)
 |-- Proceso descartado: string (nullable = true)
 |-- Régimen de Contratación: string (nullable = true)
 |-- Segmento: string (nullable = true)
 |-- Terminación Anormal despues de Convocado: string (nullable = true)
 |-- Terminación sin liquidar de Contrato: string (nullable = true)
 |-- Tipo de Contrato: string (nullable = true)
 |-- Tipo de Proceso: string (nullable = true)
 |-- Tipo de Terminación del Contrato: string (nullable = true)
 |-- Tipo de proyecto: string (nullable = true)
 |-- Ubicación de la Sala de Consulta: string (nullable = true)
 |-- Ubicación del Proyecto: string (nullable = true)
 |-- Unidad/Subunidad ejecutora (SIIF): string (nullable = true)
 |-- Valor Contrato Interventoría Externa: string (nullable = true)
 |-- Valor del Contrato: string (nullable = true)
 |-- Valor estimado del contrato: string (nullable = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- description: string (nullable = true)
 |    |    |-- name: string (nullable = true)
 |    |    |-- publication_date: string (nullable = true)
 |    |    |-- url: string (nullable = true)
```
