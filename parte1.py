def programa_beta_nike():
    inventario_nike = {
        "productoA": {"stock": 100, "precio": 59.999},
        "productoB": {"stock": 50, "precio": 45.500},
        "productoC": {"stock": 200, "precio": 29.950},
        "tallaS-rojo": {"stock": 30, "precio": 45.000},
        "tallaM-azul": {"stock": 75, "precio": 48.00},
    }

    print("\nBienvenido al Programa BETA de Nike - Gestión de Datos Dinámicos")
    print("Diccionario inicial:", inventario_nike)

    # Modificación de un valor
    clave_modificar = input("\nIngrese la clave del elemento que desea modificar: ")

    if clave_modificar in inventario_nike:
        nuevo_valor_str = input(f"Ingrese el nuevo valor para la clave '{clave_modificar}': ")
        try:
            nuevo_valor = eval(nuevo_valor_str)
            inventario_nike[clave_modificar] = nuevo_valor
            print("\nDiccionario actualizado después de la modificación:")
            print(inventario_nike)
        except (NameError, SyntaxError):
            print("Error: El valor ingresado no es válido. El diccionario no se modificó.")
    else:
        print(f"Error: La clave '{clave_modificar}' no existe en el diccionario.")

    # Eliminación de un elemento
    clave_eliminar = input("\nIngrese la clave del elemento que desea eliminar: ")

    if clave_eliminar in inventario_nike:
        del inventario_nike[clave_eliminar]
        print(f"La clave '{clave_eliminar}' ha sido eliminada.")
        print("Diccionario actualizado después de la eliminación:")
        print(inventario_nike)
    else:
        print(f"Error: La clave '{clave_eliminar}' no se encontró en el diccionario.")
        print("El diccionario permanece sin cambios:")
        print(inventario_nike)

    print("\nFin del Programa BETA de Nike.")


programa_beta_nike()
