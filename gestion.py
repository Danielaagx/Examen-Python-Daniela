import gestion_archivos
diccionario_herramientas ={}
def cargar_inventario_inicial():
    lista_previa = gestion_archivos.cargar_reparaciones()
    for elemento in lista_previa:
        diccionario_herramientas[elemento["id_herramienta"]] = {
            "nombre": elemento["nombre"],
            "estado": elemento["estado"],
        }
def registrar_herramienta():
    print("\n Registro de herramienta")
    id_herramienta = input("Ingrese el ID de la herramienta:").strip()
    if id_herramienta in diccionario_herramientas:
        print("Error: El ID ingresado ya se encuentra registrado")
        return
    nombre_herramienta = input("Ingrese el nombre de la herramienta:")
    if not nombre_herramienta:
        print("El espacio no puede estar vacio")
        return
    diccionario_herramientas[id_herramienta] ={
        "nombre": nombre_herramienta,
        "estado": "Activa",
    }
    print(f"Herramienta '{nombre_herramienta}' registrada como 'Activa' ")
def registrar_reparacion():
    print("\n Registrar_reparacion")
    if not diccionario_herramientas:
        print("No se encontraron herramientas disponibles")
        return
    id_herramienta = input(
        "Ingrese el ID de la herramienta que desea reparar:"
    ).strip()
    if id_herramienta not in diccionario_herramientas:
        print("Error: no se encontro la herramienta en el diccionario")
        return
    herramienta_actual = diccionario_herramientas[id_herramienta]
    if herramienta_actual["estado"] == "En reparacion":
        print("La herramienta se encuentra en estado: 'En reparacion' ")
        return 
    fecha_inicio = input(
        "Ingrese la fecha de inicio de la reparacion (DD/MM/AAAA):"
    ).strip()
    fecha_estimada_finalizacion = input(
        "Ingrese la fecha estimada en la que finalizara la reparacion (DD/MM/AAAA):"
    ).strip()
    observaciones = input("Ingrese las observaciones de la herramienta:").strip()
    herramienta_actual["estado"] ="En reparacion"
    datos_herramienta = {
        "id_herramienta": id_herramienta,
        "nombre": herramienta_actual["nombre"],
        "fecha_inicio_reparacion": fecha_inicio,
        "fecha_estimada_finalizacion": fecha_estimada_finalizacion,
        "observaciones": observaciones,
    }
    lista_reparaciones = gestion_archivos.cargar_reparaciones()
    nueva_lista = []
    for elemento in lista_reparaciones:
        if elemento["id_herramienta"] != id_herramienta:
            nueva_lista.append(elemento)
    nueva_lista.append(datos_herramienta)
    gestion_archivos.guardar_reparaciones(nueva_lista)
    print(f"El estado de la '{herramienta_actual['nombre']} ha cambiado a 'En reparacion'")
def mostrar_reparaciones():
    print("\n Herramientas en estado de reparacion")
    lista_reparaciones = gestion_archivos.cargar_reparaciones()
    lista_f = []
    for elemento in lista_reparaciones:
        if elemento.get("estado") == "En reparacion":
            lista_f.append(elemento)
    if not lista_f:
        print("No hay herramientas en reparacion")
        return
    for herramienta in lista_f:
        print(f"ID: {herramienta['id_herramienta']}")
        print(f"Nombre: {herramienta['nombre']}")
        print(f"Estado: {herramienta['estado']}")
        print(f"Fecha inicio: {herramienta['fecha_inicio_reparacion']}")
        print(f"Fecha estimada finalizacion: {herramienta['fecha_estimada_finalizacion']}")
        print(f"Observaciones: {herramienta['observaciones']}")
def finalizar_reparacion():
    print("\n Al finalizar el tiempo de reparacion")
    id_herramienta = input("Ingrese el ID de la herramienta lista:").strip()
    if id_herramienta not in diccionario_herramientas:
        print("La herramienta no se encuentra registrada en el diccionario")
        return
    herramienta_actual = diccionario_herramientas[id_herramienta]
    if herramienta_actual["estado"] != "En reparacion":
        print(f"La herramienta no se encuentra en reparacion. El esatdo es: {herramienta_actual['estado']}")
        return
    herramienta_actual["estado"] = "Activa"
    lista_reparaciones = gestion_archivos.cargar_reparaciones()
    for elemento in lista_reparaciones:
        if elemento["id_herramienta"] == id_herramienta:
            elemento["estado"] = "Activa"
    gestion_archivos.guardar_reparaciones(lista_reparaciones)
    print(f"Herramienta '{herramienta_actual['nombre']}' actualizada a 'Activa'")