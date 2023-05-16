import os
import glob

# Define los parámetros para el comando
parametros = "-s23 -q0.95 -t0.002 -c"

# Obtiene la lista de archivos que coinciden con el patrón
archivos = glob.glob("r-*.cfg")

# Itera sobre los archivos
for archivo in archivos:
    # Crea el comando completo
    comando = f"./SimRedMMkk {parametros} {archivo}"

    # Ejecuta el comando
    os.system(comando)
