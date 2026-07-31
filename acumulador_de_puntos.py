ids = []
participantes = []
categorias = []
fechas = []
puntos = []
niveles = []
observaciones = []
#-----------------------------------------#
#--|menu_principal_acumulador_de_puntos|--#
#-----------------------------------------#
while True:
    print("menu principal acumulador de puntos")
    print("1) crear puntos")
    print("2) editar puntos")
    print("3) eliminar puntos")
    print("4) buscar puntos")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #------------------#
    #--|crear_puntos|--#
    #------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_punto = 1
        else:
            id_punto = ids[-1] + 1
        participante = input("nombre del participante: ")
        categoria = input("categoría: ")
        fecha = input("fecha del registro: ")
        punto = int(input("cantidad de puntos: "))
        nivel = input("nivel (bronce/plata/oro/platino): ")
        observacion = input("observación: ")
        ids.append(id_punto)
        participantes.append(participante)
        categorias.append(categoria)
        fechas.append(fecha)
        puntos.append(punto)
        niveles.append(nivel)
        observaciones.append(observacion)
        print("puntos registrados correctamente.")
        print("id:", id_punto)
    #-------------------#
    #--|editar_puntos|--#
    #-------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar puntos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {participantes[i]} | {categorias[i]} | {fechas[i]} | {puntos[i]} | {niveles[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {participantes[posicion]} | {categorias[posicion]} | {fechas[posicion]} | {puntos[posicion]} | {niveles[posicion]} | {observaciones[posicion]}")
                participantes[posicion] = input("nuevo participante: ")
                categorias[posicion] = input("nueva categoría: ")
                fechas[posicion] = input("nueva fecha: ")
                puntos[posicion] = int(input("nueva cantidad de puntos: "))
                niveles[posicion] = input("nuevo nivel: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|eliminar_puntos|--#
    #---------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar puntos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {participantes[i]} | {categorias[i]} | {fechas[i]} | {puntos[i]} | {niveles[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {participantes[posicion]} | {categorias[posicion]} | {fechas[posicion]} | {puntos[posicion]} | {niveles[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    participantes.pop(posicion)
                    categorias.pop(posicion)
                    fechas.pop(posicion)
                    puntos.pop(posicion)
                    niveles.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #-------------------#
    #--|buscar_puntos|--#
    #-------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar puntos")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {participantes[posicion]} | {categorias[posicion]} | {fechas[posicion]} | {puntos[posicion]} | {niveles[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma = 0
            mayor = puntos[0]
            menor = puntos[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {participantes[i]} | {categorias[i]} | {fechas[i]} | {puntos[i]} | {niveles[i]} | {observaciones[i]}")
                suma += puntos[i]
                if puntos[i] > mayor:
                    mayor = puntos[i]
                if puntos[i] < menor:
                    menor = puntos[i]
            promedio = suma / len(ids)
            print("estadísticas acumulador de puntos")
            print("cantidad de registros:", len(ids))
            print("puntos acumulados:", suma)
            print("promedio de puntos:", round(promedio, 2))
            print("mayor puntaje:", mayor)
            print("menor puntaje:", menor)
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el programa.")
        break
    else:
        print("opción inválida.")