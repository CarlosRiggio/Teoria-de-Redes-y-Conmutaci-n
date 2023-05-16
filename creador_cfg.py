def modificar_cfg(valor):
    with open('r-08.cfg', 'r') as archivo:
        lineas = archivo.readlines()

    for i in range(len(lineas)):
        if lineas[i].startswith('#-'):
            lineas[i + 1] = f'M {valor}\n'

    with open('nuevo_archivo.cfg', 'w') as archivo_nuevo:
        archivo_nuevo.writelines(lineas)

valor_ingresado = input("Ingresa el valor para reemplazar la primera M: ")
modificar_cfg(valor_ingresado)
print("Se ha generado el nuevo archivo cfg.")
