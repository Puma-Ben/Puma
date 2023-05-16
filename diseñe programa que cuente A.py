#diseñe un programa que reciba un texto y cuente cuantas letras "a" o "A" hay en el texto.

texto= input("inserte texto aqui:\n")

counta= 0
countA= 0
 
for o in texto:
    if o == "a":
        counta=1
    if o == "A":
        countA=1
print(f" hay {counta} a y {countA} A  en el texto")

        
    


