try:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    if num2 == 0:
        print('Erro: Divisão por zero não é permitida.') # Adiciona uma condição para uma possível divisão por 0
    else:
        soma = num1 + num2
        sub = num1 - num2
        multi = num1 * num2
        divi = num1 / num2
        resto = num1 % num2
        potencia = num1 ** num2

        print(f'A soma entre {num1} e {num2} é igual a {soma}.')
        print(f'A subtração entre {num1} e {num2} é igual a {sub}.')
        print(f'A multiplicação entre {num1} e {num2} é igual a {multi}.')
        print(f'A divisão entre {num1} e {num2} é igual a {divi:.2f}.')  # Apenas exibe a divisão com 2 casas decimais
        print(f'O resto da divisão entre {num1} e {num2} é igual a {resto}.')
        print(f'{num1} elevado a {num2} é igual a {potencia}.')

except ValueError:
    print('Erro: Por favor, digite números válidos.')