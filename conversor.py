import csv

# Función frange personalizada
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

# Función para leer los resultados del archivo .out
def leer_resultados(nombre_archivo):
    resultados = []
    with open(nombre_archivo, 'r') as archivo:
        # Leer el archivo línea por línea
        lineas = archivo.readlines()

        # Iterar sobre las líneas y extraer los datos
        i = 0
        while i < len(lineas):
            if lineas[i].startswith("Trafico/s promediado/s en"):
                trafico = lineas[i].split()[-1].strip(':')
                probabilidad_bloqueo = float(lineas[i+1].split()[-1])
                # confidence_interval_1 = tuple(map(float, lineas[i+2].split(":")[-1].split(",")))
                # confidence_interval_2 = tuple(map(float, lineas[i+3].split(":")[-1].split(",")))
                # number_of_samples = int(lineas[i+4].split()[-1])
                # variance = float(lineas[i+5].split()[-1])
                # standard_deviation = float(lineas[i+6].split()[-1])
                # maximum_sample = int(lineas[i+7].split()[-1])
                # minimum_sample = int(lineas[i+8].split()[-1])

                # Agregar los resultados a la lista
                resultados.append({
                    "trafico": trafico,
                    "probabilidad_bloqueo": probabilidad_bloqueo,
                    # "confidence_interval_1": confidence_interval_1,
                    # "confidence_interval_2": confidence_interval_2,
                    # "number_of_samples": number_of_samples,
                    # "variance": variance,
                    # "standard_deviation": standard_deviation,
                    # "maximum_sample": maximum_sample,
                    # "minimum_sample": minimum_sample
                })

                i += 9  # Saltar las siguientes 9 líneas
            else:
                i += 1

    return resultados

# Valores de r
r_inicio = 0.8
r_final = 1.4
r_incremento = 0.04

# Generar los nombres de archivo
nombres_archivos_out = [f"r-{r:.2f}.cfg.out" for r in frange(r_inicio, r_final + r_incremento, r_incremento)]
nombres_archivos_csv = [f"r-{r:.2f}.csv" for r in frange(r_inicio, r_final + r_incremento, r_incremento)]

# Iterar sobre los nombres de archivo
for nombre_archivo_out, nombre_archivo_csv in zip(nombres_archivos_out, nombres_archivos_csv):
    # Leer los resultados del archivo .out
    resultados = leer_resultados(nombre_archivo_out)

    # Escribir los resultados en el archivo CSV
    with open(nombre_archivo_csv, 'w', newline='') as archivo_csv:
        campos = resultados[0].keys()
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)

        # Escribir la cabecera
        escritor_csv.writeheader()

        # Escribir cada fila de resultados
        for resultado in resultados:
            escritor_csv.writerow(resultado)
