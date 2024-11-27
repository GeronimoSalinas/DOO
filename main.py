            else:
                print ("Coleccion"(nombre_coleccion)"no encontrada: ") 
        elif opcion == "4":
            nombre_coleccion = int(input ("Ingrese Nombre de Coleccion: "))
            doc_id = input ("Ingrese ID del documento a eliminar : ")
            coleccion = db.get_collection(nombre_coleccion)
            if coleccion: 
                coleccion.delete_document(doc_id)
        elif opcion == "5":
            nombre_coleccion = int(input ("Ingrese Nombre de Coleccion: "))
            coleccion = db.get_collection(nombre_coleccion)
            if coleccion:
                documentos = coleccion.list_documents()
                if documentos:
                    print("\n---Lista de Documentos---")
                    for doc in documentos:
                        print(doc)
                        print("------------")
                else :
                    print("No hay documentos en la colección")
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no Valida. Vuelva a intentarlo nuevamente")
if __name__ == " __main__":
    main()