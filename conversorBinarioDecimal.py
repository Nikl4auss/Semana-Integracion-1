def mostrar_menu():
    print("Conversor Decimal Binario")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Salir")

def obtener_opcion():
    #validación de la opción elegida
    while True:
        opcion = input("Seleccione una opción (1, 2 o 3): ")
        if opcion in {"1", "2", "3"}:
            return opcion
        print("Opción inválida.")

def decimal_a_binario():
    #se valida que la entrada sea un número entero positivo. Caso contrario se pide que se vuelva a ingresar
    while True:
        numero = input("Ingrese un número (entero positivo): ")
        if numero.isdigit() and int(numero) > 0:
            break
        print("Error: entrada inválida. Ingrese un número positivo.")

    #convierto el input a numerico
    numero = int(numero)
    binario = ""
    
    #mientras el número sea mayor a 0, se divide entre 2 y se obtiene el residuo
    #el residuo se concatena para ir armando el binario
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        #se divide el número entre 2 y se descarta la parte decimal
        numero = numero // 2

    print("Binario:", binario)

def binario_a_decimal():
    #se valida que la entrada sea un número binario. Caso contrario se pide que se vuelva a ingresar
    while True:
        valido = True
        binario = input("Ingrese un número binario (solo 0 y 1): ")
        for c in binario:
            if c not in '01':
                print("Error: entrada inválida. Ingrese solo 0 y 1.")
                valido = False
                break
        if valido:
            break

    decimal = 0

    #recorro el número binario de derecha a izquierda y lo elevo a la potencia de su posición
    for i in range(len(binario), 0,-1 ):
        if binario[len(binario) - i] == '1':
            decimal += 2 ** (i-1)   

    print("Decimal:", decimal)

def main():
    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        if opcion == "1":
            decimal_a_binario()
        elif opcion == "2":
            binario_a_decimal()
        elif opcion == "3":
            print("¡Adiós!")
            break

# Ejecutar programa
main()
