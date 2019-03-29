# Rosalía Serrano Herrera
#

def dividir(dividendo, divisor):
    cociente = 0
    residuo = dividendo
    while residuo >= divisor:
        residuo = residuo - divisor
        cociente += 1

    print(dividendo, "/", divisor, "=", cociente, ", sobra", residuo)


def probarDivisiones():
    dividir(15, 6)
    dividir(4, 6)
    dividir(500, 21)
    dividir(151, 32)
    dividir(1024, 8)


def encontrarMayor():
    print("Teclea una serie de números para encontrar el mayor.")
    numero = int(input("Teclea un numero [-1 para salir]: "))
    mayor = -1
    while numero != -1:
        if numero > mayor:
            mayor = numero
        else:
            pass
        numero = int(input("Teclea un numero [-1 para salir]: "))
    if numero == -1 and numero >= mayor:
        print("No hay un valor mayor")
    else:
        print("El número mayor es: ", mayor)

def main():
    print("Misión 07. Ciclos while \nAutor: Rosalía Serrano Herrera \nMatrícula: A01374781 \n1. Calcular divisiones \n2. Encontrar el mayor \n3. Salir")
    opcion = int(input("Teclea tu opción: "))
    while opcion != 3:
        if opcion == 1:
            dividendo = int(input("Teclea el dividendo: "))
            divisor = int(input("Teclea el divisor: "))
            dividir(dividendo, divisor)
        elif opcion == 2:
            encontrarMayor()
        else:
            print("ERROR, teclea 1, 2 o 3")
        print("Misión 07. Ciclos while \nAutor: Rosalía Serrano Herrera \nMatrícula: A01374781 \n1. Calcular divisiones \n2. Encontrar el mayor \n3. Salir")
        opcion = int(input("Teclea tu opción: "))


    if opcion == 3:
        print("Gracias por usar este programa, regresa pronto.")

main()
