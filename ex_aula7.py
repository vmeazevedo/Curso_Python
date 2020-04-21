'''
EXERCICIO: Escreve uma função que recebe um objeto de coleção e retorna o valor do maior
numero dentro dessa coleção. Faça outra função que retorna o menor numero dessa coleção.
'''
lista = []

for i in range(5):
    n = int(input('Digite um número: '))
    lista.append(n)

def maior_num():
    print(max(lista))

def menor_num():
    print(min(lista))

print(f'O maior numero da lista é: {maior_num()} ') 
print(f'O menor numero da lista é: {menor_num()} ') 


