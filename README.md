# <samp>ArquitecturaAPI</samp>
Librerías de Python a instalar: `pip install django django-rest-framework psycopg2`

Después de instalar todo, por favor ejecutar el comando `python manage.py makemigrations` y `python manage.py migrate`.

Luego de aquello, **importar datos** a PostgreSQL. Los datos están en la carpeta **PostgreSQL Data**. La versión que estamos utilizando es la **15**.

----

## <samp>Endpoints</samp>

`/api/`: API Root.

<p><i>Los parámetros deben de ir en el Body</i></p>

----

`/api/valorarClase/`: [**POST**] Endpoint para valorar una clase, los parámetros son: 

| Parámetro  |           Descripción           | Tipo de Dato |
| :--------- | :-----------------------------: | -----------: |
| alumno     | RUT del Alumno que va a evaluar |          int |
| clase      |    ID de la clase a valorar     |          int |
| valoracion |         Nota a evaluar          |          int |

----

`/api/agendarClase/`: [**POST**] Endpoint para agendar una clase como profesor, los parámetros son: 

| Parámetro    |                      Descripción                      | Tipo de Dato |
| :----------- | :---------------------------------------------------: | -----------: |
| fechaInicio  |          Fecha y Hora de inicio de la Clase **`(YYYY-mm-dd HH:MM:ss)`** |     datetime |
| fechaTermino |       Fecha y Hora de finalización de la Clase **`(YYYY-mm-dd HH:MM:ss)`**       |     datetime |
| asignatura   |     ID de la Asignatura la cual tratará la Clase.     |          int |
| profesor     |   RUT del Profesor encargado de realizar la Clase.    |          int |
| link         |                 Link/URL de la Clase.                 |       string |
| plataforma   | ID de la Plataforma en la cual se realizará la Clase. |          int |

