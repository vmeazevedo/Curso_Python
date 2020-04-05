not1 = float(input('Digite a sua nota 1: '))
not2 = float(input('Digite a sua nota 2: '))
media = (not1+not2) /2

if media < 5:
    print('Reprovado!')
elif media == 5 or media <= 6.9:
    print('Recuperação!') 
elif media >= 7:
    print('Aprovado!')

