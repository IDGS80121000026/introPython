num1 = 20
num2 = 4

print("La suma es: ", (num1+num2))
print("La resta es: ", (num1-num2))
print("La multiplicacion es: ", (num1*num2))
print("La division es: ", (num1/num2))
print("La dicision exacta es: ", (num1//num2))
print("La potencia es: ", (num1**num2))

#Concatenacion en python

texto1 = "Hola"
texto2 = "Mundo"
textoFinal = texto1 + " " + texto2
print(textoFinal)

print("El saludo es: %s %s" %(texto1, texto2))   #El porcetanje es para sustituir los valores en cada variable 

saludoFinal = "Saludo {} {}".format(texto1,texto2)
print(saludoFinal)

saludoFinal = "Saludo 2: {y} {x}".format(x=texto1,y=texto2)
print(saludoFinal)