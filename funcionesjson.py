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
    print('6º Fin del programa')
    print('===================================================================\n')

def opcion1(diccionario):
    nombre=[]
    url=[]
    for i in diccionario:
        nombre.append(i.get("nombre"))
        url.append(i.get("imagen"))

    return nombre,url  

def comprobar_caja(caja,diccionario,correcto):
    nombres=[] 
    for i in diccionario:
        nombres.append(i['nombre'])
    if caja in nombres:
        correcto= True
    else:
        print('El nombre de la caja no existe, introduce un existente\n')
        correcto= False
    return correcto

     

def opcion2(diccionario,caja_input):
    objetos = []
    for i in diccionario:
        if i['nombre'] == caja_input:
            for j in i['descripción']['contenido']:
                objetos.append(list(j.values())[0])
                
    return objetos

def opcion3_comprobar_compra_venta(minimo,maximo,correcto):
    if minimo > maximo:
        print('Introduce otros valores donde el minimo sea menor que el maximo\n')
        correcto=False
    else:
        correcto=True
    return correcto


def opcion3_compra(minimo,maximo,diccionario):
    cajas_compra = []
    precio_cajas=[]
    for i in diccionario:
        precio=i['precio_compra']
        precio=precio.replace('$','')
        precio=float(precio)
        if precio >= minimo and precio <= maximo:
            cajas_compra.append(i['nombre'])
            precio_cajas.append(precio)
    return cajas_compra, precio_cajas    

def opcion3_venta(minimo,maximo,diccionario):
    cajas_venta = []
    precio_cajas = []
    for i in diccionario:
        precio=i['sale_price_text']
        precio=precio.replace('$','')
        precio=float(precio)
        if precio >= minimo and precio <= maximo:
            cajas_venta.append(i['nombre'])
            precio_cajas.append(precio)
    return cajas_venta, precio_cajas  

def opcion4(hexadecimal,diccionario):
    for i in diccionario:
        cantidad = []
        objetos = []
        for j in i['descripción']['contenido']:
            valor_hxd_j = list(j.values())[1]
            valor_obj_j = list(j.values())[0]
            if hexadecimal == valor_hxd_j:
                cantidad.append(valor_hxd_j)
                objetos.append(valor_obj_j)
                
        print('\nPara la caja',i['nombre'],'hay un total de',len(cantidad),'objetos con ese hexadecimal y son:\n')
        for z in objetos:
            print(z,'\n------------------------')

def opcion5_venta (diccionario,orden):
    cajas = []
    descripcion = []
    precio_venta = []
    coincidencias = []
    for i in diccionario:
        precio = i['sale_price_text']
        precio = precio.replace('$','')
        precio=float(precio)
        precio_venta.append(precio)
        precio_venta.sort(reverse=orden)
    
    for i in diccionario:
        precio = float(i['sale_price_text'].replace('$',''))
        if precio in precio_venta:
            indice_z = precio_venta.index(precio)
            cajas.insert(indice_z, i['nombre'])
            descripcion.insert(indice_z, i['descripción']['tipo'])
        else:
            cajas.append(i['nombre'])
            descripcion.append(i['descripción']['tipo'])
    
    for i in range(len(cajas)):
        print('Caja:',cajas[i],'------ Calidad:',descripcion[i],'------ Precio de venta:',precio_venta[i])
    
    for i in descripcion:
        repetidas=descripcion.count(i)
        if i in descripcion and i not in coincidencias:
            coincidencias.append(i)
            print('Hay',repetidas,i)


def opcion5_compra (diccionario,orden):
    cajas = []
    descripcion = []
    precio_compra = []
    coincidencias = []
    for i in diccionario:
        precio = i['precio_compra']
        precio = precio.replace('$','')
        precio=float(precio)
        precio_compra.append(precio)
        precio_compra.sort(reverse=orden)
    
    for i in diccionario:
        precio = float(i['precio_compra'].replace('$',''))
        if precio in precio_compra:
            indice_z = precio_compra.index(precio)
            cajas.insert(indice_z, i['nombre'])
            descripcion.insert(indice_z, i['descripción']['tipo'])
        else:
            cajas.append(i['nombre'])
            descripcion.append(i['descripción']['tipo'])

    for i in range(len(cajas)):
        print('Caja:',cajas[i],'------ Calidad:',descripcion[i],'------ Precio de compra:',precio_compra[i])
    
    for i in descripcion:
        repetidas=descripcion.count(i)
        if i in descripcion and i not in coincidencias:
            coincidencias.append(i)
            print('Hay',repetidas,i)


def comprobar_opcion_menu(opcion,valida):
    if opcion <1 or opcion > 6:
        print('Por favor introduce una opción valida')
    else:
        valida=True
    return valida
        