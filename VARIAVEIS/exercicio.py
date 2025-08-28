# Peça dois números do usuário, podendo ser inteiro ou fluante. Depois, mostre:
'''
Soma
Divisão
Subtração
Multiplicação
Resto da divisão?

'''
nome = str(input("Qual é o seu nome?"))
dadosUsuario = (f"Olá {nome}, seja bem vindo!")
print(dadosUsuario)

numero1 = int(input("Poderia me dizer o primeiro número?"))
numero2 = int(input("Agora você poderia me dizer o segundo número?"))

operacoesSugeridas = (f"A soma é igual a {numero1 + numero2}, a divisão é igual {numero1/numero2}, a subtração é igual a {numero1-numero2}, a multiplicação é igual a {numero1*numero2} e o resto da divisão é {numero1 % numero2}")
print(operacoesSugeridas)






