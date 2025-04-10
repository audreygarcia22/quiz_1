def menu_interavtivo():
    nombres = ["Carlos","Sofhia","Alberto","Monica","Luis"]

    while True:
        print ("\n---Menú Interactivo")
        print ("1. memsaje")
        print ("2. Lista nombres")
        print ("3. Salir del programa")

        opcion = input ("Por favor,ingresa una opcion (1,2,3):")

        if opcion == "1" or opcion.lower () == "Mensaje":
            print("\n🌟 ¡Sigue adelante, cada paso te acerca más a tu meta! 💪")
        elif opcion == "2" or opcion.lower() == "nombres":
            print ("-",nombre)
        elif opcion == "3" or opcion.lower() == "Salir":
            print("\n 👋 Gracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print("\n⚠️ Opción no válida. Intenta nuevamente.")
        
menu_interavtivo()
 