import json
def cargar_json():
    with open('./cajas.json', 'r') as fichero_cajas:
        datos = json.load(fichero_cajas)
    return(datos)

def menu():
    print('\n===================================================================')
    print('1º Listar el nombre de las cajas, con una url de la imagen de esta')
    print('2º Introduce el nombre de la caja para ver los objetos que contiene')
    print('3º Mostrar los precios de venta y de compra de las cajas')
    print('4º Introduce un hexadecimal para mostrar los objetos con este color')
    print('5º Mostrar los nombres de las cajas con su tipo, ordenadas')
    print('===================================================================\n')

def opcion1(diccionario):
    nombre=[]
    url=[]
    for i in diccionario:
        nombre.append(i.get("nombre"))
        url.append(i.get("imagen"))

    return nombre,url        
