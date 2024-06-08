import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def read_file(file_path):
    with open(file_path) as file:
        return file.read()

def analyze_files(file_paths):
    occurrence_count = {}

    for file_path in file_paths:
        data = read_file(file_path)
        for line in data.split("\n"):
            line = line.split(";")
            if len(line) > 15 and line[15]:
                key = line[15].lower().strip()
                occurrence_count[key] = occurrence_count.get(key, 0) + 1

    # Convertir el diccionario en un dataframe de pandas
    df = pd.DataFrame(list(occurrence_count.items()), columns=['Values', 'Number of occurences'])

    # Ordenar el dataframe por el número de ocurrencias y seleccionar las top_n filas
    df = df.sort_values(by='Number of occurences', ascending=False).head(20)

    return df
#Para la representación de las indisponibilidades más destacables, se sigue la siguiente distribución:
#Gráfico de barras para que muestre las 20 indisponibilidades más frecuentes indicando el número de veces que ha sucedido cada una.
def visualize_data_bar(filtered_data):
    plt.figure(figsize=(10, 6))
    plt.barh(filtered_data['Values'], filtered_data['Number of occurences'], color="skyblue")
    plt.ylabel("Values")
    plt.xlabel("Number of occurences")
    plt.title("Top 20 Occurences of values in the data")
    plt.tight_layout()
    plt.show()

#Gráfico de linea para entender de forma sucesiva la tendencia de las indisponibilidades por orden de frecuencia de mayor a menor
def visualize_data_line(filtered_data):
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_data['Values'], filtered_data['Number of occurences'], marker='o', linestyle='-')
    plt.xlabel("Values")
    plt.ylabel("Number of occurences")
    plt.title("Top 20 Occurences of values in the data (Line Chart)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#Gráfico de pastel para mostrar la distribución porcentual de los diferentes tipos de eventos.
def visualize_data_pie(filtered_data):
    plt.figure(figsize=(8, 8))
    plt.pie(filtered_data['Number of occurences'], labels=filtered_data['Values'], autopct='%1.1f%%', startangle=140)
    plt.title("Top 20 Occurences of values in the data (Pie Chart)")
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    plt.show()

def main():
    directory = "../data"
    file_paths = [os.path.join(directory, file) for file in os.listdir(directory)]

    filtered_data = analyze_files(file_paths)

    visualize_data_bar(filtered_data)
    visualize_data_line(filtered_data)
    visualize_data_pie(filtered_data)

if __name__ == "__main__":
    main()
