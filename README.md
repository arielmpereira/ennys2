# Análisis de la ENNyS 2

---
## ¿Por qué este proyecto?

* Datos **oficiales y representativos** de Argentina. ENNyS 2 es la foto nutricional y de salud más completa y reciente del país. Poner el foco en ultraprocesados en adultos conecta con hipertensión, diabetes, obesidad y costos sanitarios directos.

* Tema **socialmente relevante**: impacto de ultraprocesados en salud adulta. No es un tema técnico aislado: responde a una pregunta socialmente relevante —¿cuánto aportan los ultraprocesados a empeorar indicadores de salud?

* Permite aplicar todos los temas de Análisis de Datos II: inferencia paramétrica y no paramétrica, comparaciones múltiples, bootstrap, modelos..

* Aprendizaje “del mundo real: Datos oficiales y multi‑archivo, filtrado por subpoblaciones, joins con diccionarios, manejo de faltantes y decisiones de codificación. Es exactamente lo que nos van a pedir afuera.


---
## Instructivo de descarga de las bases de datos

**Importante:**  
Los archivos originales de ENNyS 2 son grandes (varios superan los 100 MB) y **GitHub no permite subir archivos individuales de más de 100 MB**.  
Por eso, **no se incluyen en este repositorio**. Cada integrante debe descargarlos desde las fuentes oficiales, descomprimirlos y guardarlos localmente en la carpeta `data/`.


---

### 1. Base principal de la encuesta

Qué contiene:
datos sociodemográficos, antropométricos, salud autorreportada, hábitos, actividad física, etc. Incluye identificadores para vincular con otras bases.

Link de descarga:
http://datos.salud.gob.ar/dataset/2d008878-d0d7-44d8-a6f8-e5ec1ed769fe/resource/ed886299-7c31-4bce-9d13-d41a97210b24/download/ennys2_encuesta.zip

---
### 2. Base de Alimentos, Bebidas y Suplementos

Qué contiene:
Registro detallado del consumo individual del recordatorio de 24 horas. Cada fila corresponde a un alimento/bebida/suplemento consumido por una persona, con cantidad y unidad.

Link de descarga:
http://datos.salud.gob.ar/dataset/2d008878-d0d7-44d8-a6f8-e5ec1ed769fe/resource/42e971e2-8d80-4c26-94fd-e7b28fb570a3/download/base_alimentos_bebidas_suplementos.zip

---
### 3. Tabla de Composición de Alimentos
Qué contiene:
Listado maestro de alimentos, bebidas y suplementos con su composición nutricional por porción o por 100 g/ml (energía, macronutrientes, micronutrientes).

Link de descarga:
http://datos.salud.gob.ar/dataset/2d008878-d0d7-44d8-a6f8-e5ec1ed769fe/resource/815688ad-d43a-490c-95c6-cb366fc09d75/download/base_nutrientes.zip

---

## Documentación recomendada

Antes de comenzar con el análisis, se recomienda leer la siguiente documentación para familiarizarse con la estructura y el contenido de las bases de datos:

1. **Manual metodológico ENNyS 2**  
   Explica el diseño muestral, los cuestionarios aplicados, la población objetivo y el procedimiento de recolección de datos.  
   Archivo: `doc/ennys2_manual_metodologico.doc`

2. **Base de nutrientes (SARA 2)**  
   Describe el sistema argentino de alimentos, la estructura de la tabla de composición y el significado de cada campo.  
   Archivo: `doc/base_nutrientes.pdf`  
   *(Usada para convertir el consumo de alimentos en nutrientes totales y clasificar ultraprocesados)*

3. **Base de alimentos, bebidas y suplementos**  
   Explica la codificación de alimentos, bebidas y suplementos utilizada en la encuesta.  
   Archivo: `doc/base_alimentos_bebidas_suplementos.pdf`

4. **Diccionario de variables (ennys2_variables.csv)**  
   Lista de variables presentes en la base principal y su descripción.  
   Archivo: `doc/ennys2_variables.csv`  
   *(No hay versión oficial en PDF; este CSV cumple esa función)*

---

**Recomendación:**  Comenzar leyendo el *Manual metodológico* para entender cómo se recolectaron los datos, luego revisar el *diccionario de variables* y finalmente explorar las tablas de alimentos y nutrientes para comprender cómo se calculan los indicadores que vamos a usar.


