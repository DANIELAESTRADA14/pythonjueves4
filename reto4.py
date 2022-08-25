contador = 0

contadorNegativo = 0

while(contador<5):
    numero = int(input("Ingrese un numero: "))
    if(numero < 0):
        contadorNegativo += 1
    else:
        contadorNegativo
    contador += 1
print(f"El numero de negativos ingresados fue de {contadorNegativo}")
