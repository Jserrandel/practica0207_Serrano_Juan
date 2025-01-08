def limpiar(cifra):
    """
    Función que elimina los puntos de separación de miles y cambia las comas de separación de decimales por puntos.
    Parámetros:
        - cifra: Es una cadena con una cifra
    Devuelve:
        Un real con la cifra de la cadena después de eliminar el separador de miles y cambiar el separador de decimales por punto.
    """
    cifra = cifra.replace('.', '')
    cifra = cifra.replace(',','.')
    return float(cifra) 

def preprocesado(ruta):
    """
    Función que preprocesa los datos contenidos en un fichero con formato csv y devuelve un diccionario con los nombres de las columnas como claves y las listas de valores asociados a ellas.
    Parámetros:
        - ruta: Es una cadena con la ruta del fichero.
    Devuelve:
        Un diccionario con pares formados por los nombres de las columnas y las listas de valores en las columnas.
    """
    try:
        with open(ruta, 'r') as f:
            lineas = f.read().split('\n')
    except FileNotFoundError:
        print('El fichero no existe.')
        return
    
    claves = lineas.pop(0).split(";")
    cotizaciones = {}
    for i in claves:
        cotizaciones[i] = []
    for linea in lineas:
        campos = linea.split(';')
        cotizaciones[claves[0]].append(campos[0])
        for i in range(1, len(campos)):
            cotizaciones[claves[i]].append(limpiar(campos[i]))
    return cotizaciones


def resumen_cotizacion(cotizaciones, ruta):
    """
    Función que recibe un diccionario con los valores de cotización y crear un fichero con un resumen con el mínimo, el máximo y la media.
    Parámetros:
        - cotizaciones: Es un diccionario con pares cuyas claves son los nombres de la variables medidas y cuyos valores son las listas de valores de cada variable.
        - ruta: Es una cadena con la ruta del fichero.
    """
    del(cotizaciones['Nombre'])
    contenido = ""
    contenido += 'Nombre'
    for i in cotizaciones:
        contenido += ";" + i
    contenido += '\nMínimo'
    for i in cotizaciones.values():
        contenido += ';' + str(min(i))
    contenido += '\nMáximo'
    for i in cotizaciones.values():
        contenido += ';' + str(max(i))
    contenido += '\nMedia'
    for i in cotizaciones.values():
        contenido += ';' + str(sum(i)/len(i))
    with open(ruta, 'w') as f:
        f.write(contenido)
    return


cotizaciones = preprocesado('cotizacion.csv')
print(cotizaciones)
resumen_cotizacion(cotizaciones, 'resumen-cotizacion.csv')