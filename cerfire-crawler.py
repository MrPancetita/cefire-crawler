import requests
from bs4 import BeautifulSoup

class Curso:
    def __init__(self, codigo, titulo, localidad, inicio, fin, horas, estado):
        self.codigo = codigo
        self.titulo = titulo
        self.localidad = localidad
        self.inicio = inicio
        self.fin = fin
        self.horas = horas
        self.estado = estado

    def __str__(self):
        return f"{self.codigo} - {self.titulo} - {self.localidad} - {self.inicio} - {self.fin} - {self.horas}h - {self.estado}"

def main():
    # URL de la página
    cursos = []
    page = 1
    finished = False

    while not finished:
        # URL de la página
        url = f"https://cefire.edu.gva.es/sfp/index.php?seccion=ediciones&pagina={page}"

        # Obtener el contenido de la página
        response = requests.get(url)
        response.encoding = 'utf-8'  # Asegurarse de que la codificación sea correcta

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            # Si la tabla está vacía, recuperaremos 3 elementos en cursos_tabla que serán:
            # 0. '\n'
            # 1. <tr class=cabecera>...</tr>
            # 2. '\n'

            cursos_tabla = soup.find("tbody", {"id": "mantenimiento"})  # Ajustar según el HTML específico
            
            if len(cursos_tabla) <= 3:
                finished = True
                break
            else:
                # Skip the header row and empty elements
                for i, curso_fila in enumerate(cursos_tabla.find_all("tr")):
                    # Skip the first 3 elements
                    if i < 3:
                        continue
                    datos = curso_fila.find_all("td")  # Ajustar según el HTML específico
                    
                    if datos:
                        codigo = datos[0].text.strip()
                        titulo = datos[1].text.strip()
                        localidad = datos[2].text.strip()
                        inicio = datos[3].text.strip()
                        fin = datos[4].text.strip()
                        horas = datos[5].text.strip()
                        estado = datos[6].text.strip()
                        print(f"{codigo} - {titulo} - {localidad} - {inicio} - {fin} - {horas}h - {estado}")

                        # Crear un objeto Curso y agregarlo a la lista
                        curso = Curso(codigo, titulo, localidad, inicio, fin, horas, estado)
                        cursos.append(curso)
                page += 1

    else:
        print("Error al acceder a la página.")

    # Guardar los cursos en un nuevo archivo CSV utilizando ; como separador
    with open("cursos.csv", "w", encoding="utf-8") as f:
        f.write(b'\xEF\xBB\xBF'.decode('utf-8'))  # Añadir BOM para UTF-8
        # Escribir la cabecera del CSV
        f.write("Código;Título;Localidad;Inicio;Fin;Horas;Estado\n")
        # Escribir los datos de los cursos
        for curso in cursos:
            f.write(f"{curso.codigo};{curso.titulo};{curso.localidad};{curso.inicio};{curso.fin};{curso.horas};{curso.estado}\n")
    print("Cursos guardados en cursos.csv")

if __name__ == "__main__":
    main()    

# Este script utiliza requests para obtener el contenido de la página y BeautifulSoup para analizar el HTML.