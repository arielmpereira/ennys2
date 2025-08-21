# Grupo I - Propuesta de Trabajo de Investigación
## Análisis de la Base de Datos de la Encuesta Nacional de Nutrición y Salud 2018
A partir de la base de datos obtenida mediante la encuesta, se busca estimar la prevalencia de consumo de alimentos ultraprocesados y la presencia de sobrepeso en niños y adolescentes. Se incluirán los niños mayores de 6 meses, edad que marca el inicio de la alimentación complementaria.

Como objetivo complementario, se plantea analizar el consumo de ultraprocesados en la población adulta y establecer su relación con las mediciones bioquímicas disponibles.

En ambos análisis, se incorporarán variables socioeconómicas, con el fin de realizar comparaciones entre grupos con distintos niveles de acceso al cuidado de la salud.

### Base de datos

Se usará la base de datos publicada por el Ministerio de Salud de la Nación disponible en el sitio: [Base de datos de la 2° Encuesta Nacional de Nutrición y Salud (ENNyS2) 2018-2019](https://datos.gob.ar/dataset/salud-base-datos-2deg-encuesta-nacional-nutricion-salud-ennys2-2018-2019)

Este conjunto cuenta con 21357 registros relevados en las localidades argentinas con más de 5000 habitantes de acuerdo al censo realizado en el año 2010.

#### Composición de la muestra

|Población|Rango etáreo|Registros|Interés para este trabajo|
|---------|------------|---------|-------------------------|
|Bebés|0 a 6 meses|1348|No, lactantes exclusivemente o mínima alimentación complementaria|
|Bebés|6 a 24 meses|4415|Si, comienza la alimentación complementaria|
|Niños|2 a 12 años|5829|Si|
|Adolescentes|13 a 17 años|2399|Si|
|Adultos|18 o más|7367| Complementario, se quiere analizar la relación de consumo de ultraprocesados y niveles de colesterol y azúcar en sangre.

#### Variables
##### Bebés
|Variable|Tipo|Descripción|
|--------------|--------|--------|
|T_C1_HA_7_1_12|Numérico|Morcilla|
|T_C1_HA_7_1_16|Numérico|Fideos, sémola, avena y otros cereales con gluten|
|T_C1_HA_7_1_17|Numérico|Arroz, harina de maíz, tapioca y otros cereales sin gluten|
|T_C1_HA_7_1_18|Numérico|Papillas listas para comer|
|T_C1_HA_7_1_19|Numérico|Pan o galletitas saladas|
|T_C1_HA_7_1_20|Numérico|Galletitas dulces|
|T_C1_HA_7_1_25|Numérico|Helado|
|T_C1_HA_7_1_26|Numérico|Postres lácteos envasados|
|T_C1_HA_7_1_27|Numérico|Miel|
|T_C1_HA_7_1_28|Numérico|Golosinas|
|T_C1_HA_7_1_30|Numérico|Gaseosa (común o light)|
|T_C1_HA_7_1_34|Numérico|Jugo de frutas industrial|
|T_C1_HA_7_1_35|Numérico|Jugo de frutas para diluir, polvo o líquido (común o light)|
|T_C1_HA_7_1_37|Numérico|Sal|

##### Niños
|Variable|Tipo|Descripción|
|--------------|--------|--------|
|T_C2_EE_7_2_1|Numérico|Bebidas con azúcar (jugos en polvo y/o concentrados, gaseosas, aguas saborizadas|
|T_C2_EE_7_2_2|Numérico|Bebidas sin azúcar (jugos en polvo y/o concentrados, gaseosas, aguas saborizadas|
|T_C2_EE_7_2_4|Numérico|Productos de copetín (papas fritas, palitos de maíz, etc.)|
|T_C2_EE_7_2_5|Numérico|Golosinas (caramelos, alfajores, chupetines, chicles, barras de cereal, etc.)|
|T_C2_EE_7_2_6|Numérico|Facturas, productos de pastelería, galletitas dulces, cereales con azúcar|
|T_C2_EE_7_2_9|Numérico|Yogur/postres lácteos /leche|
|T_C2_EE_7_2_10|Numérico|Sándwich|

##### Adolescentes
|Variable|Tipo|Descripción|
|--------------|--------|--------|
|T_C3_FCA_6_1_4|Numérico|…papa, batata, cereales refinados como arroz blanco, pastas, tartas, empanadas y|
|T_C3_FCA_6_1_5|Numérico|…cereales integrales, legumbres (por ejemplo lentejas, garbanzos, |porotos, arroz|
|T_C3_FCA_6_1_6|Numérico|… embutidos y/o fiambres (jamón, salame, chorizo, salchicha, etc)?|
|T_C3_FCA_6_1_9|Numérico|… aceites vegetales (como girasol, maíz, soja, girasol alto oleico, oliva y/o ca|
|T_C3_FCA_6_1_11|Numérico|"… productos de copetín (papas fritas, palitos de maíz, etc.)?|
|T_C3_FCA_6_1_12|Numérico|"… golosinas (caramelos, alfajores, chupetines, chicles, barras de cereal, etc.)?|
|T_C3_FCA_6_1_13|Numérico|"…facturas y/o productos de pastelería, galletitas dulces, cereales con azúcar|
|T_C3_FCA_6_1_14|Numérico|"…productos congelados pre elaborados (nuggets de pollo, supremas, medallones, ba|
|T_C3_FCA_6_1_15|Numérico|"… bebidas artificiales sin azúcar (jugos en polvos y/o concentrados, gaseosas, a|
|T_C3_FCA_6_1_16|Numérico|"… bebidas artificiales con azúcar (jugos en polvos y/o concentrados, gaseosas, a|

### Documentos Anteriores

Publicaciones de organismos como la Organización Paranamericana de la Salud y la Asociación Argentina de Pediatría dan cuenta de la relevancia del tema de estudio.

Fuera de Latinoamérica, el informe MAHA, del gobierno de los Estados Unidos, también describe la crisis sanitaria causada por enfermedades crónicas en el 40% de niños y adolescentes.

1. Organización Panamericana de la Salud (2019). [Las ENT de un vistazo: Mortalidad de las enfermedades no transmisibles y prevalencia de sus factores de riesgo en la Región de las Américas](https://iris.paho.org/handle/10665.2/51752)
1. Asociación Argentina de Pediatría (2024). [Consumo de alimentos ultraprocesados en niños entre
6 y 23 meses según la Segunda Encuesta Nacional de
Nutrición y Salud de Argentina](https://www.sap.org.ar/docs/publicaciones/archivosarg/2024/v122n2a12.pdf)
1. Casa Blanca (2025). [MAHA Report](https://www.whitehouse.gov/wp-content/uploads/2025/05/MAHA-Report-The-White-House.pdf)

### Proyecto
#### Riesgos
##### Inexistencia de datos anteriores para muestras apareadas
La base de datos de la encuesta 2005 (ENNyS 2005) no está publicada en Internet. Una solicitud de datos públicos al Ministerio de Salud de la Nación fue realizada sin resultados aún.

Una posible mitigación consiste en usar el documento de [Resultados de ENNyS 2005](https://cesni-biblioteca.org/archivos/ennys.pdf) y considerar las unidades de análisis que representan a la población cubierta por la ENNyS 2005. La población de interés para el análisis planteado en este trabajo está dado por los niños de 6 meses a 5 años de edad.