"""
    1.4 Extraccion de las indisponibilidades del ultimo mes. “indisp2024_0X”
"""

import os  
import zipfile  
import requests  
from bs4 import BeautifulSoup  
import urllib.request  

URL = "https://www.omie.es/en/file-access-list?parents%5B0%5D=/&parents%5B1%5D=Intraday%20Auction%20Market&parents%5B2%5D=7.%20Unavailability&dir=Unavailability%20declaration%20of%20spanish%20bid%20units&realdir=indisp"
DATA_FOLDER = "../data"  # Carpeta para guardar los datos


def get_content(url):
    response = requests.get(url, verify=False)  # Obtener el contenido de la URL
    html_content = response.text  # Obtener el contenido HTML
    return BeautifulSoup(html_content)  # Analizar el HTML con BeautifulSoup


def download_file(file_url, file_name):
    filename = os.path.join(DATA_FOLDER, file_name)  # Ruta completa del archivo
    urllib.request.urlretrieve(file_url, filename)  # Descargar el archivo
    print(f"Downloaded {file_name}")

    if file_name.endswith(".zip"):  # Verificar si el archivo es un ZIP
        with zipfile.ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall(DATA_FOLDER)  # Extraer el contenido del ZIP
        print(f"Extracted contents of {file_name}")
        os.remove(filename)  # Eliminar el archivo ZIP


def main():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)  # Crear la carpeta si no existe

    html_soup = get_content(URL)  # Obtener y analizar el contenido de la URL
    links = html_soup.find_all("td")  # Encontrar todas las etiquetas <td>

    for link in links:
        href_tag = link.find("a")  # Encontrar la etiqueta <a> dentro de <td>
        if href_tag:
            href = href_tag["href"]  # Obtener el atributo href
            file_url = "https://www.omie.es" + href  # Construir la URL completa del archivo
            file_name = href.split("filename=")[-1]  # Obtener el nombre del archivo
            download_file(file_url, file_name)  # Descargar el archivo
            break


if __name__ == "__main__":
    main()  

#3º Visualizacio n de los datos y extraccio n de “insights” u tiles para explicar la informacio n oculta
#dentro de los datos, mediante el uso de gra ficos de matplotlib o plotly. Por ejemplo: Libro de
#ordenes. Para la extraccio n de insights se podra usar cualquier “dataset”

import matplotlib.pyplot as plt  
import os 
import sys  

def read_file(file_path):
    with open(file_path) as file:  # Leer el archivo
        return file.read()  # Devolver el contenido del archivo


def analyze_files(file_paths, top_n):
    occurrence_count = {}  # Diccionario para contar las ocurrencias

    for file_path in file_paths:
        data = read_file(file_path)  # Leer el contenido del archivo
        for line in data.split("\n"):  # Dividir en líneas
            line = line.split(";")  # Dividir cada línea por punto y coma
            if len(line) > 15 and line[15]:  # Verificar la longitud y no vacío
                key = line[15].lower().strip()  # Limpiar y normalizar la clave
                occurrence_count[key] = occurrence_count.get(key, 0) + 1  # Contar las ocurrencias

    # Filtrar para mantener las top_n valores más frecuentes
    return dict(
        sorted(occurrence_count.items(), key=lambda x: x[1], reverse=True)[:top_n]
    )


def visualize_data(filtered_data):
    values = list(filtered_data.keys())  # Extraer las claves
    occurrences = list(filtered_data.values())  # Extraer los valores

    plt.figure(figsize=(10, 6))  
    plt.barh(values, occurrences, color="skyblue")  # Crear un gráfico de barras horizontales
    plt.ylabel("Values")  
    plt.xlabel("Number of occurences")  
    plt.title("Occurences of values in the data")  
    plt.tight_layout()  # Ajustar el diseño
    plt.show()  # Mostrar el gráfico


def main():
    if len(sys.argv) != 2:  # Verificar el número de argumentos
        print("Uso: python visualize_data.py <top_n>")  # Mensaje de uso correcto
        sys.exit(1)  # Salir del programa en caso de error

    directory = "../data"  # Definir el directorio de los archivos
    file_paths = [os.path.join(directory, file) for file in os.listdir(directory)]  # Generar las rutas de los archivos

    filtered_data = analyze_files(file_paths, int(sys.argv[1]))  # Analizar los archivos

    visualize_data(filtered_data)  # Visualizar los datos


if __name__ == "__main__":
    main()  
