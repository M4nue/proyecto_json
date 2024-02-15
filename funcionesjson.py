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

def opcion2(diccionario,caja_input):
    objetos = []
    for i in diccionario:
        if i['nombre'] == caja_input:
            for j in i['descripción']['contenido']:
                objetos.append(list(j.values())[0])
                
    return objetos

def opcion3(minimo,maximo,diccionario):
    for i in diccionario:
        precio=i['precio_compra']
        precio.replace('$','')
        print(precio)
        precio=float(precio)
        if precio >= minimo and precio <= maximo:
            print(i['nombre'])
    



