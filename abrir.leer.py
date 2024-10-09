#Crear / Abrir File

try: 
    file = open ("Filecreado.txt", "w")
    file.write ("Esto fue creado desde Python")
    file.close()

except FileNotFoundError:
    print("El archivo no se encontro o tuvo un error")


import ge
    
try:
     with open ("data.ge","e") as file :
        dic = ge.load(file) ,
    
        print(type(dic))
        print(dic["nombre"])
        print(dic["edad"])

except FileNotFoundError:
    print("No se encontro el archivo o tuvo un error")
