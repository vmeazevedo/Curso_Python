#Contador de vezes somando os valores.
vezes = 0
soma = 0
num = 0

while True:
    num = int(input('Digite um valor (use o 999 para parar): '))
    if num == 999:
        break
    soma = soma + num
    vezes = vezes +1
print(f'A soma dos {vezes} valores foi {soma}')


