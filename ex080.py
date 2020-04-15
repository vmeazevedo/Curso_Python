# num.insert(2,0)         #Na posição 2 eu insiro o digito 0
lista = []

for c in range(0,5):
    entrada = int(input('Digite um valor: '))
    if c == 0 or entrada > lista[-1]:           #Se o valor de C == 0 ou seja é o primeiro
        lista.append(entrada)                   #Verificar se é maior que o ultimo elemento
        print('Adicionado no final da lista...')
    else:
        posicao = 0
        while posicao < len(lista):
            if entrada <= lista[posicao]:
                lista.insert(posicao, entrada)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')
