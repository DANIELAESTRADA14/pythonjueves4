numero = 1
suma = 0
while(numero >= 0):
    numero=int(input("Digite un numero: "))
    if(numero < 0):
        break
    suma += numero
    print(suma)