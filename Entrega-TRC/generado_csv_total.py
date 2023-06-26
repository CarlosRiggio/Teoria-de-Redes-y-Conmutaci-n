import csv

# Lista para almacenar los datos combinados
datos_combinados = []

# Leer los archivos CSV y combinar los datos
for r in range(80, 141, 4):
    nombre_archivo = f'r-{r/100:.2f}.csv'

    with open(nombre_archivo, 'r') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for row in reader:
            fila_existente = next((fila for fila in datos_combinados if fila['r'] == r/100), None)

            if fila_existente:
                fila_existente[row['trafico']] = row['probabilidad_bloqueo']
            else:
                nueva_fila = {'r': r/100, row['trafico']: row['probabilidad_bloqueo']}
                datos_combinados.append(nueva_fila)

# Escribir los datos combinados en el archivo de salida
with open('todos_bloqueos.csv', 'w', newline='') as archivo_salida:
    fieldnames = ['r', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    writer = csv.DictWriter(archivo_salida, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(datos_combinados)
