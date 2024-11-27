            from bdb import bdd
import json 

def mostrar_menu():
    print("\n--- Base de Datos Documental ---")
    print("1. Crear Colección")   
    print("2. Importar CSV a colección")  
    print("3. Consultar documento de colección") 
    print("4. Eliminar documento de colección")  
    print("5. Listar todos los documentos en colección")
    print("6. Salir ")
    return input ("Seleccione una opción:   ")

def main():
    db=bdd("Mi BDD")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre_coleccion = input ("Ingrese Nombre de Coleccion: ")
            db.create_collection(nombre_coleccion)
            print("Coleccion" (nombre_coleccion)"creada.")
            elif opcion == "2":
            nombre_coleccion = input ("Ingrese Nombre de Coleccion: ")
            collection = db.get_collection(nombre_coleccion)
            ruta_CSV = input("Ingrese Ruta del archivo CSV: ")
            collection.import_collection(ruta_CSV)

        elif opcion == "3":
            nombre_coleccion = int(input ("Ingrese Nombre de Coleccion: "))
            doc_id = input ("Ingrese ID del documento: ")
            coleccion = db.get_collection(nombre_coleccion)
            if coleccion:
                documento = coleccion.get_document(doc_id)
                if documento:
                    print("Documento encontrado")
                    print(documento)        
                else:
                    print("Documento no encontrado.")
                

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