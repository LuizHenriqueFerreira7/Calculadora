numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Escolha a operação desejada: ")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite o número da operação: ")

if operacao == '1':
    resultado = numero1 + numero2
    print(f"O resultado da adição é: {resultado}")
elif operacao == '2':
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == '3':
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == '4':
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
