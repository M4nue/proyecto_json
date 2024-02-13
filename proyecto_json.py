import json, funcionesjson

archivo_json = funcionesjson.cargar_json()

funcionesjson.menu()
opcion = int(input('Introduce una opción (1-5): '))

if opcion == 1:
    
    nombres_tubla=funcionesjson.opcion1(archivo_json)
    nombres_lista=list(nombres_tubla)
    for i,j in zip(nombres_lista[0],nombres_lista[1]):
        print('nombre:',i,'\nimagen:',j,'\n')