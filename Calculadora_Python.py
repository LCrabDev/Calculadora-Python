# Esse código é uma versão de uma calculadora em Python

""" Irei criar uma função com o nome "calculadora" que recebe como parâmetro (valor1, valor2)"""

print('__CALCULADORA PYTHON__')
print(22 * '-')
def calculadora(valor1, valor2):

    # O usuário irá escolher os numeros.
    valor1 = int(input('Digite um valor: '))
    valor2 = int(input('Digite outro valor: '))
    print('Os operadores matematicos sao: (Soma (+), Subtracao (-), Multiplicacao (X), Divisao (/)')

    # Após a escolha, o usuário irá escolher o operador matemático.
    
    operador = input('Digite um operador matemático: ')
    soma = valor1 + valor2
    subtracao = valor1 - valor2
    multiplicacao = valor1 * valor2
    divisao = valor1 / valor2

    #Para tratar as escolhas do usuário, criei uma lista com os operadores matemáticos.

    operadores_matematicos = ['+', '-', 'x', 'X', '/']

    # Agora o código irá tratar as informações escolhidas pelo usuário.

    ''' O código irá interpretar (Soma como ' + '), (Subtração como ' - ')
    (Multiplicação como ' x ' ou ' X ') e (Divisão como ' / ').'''

    if operador == '+':
        print('O resultado da soma foi: {}'.format(soma))
    elif operador == '-':
        print('O resultado da subtracao foi: {}'.format(subtracao))
    elif operador == 'x' or operador == 'X':
        print('O resultado da multiplicacao foi: {}'.format(multiplicacao))
    elif operador == '/':
        print('O resultado da divisao foi: {}'.format(divisao))
    # Caso a escolha do usuário seja diferente dos operadores matematicos, ele irá tratar o 'else':
    else:
        if operador != operadores_matematicos:
            print('Por favor, digite somente operadores matematicos de Soma, Subtracao, Multiplicacao ou Divisao')

# A estrutura da função foi finalizada, basta executar o código como "Run Python File".

calculadora('valor1', 'valor2')
