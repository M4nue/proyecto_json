import json, funcionesjson

archivo_json = funcionesjson.cargar_json()

continuar = True
while continuar==True:
    opcion_valida = False
    while opcion_valida == False:
        try:
            funcionesjson.menu()
            opcion = int(input('Introduce una opción (1-6): '))
            opcion_valida=funcionesjson.comprobar_opcion_menu(opcion,opcion_valida)
        except:
            print('Ha ocurrido un error, introduce un numero del 1-6')


    if opcion == 1:
        try:
            nombres_tubla=funcionesjson.opcion1(archivo_json)
            nombres_lista=list(nombres_tubla)

            for i,j in zip(nombres_lista[0],nombres_lista[1]):
                print('nombre:',i,'\nimagen:',j,'\n')
        except:
            print('Ha ocurrido un error en la función 1')

    elif opcion == 2:

        try:
            caja=input('Introduce el nombre de la caja que quieres consultar: ')
            resultado=funcionesjson.opcion2(archivo_json,caja)

            for i in resultado:
                print('     ',i,'\n-----------------------------------------------')
            print('Hay un total de', len(resultado),'objetos')
        except:
            print('Ha ocurrido un error en la función 2')

    elif opcion == 3:

        try:
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
        except:
            print('Ha ocurrido un error en la función 3')


    elif opcion == 4:
        try:
            color = input('introduce un color en formato hexadecimal: ')
            cant_obj_hxd = funcionesjson.opcion4(color,archivo_json)
        except:
            print('Ha ocurrido un error en la función 4')

    elif opcion == 5:
        try:
            compra_o_venta =input('¿Deseas mostrar los precios de compra? *por defecto aparece los de venta* S/n: ')
            ordenar = input('¿Deseas invertir el orden de menor a mayor? S/n: ')
            orden = True
            
            if ordenar == 'S':
                orden = False
            else:
                orden = True
            
            if compra_o_venta == 'S':
                resultado=funcionesjson.opcion5_compra(archivo_json,orden)
            else:    
                resultado=funcionesjson.opcion5_venta(archivo_json,orden)
        except:
            print('Ha ocurrido un error en la función 5')    
    
    elif opcion == 6:
        try:
            print('¡¡¡Fin del programa!!!')
            continuar= False
        except:
            print('Ha ocurrido un error en la función 6')