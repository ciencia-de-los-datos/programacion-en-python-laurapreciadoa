"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv
    data = open ("data.csv", "r").readlines ()
    valores_en_columna= [int(k[2]) for k in data]
    total_suma=sum (valores_en_columna)
    return total_suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    import csv
    data = open ("data.csv", "r").readlines () 
    columna_uno= [k[0][0] for k in data] 
    columna_uno.sort() 
    resultados = [(k,columna_uno.count(k)) for k in set(columna_uno)]
    resultados.sort ()
    return resultados


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    data = open ("data.csv", "r").readlines () 
    columna_uno = [k[0][0] for k in data]
    columna_dos = [int(k[2]) for k in data]  
    valores_únicos = list(set(columna_uno))
    valores_únicos.sort()
    resultados = dict.fromkeys(valores_únicos, 0)

    for k in range(len(data)):
        resultados[columna_uno[k]] += columna_dos[k]
    return list(resultados.items())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data = open ("data.csv", "r").readlines () 
 
    meses = [k[9] + k[10] for k in data]
    meses.sort()
    meses_unicos = list(set(meses))
    meses_unicos.sort()
    resultados = []

    for mes in meses_unicos:
      cantidad = meses.count(mes)
      resultados.append((mes, cantidad))
    return resultados


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = open ("data.csv", "r").readlines () 

    columna_uno= [k[0][0] for k in data]
    columna_dos= [int(k[2]) for k in data]
    valores_unicos=list(set(columna_uno))
    valores_unicos.sort ()
    respuesta_min = dict.fromkeys(valores_unicos, float('inf'))
    respuesta_max = dict.fromkeys(valores_unicos, -float('inf'))
    for k in range(len (data)):
        if columna_dos[k]<respuesta_min[columna_uno[k]]:
            respuesta_min[columna_uno[k]] = columna_dos[k]
        if columna_dos[k]>respuesta_max[columna_uno[k]]:
             respuesta_max[columna_uno[k]]= columna_dos[k]
    return [(letra, respuesta_max[letra], respuesta_min[letra]) for letra in respuesta_min]


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    data = open ("data.csv", "r").readlines () 

    min_values = {}
    max_values = {}

    for line in data:
        fields = line.replace("It", " ").split()
        column = fields[4].split(",")

        for item in column:
            key, value = item.split(":")
            value = int(value)

            if key in min_values:
                if min_values[key] > value:
                    min_values[key] = value
                elif max_values[key] < value:
                    max_values[key] = value
            else:
                min_values[key] = value
                max_values[key] = value

    resultado = [(key, min_values[key], max_values[key]) for key in min_values]
    resultado.sort()            
    return resultado


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = open ("data.csv", "r").readlines () 
    columna_uno = [line.split()[0] for line in data]
    columna_dos = [int(line.split()[1]) for line in data]

    valores_unicos = sorted(set(columna_dos))

    respuesta = {valor: [] for valor in valores_unicos}

    for i, valor in enumerate(columna_dos):
        respuesta[valor].append(columna_uno[i])

    resultado = list(respuesta.items())
    return resultado


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data = open ("data.csv", "r").readlines () 
    columna_uno = [k[0][0] for k in data]
    columna_dos = [int(k[2]) for k in data] 
    valores_unicos_columna_dos = sorted(set(columna_dos))
    result = []

    for valor in valores_unicos_columna_dos:
        letras_asociadas = sorted(list(set(columna_uno[i] for i, v in enumerate(columna_dos) if v == valor)))
        result.append((valor, letras_asociadas))

    result.sort()
    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    respuesta = {}
    data = open ("data.csv", "r").readlines ()
    for line in data:
        fields = line.replace("\t", " ").split()
        columna_cinco_values = fields[4].split(",")

        for element in columna_cinco_values:
            clave, numero = element.split(":")
            if clave not in respuesta:
                respuesta[clave] = 1
            else:
                respuesta[clave] += 1

    sorted_items = sorted(respuesta.items())
    respuesta = dict(sorted_items)
    return respuesta


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = open ("data.csv", "r").readlines ()
    columna1 = []
    columna2 = []
    columna3 = []

    for line in data:
        fields = line.replace("\t", " ").split()
        columna1.append(fields[0])
        columna2.append(len(fields[3].split(",")))
        columna3.append(len(fields[4].split(",")))

    resultado = list(map(lambda x, y, z: (x, y, z), columna1, columna2, columna3))
    return resultado


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    import csv
    data = open ("data.csv", "r").readlines ()


    def calcular_suma_columna2_por_letra_columna4(data):
        suma_por_letra = {}

        for linea in data:
            campos = linea.replace("\t", " ").split()
            columna3 = campos[3]
            valor_columna2 = int(campos[1])

            claves = columna3.split(",")

            for clave in claves:
                if clave in suma_por_letra:
                    suma_por_letra[clave] += valor_columna2
                else:
                    suma_por_letra[clave] = valor_columna2

        suma_por_letra = dict(sorted(suma_por_letra.items()))
        return suma_por_letra

    resultado = calcular_suma_columna2_por_letra_columna4(data)
    return resultado


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import csv
    data = open ("data.csv", "r").readlines ()

    columna1 = [k[0][0] for k in data]
    unicos = list(set(columna1))
    unicos.sort()
    respuesta = dict.fromkeys(unicos, 0)
    
    for linea in data:
        campos = linea.replace("\t", " ").split()
        clave = campos[0]
        valores = campos[4].split(",")
        suma = 0
        
        for elemento in valores:
            suma += int(elemento.split(":")[1])
        
        respuesta[clave] += suma
    return respuesta
