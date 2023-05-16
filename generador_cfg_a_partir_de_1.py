def modificar_cfg(valor, nombre_archivo):
    with open('r-0.8.cfg', 'r') as archivo:
        lineas = archivo.readlines()

    for i in range(len(lineas)):
        if lineas[i].startswith('#-'):
            lineas[i + 1] = f'M {valor}\n'

    with open(nombre_archivo, 'w') as archivo_nuevo:
        archivo_nuevo.writelines(lineas)

    print(f"Se ha generado el archivo {nombre_archivo}.")


tabla = {
    0.8: 10,
    0.84: 9.523809524,
    0.88: 9.090909091,
    0.92: 8.695652174,
    0.96: 8.333333333,
    1: 8,
    1.04: 7.692307692,
    1.08: 7.407407407,
    1.12: 7.142857143,
    1.16: 6.896551724,
    1.2: 6.666666667,
    1.24: 6.451612903,
    1.28: 6.25,
    1.32: 6.060606061,
    1.36: 5.882352941,
    1.4: 5.714285714
}

for r, m in tabla.items():
    nombre_archivo = f"r-{r}.cfg"
    modificar_cfg(m, nombre_archivo)
