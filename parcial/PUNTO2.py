comprobar = True
while comprobar == True:
    numero = int(input("ingresa un numero entero positivo :"))
    
    if numero > 0:
        i = 1+1
        while i < 11:
            print (numero, "X", i, "=", numero*i)
            comprobar = False
            
        else:
            print("el numero que ingreso no es correcto, intentalo otra vez")