def soma(numero1, numero2):
    print(f'somando {numero1} + {numero2}')
    return numero1 + numero2

def subtracao(numero1, numero2):
    print(f'subtraindo {numero1} - {numero2}')
    return numero1 - numero2

def divisao(numero1, numero2):
    print(f'dividindo {numero1} / {numero2}')
    return numero1 / numero2

def multiplicacao(numero1, numero2):
    print(f'multiplicando {numero1} * {numero2}')
    return numero1 * numero2           


if __name__ == '__main__':
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))

    operador = input('Digite um operador válido: ')

    resultado = 0

    if operador == '+':
        resultado = soma(numero1, numero2)
    elif operador == '-':
        resultado = subtracao(numero1, numero2)     
    elif operador == '/':
        resultado = divisao(numero1, numero2)    
    elif operador == '*':
        resultado = multiplicacao(numero1, numero2)
    else: 
        print('Operador incorreto')        


    if resultado != None:
        print(f'O resultado da operação é: {resultado}')