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

            # Buscar los elementos que contienen la información de los cursos
            cursos_tabla = soup.find("tbody", {"id": "mantenimiento"})  # Ajustar según el HTML específico
            
            #TODO
            #Hay que contar los tr que encontramos dentro:
                # Si solo hay uno, significa que no hay más cursos en current page
                # Si hay más de uno, significa que hay más cursos en current page
            # Tenemos que escapar el primer elemento, ya que es el encabezado de la tabla

            if not cursos_tabla:
                finished = True
                break
            else:
                for curso_fila in cursos_tabla.find_all("tr"):
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

if __name__ == "__main__":
    main()
# Este script utiliza requests para obtener el contenido de la página y BeautifulSoup para analizar el HTML.