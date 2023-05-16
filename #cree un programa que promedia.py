#cree un programa que pida numeros al usuario y muestre el promedio actual.si el usuario ingresa 0. se detiene el ingreso de numeros.


prom= 0

suma = 0 

cant= 0

while ( True):
    
    num= float(input("ingrese un numero: "))

    if (num== 0):
        break
    if (num<0):
        continue
    suma += num #agregamos ala suma total
    cant += 1 #agregar 1 al contador
    prom= suma / cant 
    print("el promedio es", prom)