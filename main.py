import gestion
def menu():
    gestion.cargar_inventario_inicial()
    while True:
        print("---SISTEMA DE CONTROL DE REPARACIONES---")
        print("1. Registrar nueva herramienta")
        print("2. Ejecutar: registrar_reparacion")
        print("3. Mostrar herramientas en estado de reparacion")
        print("4. Finalizar reparacion (La herramienta vuelve a estado activa)")
        print("5. Salir")
        opcion = input("Seleccione una opcion segun la accion que desea realizar (1-5)")
        if opcion == "1":
            gestion.registrar_herramienta()
        elif opcion == "2":
            gestion.registrar_reparacion()
        elif opcion == "3":
            gestion.mostrar_reparaciones()
        elif opcion == "4":
            gestion.finalizar_reparacion()
        elif opcion == "5":
            print("Has finalizado la ejecución del programa.")
            break
        else:
            print("Error: La opción ingresada es invalida ")
menu()
