import os 

sair = "Sair"
numero01 = input("Digite o primeiro numero: ")
numero02 = input("Digite o segundo valor: ")
operador = input("Digite o operador (+-/*) ")

numero01_float = 0
numero02_float = 0

numero01_float = float(numero01)
numero02_float = float(numero02)

if operador == "+":
    print(f"{numero01_float} + {numero02_float} = ", numero01_float + numero02_float)
elif operador == "-":
    print(f"{numero01_float} - {numero02_float} = ", numero01_float - numero02_float)
elif operador == "*":
    print(f"{numero01_float} * {numero02_float} = ", numero01_float * numero02_float)
elif operador == "/":
    print(f"{numero01_float} / {numero02_float} = ", numero01_float / numero02_float)

