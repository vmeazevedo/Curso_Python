lista = []

while True:
    entrada = int(input('Digite um valor: '))
    if entrada in lista:
        print('O valor duplicado! Não vou adicionar')
        resposta = str(input('Quer continuar? [S/N]: '))
        if resposta == 's':
            continue
        else:
            break
    else:
        print('Valor adicionado com sucesso.')
        lista.append(entrada)
        resposta = str(input('Quer continuar? [S/N]: '))
        if resposta == 's':
            continue
        else:
            break
print('-='*25)
lista.sort()
print(F'Você digitou os valores {lista}')
