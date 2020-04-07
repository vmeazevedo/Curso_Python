print('\tBem vindo!\n\n Calculadora Simples - 1.0')
print('As operações que você pode fazer nessa calculadora são:')
print('1. Soma')
print('2. Multiplicação')
print('3. Verificar qual é o maior')
print('4. Incluir novos números')
print('5. Sair')

soma = 1
multiplicar = 2
maior = 3
novos_numeros =4
sair = 5

print('Digite os números que serão calculados: ')
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

operacao = int(input("Digite a operação desejada: "))

print("\n")

while operacao != 0:
    if operacao == 1:
        print("O resultado da soma é:" ,a+b)
        resposta = str(input('Gostaria de realizar outra operação? [S/N]: ')).lower()
        if resposta == 's':
            print('Digite os números que serão calculados: ')
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))
            operacao = int(input("Digite a operação desejada: "))
        else:
            break

        

    if operacao == 2:
        print("O resultado da multiplicação é:" ,a*b)
        resposta = str(input('Gostaria de realizar outra operação? [S/N]: ')).lower()
        if resposta == 's':
            print('Digite os números que serão calculados: ')
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))
            operacao = int(input("Digite a operação desejada: "))
        else:
            break
        

    if operacao == 3:
        if a > b and a != b:
            print('O primeiro valor é maior que o segundo.')
            resposta = str(input('Gostaria de realizar outra operação? [S/N]: ')).lower()
            if resposta == 's':
                print('Digite os números que serão calculados: ')
                a = int(input("Digite o primeiro número: "))
                b = int(input("Digite o segundo número: "))
                operacao = int(input("Digite a operação desejada: "))
            else:
                break

        elif a == b:
            print('Os valores são iguais.')
            resposta = str(input('Gostaria de realizar outra operação? [S/N]: ')).lower()
            if resposta == 's':
                print('Digite os números que serão calculados: ')
                a = int(input("Digite o primeiro número: "))
                b = int(input("Digite o segundo número: "))
                operacao = int(input("Digite a operação desejada: "))
            else:
                break

        else: 
            print('O segundo valor é maior que o primeiro.')
            resposta = str(input('Gostaria de realizar outra operação? [S/N]: ')).lower()
            if resposta == 's':
                print('Digite os números que serão calculados: ')
                a = int(input("Digite o primeiro número: "))
                b = int(input("Digite o segundo número: "))
                operacao = int(input("Digite a operação desejada: "))
            else:
                break
        

    if operacao == 4:
        print('Digite os números que serão calculados: ')
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        operacao = int(input("Digite a operação desejada: "))

    if operacao == 5:
        print('Até logo.')
        break