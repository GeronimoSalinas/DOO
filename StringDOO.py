schema = "Nombre,Apelldo,Edad"
row = "Geronimo,Salinas,18"

class StrDoo(object):
    def __init__(self, schemaDOO,separator=","):
        self.schema =schemaDOO.split(separator)
        self.separator = separator
    def convert (self,row) :
        temp = row.split(self.separator)
        if len (temp) == len(self.schema):
            i = 0
            dic = {} 
            while i < len(temp):
                key = self.schema[i]
                value = temp[i]
                dic[key] = value 
                i = i + 1
            return dic
        
a = StrDoo(schema)
b = a.convert(row)
print (b)

                 