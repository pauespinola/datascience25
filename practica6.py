n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))
n4 = int(input("Ingrese el cuarto número: "))

lista = [n1,n2,n3,n4]

option = ""

while option != "4":
    print("** M E N Ú **")
    print("1. Suma de los números \n" \
    "2. Promedio de los números \n" \
    "3. Mostrar el mayor y el menos \n" \
    "4. Salir")
    option = int(input("Ingrese el n° menú: "))
    if option == 1:
        print(f"la suma es: {sum(lista)}")
    elif option == 2:
        print(f"el promedio es: {sum(lista)/len(lista)}")
    elif option == 3:
        print(f"El mayor es: {max(lista)} - El menor es: {min(lista)} ")
    elif option == 4:
        print("salir")
        exit()
    else:
        print("Elige un número del menú ")