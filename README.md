![](https://github.com/dav009/contra/blob/master/logo.gif?raw=true)

Contra es un conjunto de scripts para:  (i) descargar y (ii) extraer informacion de `contratos.gov.co` (Sitio web del gobierno colombiano con informacion contractual)
 
Tener la informacion contractual en un formato procesable es un requirimiento indispensable para usar los datos en la solucion de problemas (i.e: Deteccion de Corrupcion).
 
1. Descarga los contratos de contratos.gov.co (approx 1 millon para Julio 2015)
2. Extrae del html la informacion sobre los contratos y genera un archivo donde cada entrada es un objeto json
 
Descargar dataset : <Enlace>
 
# Dataset
 
## Estructura
 
```json
{
  "bla": "bla"
}
```
 
# Detalles
 
 1. Los enlaces a los contratos son deconocidos. Primero se descargan los enlaces a los contratos via el API de busqueda
 2. Se descargan las paginas de los contratos
 3. Se paresen las paginas de los contratos, generando el dataset
 4. Limpieza
 5. yay ^^