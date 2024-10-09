a = 10
b = 4

try :
    c = a / b 
    print (c)
except :
    print ("No es posible dividir por :  ", b)


try: 
    numero = int(input("Ingrese un numero:  "))
    resultado = 10 / numero

except ZeroDivisionError:
    print ("error: no se puede dividir por cero")

except ValueError:
    print ("error: solo numeros enteros.")

else :
    print("Resultado:" , {resultado})

finally :
    print("Finalizando...")
