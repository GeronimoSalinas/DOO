#%% 
from STR import Strdoc

class Documento(): 
    def __init__(self, id, contenido=None): 
        self.id = id 
        self.contenido = contenido if contenido is not None else {} 
 
    def obtener_valor(self, clave):  # Renombrado de obtn_valor
        return self.contenido.get(clave, None) 
     
    def actualizar_valor(self, clave, valor):  # Renombrado de edit_valor
        self.contenido[clave] = valor 
 
    def __str__(self): 
        return f"Documento(id={self.id}, contenido={self.contenido})" 
 
class Coleccion(): 
    def __init__(self, nombre): 
        self.nombre = nombre 
        self.documentos = {} 
        self.id = 0  # Se inicia en 0 para que sea autoincremental
     
    def agregar_documento(self, documento):  # Renombrado de add_doc
        self.documentos[documento.id] = documento 
 
    def eliminar_documento(self, id_documento):  # Renombrado de drop
        if id_documento in self.documentos: 
            del self.documentos[id_documento] 
 
    def buscar_documento(self, id_documento):  # Renombrado de search
        return self.documentos.get(id_documento, None) 
     
    def importar_coleccion(self, ruta):  # Renombrado de import_colleccion
        with open(ruta, "rt") as file: 
            schema = file.readline().replace("\n", "") 
            csv = Str2Doc(schema) 
             
            for line in file: 
                nuevo = Documento(self.id, csv.convert(line.strip())) 
                self.agregar_documento(nuevo) 
                self.id += 1 
     
    def __str__(self): 
        return f"Coleccion {self.nombre} con {len(self.documentos)} documentos." 
 
class BDD(): 
    def __init__(self, nombre): 
        self.nombre = nombre 
        self.colecciones = {} 
 
    def crear_coleccion(self, nombre_coleccion):  # Renombrado de create_collection
        if nombre_coleccion not in self.colecciones: 
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion) 
     
    def eliminar_coleccion(self, nombre_coleccion):  # Renombrado de delete_collection
        if nombre_coleccion in self.colecciones: 
            del self.colecciones[nombre_coleccion] 
     
    def obtener_coleccion(self, nombre_coleccion):  # Renombrado de get_collection
        return self.colecciones.get(nombre_coleccion, None) 
     
    def __str__(self): 
        return f"Base de datos documental con {len(self.colecciones)} colecciones." 
