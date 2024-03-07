grado_cambiar = int(input("ingrese la cantidad de grados celsius para comvertir"))
celsius_fahrenheit = (9/5 * grado_cambiar) + 32
grado_cambiar2 = int(input("ingrese la cantidad de grados fahrenheit para convertir: "))
fahrenheit_celsius = (grado_cambiar2 -32)* 5/9

while True:
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    print("3. Finalizar")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = celsius_fahrenheit
        print("La temperatura en grados Fahrenheit es:", fahrenheit)
    elif opcion == "2":
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        celsius = fahrenheit_celsius
        print("La temperatura en grados Celsius es:", celsius)
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")