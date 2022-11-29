print("Operaciones matematicas")
num1= 20
num2= 3

suma = num1 + num2 
multiplicacion= num1 * num2
division = num1 / num2
resto = num1 % num2

print("Suma " + str(suma))
print("La multipliacion de  " + str(num1) + " * " + str(num2) + "es " + str(multiplicacion))
print( "Division " + str(division))
print( "Resto " + str(resto))

#Las conversiones solamente entre tipos compatibles
#Redondeamos division

redondeo = int(division)
print("Division redondeada " + str(redondeo))

