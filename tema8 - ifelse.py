print("Suma de numeros")
num1 = int(input("Dame n1"))
num2 = int(input("Dame n2"))

if num1 > num2 : 
    print("El {} es mayor que el {}".format(num1,num2))
else:
    print("El {} es mayor que el {}".format(num2,num1))
    
print("------------ Pedir una edad  ---------------")
edad = int(input("Ingresa tu edad:"))

if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
