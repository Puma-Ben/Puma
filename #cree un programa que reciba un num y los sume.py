#cree un programa que reciba un numero positivo y entrega la suma de todos sus digitos. EJ: 123=1+2+3 = 6.

num=input("ingrese un numero:\n")
suma=0
for l in num:
    suma += int (l)

print("la suma es", suma)


