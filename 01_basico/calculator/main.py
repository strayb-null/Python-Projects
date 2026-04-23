operador = input("Escolha uma operação (* / + -): ")
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

resultado = None

if operador == "*":
    resultado = numero_1 * numero_2

elif operador == "/":
    if numero_2 != 0:
        resultado = numero_1 / numero_2
    else: 
        print("Não é possivel fazer dividir por 0")
        
elif operador == "+":
    resultado = numero_1 + numero_2

elif operador == "-":
    resultado = numero_1 - numero_2

else:
    raise ValueError("Operação Invalida")

if resultado is not None:
    print(f"O resultado é: {resultado:g}")
