'''
numero = 5
while(numero < 10):
    print("Estoy dentro del ciclo")
    numero += 1
else:
    print("Adios")
    
print("Estoy por fuera del ciclo") '''


opcion = 1
print('****Menu****')
print("1. SUMAR")
print("2. RESTAR")
print("0. SALIR")

while(opcion != 0):
    opcion=int(input("Digite una opción: "))
    if(opcion == 1):
        print("sumando...")
    elif(opcion == 2):
        print("restando...")
    elif(opcion == 0):
        break
    else:
        print("número no válido...")
