import random

vezes = 0

print('-='*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*15)

while True:
    usuario = str(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I]: ')).lower()
    computador = random.randint(1,10)
    soma = int(usuario) + int(computador)

    if escolha == 'p' and soma %2 == 0:
        print(f'Você jogou {usuario} e o computador jogou {computador}. Total deu {soma}. DEU PAR!')
        print('Voce venceu! Vamos jogar novamente...\n')
        vezes = vezes+1

    elif escolha == 'i' and soma %2 != 0:
        print(f'Você jogou {usuario} e o computador jogou {computador}. Total deu {soma}. DEU ÍMPAR!')
        print('Você venceu!Vamos jogar novamente...\n')
        vezes = vezes+1
        
    elif escolha == 'p' and soma %2 != 0:
        print(f'Você jogou {usuario} e o computador jogou {computador}. Total deu {soma}. DEU ÍMPAR!')
        print('Você perdeu!\n')
        print(f'A quantidade de vezes que você ganhou do computador foi {vezes}.')
        break     
    elif escolha == 'i' and soma %2 == 0:
        print(f'Você jogou {usuario} e o computador jogou {computador}. Total deu {soma}. DEU PAR!')
        print('Você perdeu!\n')
        print(f'A quantidade de vezes que você ganhou do computador foi {vezes}.')
        break    
