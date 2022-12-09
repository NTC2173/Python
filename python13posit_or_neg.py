
respuesta = "s"

while(respuesta == "s"):
    #Iremos pidiendo numeros al usuario
    print("Introduzca numero: ")
    numero = int(input())
    if(numero > 0):
        print("POSITIVO")
    elif(numero == 0):
        print("ZERO")
    else:
        print("NEGATIVO")
        
    print("¿Desea continuar? (s/n)")
    respuesta = input()
    
print("Fin de programa")