print("Ejemplo Bucles")

print("For")
print("-----------------")
#Normalmente las variables contador de los bucles se suelen empresar con una sola letra, ex: i,j,x,z
for i in range(5):
    print("Valor de i " + str(i))
    
print("-----------------")
    
for i in range(1,6):
    print("Valor de i " + str(i))

print("While")
#Necesitamos una variable para la condicion del bucle
contador = 0

while(contador <=5 ):
    print("Contador " + str(contador))
    #Debemos hacer algo para salir del bucle, en este ejemplo incrementaremos el contrador
    contador += 1
    #Tambien se utiliza la instruccion contador = contador + 1

print("Fin del programa")     