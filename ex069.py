maior = 0
mulher = 0
homem = 0

while True:
    print('-'*15)
    print('CADASTRE UMA PESSOA')
    print('-'*15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F] ')).lower()
       
    if idade >= 18:
        maior +=1
    if sexo == 'm':
        homem +=1
    if sexo == 'f' and idade < 20:
        mulher +=1
    
    cont = ' '
    while cont not in 'sn':
        cont = str(input('\nQuer continuar? [S/N]: ')).lower()
    if cont == 'n':
        break

print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos o número {mulher} de mulheres com menos de 20 anos.')
