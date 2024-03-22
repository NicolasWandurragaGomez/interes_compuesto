import math

#input 

C= int(input("Digite la capital: "))

#processing

n = 0
d = C * 2

while (C <= d):
    C= 1.05 * C
    n= n + 1

#output

print("Capital inicial: " + str(d / 2))
print("El numero de meses en el que su capital se duplicaria es: " + str(n)) 
print("El total de su capitan seria: " + str(C))
