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

    cajas_rango_compra = funcionesjson.opcion3_compra(precio_minimo,precio_maximo,archivo_json)
    cajas_rango_venta = funcionesjson.opcion3_venta(precio_minimo,precio_maximo,archivo_json)

    print('El precio de las cajas al comprar esta en:\n')
    for i,j in zip(cajas_rango_compra[0],cajas_rango_compra[1]):
        print('     ',i,'=',j,'\n----------------------------------------')

    print('El precio de las cajas al vender esta en: \n')
    for i,j in zip(cajas_rango_venta[0],cajas_rango_venta[1]):
        print('     ',i,'=',j,'\n----------------------------------------')

elif opcion == 4:

    color = input('introduce un color en formato hexadecimal: ')
    cant_obj_hxd = funcionesjson.opcion4(color,archivo_json)

elif opcion == 5:
    ordenar = input('¿Deseas invertir el orden de menor a mayor? S/n: ')
    orden = True
    if ordenar == 'S':
        orden = False
    else:
        orden = True
    resultado=funcionesjson.opcion5_venta(archivo_json,orden)