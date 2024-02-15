import json, funcionesjson

archivo_json = funcionesjson.cargar_json()

funcionesjson.menu()
opcion = int(input('Introduce una opción (1-5): '))

if opcion == 1:
    
    nombres_tubla=funcionesjson.opcion1(archivo_json)
    nombres_lista=list(nombres_tubla)
    for i,j in zip(nombres_lista[0],nombres_lista[1]):
        print('nombre:',i,'\nimagen:',j,'\n')

elif opcion == 2:
    caja=input('Introduce el nombre de la caja que quieres consultar: ')
    resultado=funcionesjson.opcion2(archivo_json,caja)
    for i in resultado:
        print('     ',i,'\n-----------------------------------------------')
    print('Hay un total de', len(resultado),'objetos')

elif opcion == 3:
    precio_minimo = float(input('introduce el precio minimo de coste de la caja: '))
    precio_maximo = float(input('introduce el precio maximo de coste de la caja: '))
    print(type(precio_maximo))
    cajas_rango = funcionesjson.opcion3(precio_minimo,precio_maximo,archivo_json)