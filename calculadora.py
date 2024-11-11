def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def muntiplicacao(x, y):
    return round(x * y, 2)

def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return round(x / y, 2)

def calculadora():
    print('Selecione a operação:')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')

    while True:
        escolha = input("Digite o número da operação(1/ 2/ 3/ 4) ou 'sair' para finalizar: ")

        if escolha == 'sair':
            print('Calculadora finalizada.')
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input('Digite o primeiro número: '))
                num2 = float(input('Digite o segundo número: '))
            except ValueError:
                print('Erro! Digite números válidos.')
                continue

            if escolha == '1':
                print('Resultado: ', soma(num1, num2))
            elif escolha == '2':
                print('Resultado: ', subtracao(num1, num2))
            elif escolha =='3':
                print('Resultado: ', muntiplicacao(num1, num2))
            elif escolha == '4':
                print('Resultado: ', divisao(num1, num2))
        else:
            print('Opção inválida! Tente novamente.')

if __name__ == '__main__':
    calculadora()