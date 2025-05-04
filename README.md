# CEFIRE Cursos Scraper

Este script de Python extrae la información de los cursos disponibles en la web del CEFIRE (Centros de Formación, Innovación y Recursos Educativos) y la guarda en un archivo CSV.

## Propósito

La interfaz web del CEFIRE para la consulta de cursos puede resultar poco práctica para algunas personas. Este script surge como una alternativa para obtener la información de los cursos de forma estructurada y fácilmente manipulable, por ejemplo, para filtrar, ordenar o importar los datos a otras herramientas.

## Características

* **Scrapeo automático:** Extrae la información relevante de los cursos directamente de la página web del CEFIRE, navegando por las diferentes páginas de resultados.
* **Formato CSV:** Guarda los datos en un archivo llamado `cursos.csv` (delimitado por punto y coma `;`), un formato estándar y compatible con la mayoría de hojas de cálculo y programas de análisis de datos.
* **Identificación de fin de página:** El script detecta automáticamente cuándo no hay más cursos para extraer, evitando errores.
* **Información detallada:** Extrae el código del curso, título, localidad, fecha de inicio, fecha de fin, número de horas y estado.

## Requisitos

* **Python 3.x:** Asegúrate de tener Python 3 instalado en tu sistema.
* **Librerías Python:** El script utiliza las siguientes librerías, que puedes instalar con `pip`:
    ```bash
    pip install requests beautifulsoup4
    ```
    * `requests`: Para realizar las peticiones HTTP a la página web.
    * `beautifulsoup4` (bs4): Para analizar el HTML de la página y extraer la información.

## Instalación

1.  **Clona el repositorio (opcional):** Si has subido el script a un repositorio de GitHub, puedes clonarlo:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```
2.  **Descarga el script:** Si solo tienes el archivo `.py`, descárgalo a tu directorio local.
3.  **Instala las dependencias:** Si aún no las tienes instaladas, ejecuta el comando:
    ```bash
    pip install requests beautifulsoup4
    ```

## Uso

1.  **Ejecuta el script:** Abre una terminal o línea de comandos, navega hasta el directorio donde guardaste el script y ejecuta:
    ```bash
    python nombre_del_script.py
    ```
    *(Reemplaza `nombre_del_script.py` con el nombre real de tu archivo Python).*

2.  **Archivo CSV generado:** Una vez que el script finalice, se creará un archivo llamado `cursos.csv` en el mismo directorio. Este archivo contendrá la información de los cursos extraídos, con los campos separados por punto y coma (`;`).

## Formato del archivo CSV

El archivo `cursos.csv` contendrá las siguientes columnas:

* **Código:** Identificador único del curso.
* **Título:** Nombre del curso.
* **Localidad:** Lugar donde se imparte el curso (puede ser online).
* **Inicio:** Fecha de inicio del curso.
* **Fin:** Fecha de finalización del curso.
* **Horas:** Duración del curso en horas.
* **Estado:** Estado actual del curso (por ejemplo, "Preinscripción abierta").

Los campos estarán separados por punto y coma (`;`).

## Consideraciones y Advertencias

* **Cambios en la web del CEFIRE:** La estructura de la página web del CEFIRE puede cambiar en el futuro, lo que podría hacer que el script deje de funcionar correctamente. En ese caso, sería necesario actualizar el script para adaptarlo a los nuevos cambios, especialmente los selectores CSS (`tbody#mantenimiento` y las etiquetas `td` dentro de las filas `tr`).
* **Términos de uso:** Asegúrate de revisar los términos de uso del sitio web del CEFIRE. Un scraping excesivo o no autorizado podría considerarse inapropiado. Este script se proporciona con la intención de facilitar el acceso a la información pública.
* **Mejoras:** Este script es una versión funcional. Se podrían añadir funcionalidades como:
    * Filtrado de cursos por criterios (palabra clave, provincia, etc.) directamente en el script o posteriormente analizando el CSV.
    * Guardado de la información en otros formatos (JSON, Excel).
    * Interfaz gráfica de usuario (GUI).
    * Programación de la ejecución del script para obtener actualizaciones periódicas.

## Contribuciones

Siéntete libre deForkear este repositorio y realizar mejoras. ¡Las pull requests son bienvenidas!

## Licencia

[Aquí puedes añadir la licencia bajo la que distribuyes tu código, por ejemplo, MIT License]

## Contacto

[Tu nombre o alias]
[Tu correo electrónico (opcional)]
[Enlace a tu perfil de GitHub (opcional)]
