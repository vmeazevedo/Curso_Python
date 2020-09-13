#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

import random
import time

t = 3

presentes = ['Maquiagem bem cara e rezar!', 'Jóia e rezar.', 'Perfume caro e rezar.', 'Sapato que ela ama e rezar.', 'Bolsa nova e rezar.']
doces = ['Chocolate e pede desculpas.','Mousse e pede desculpas.','Bolo e pede desculpas.','Torta e pede desculpas.','Pudim e pede desculpas.','Brownie e pede desculpas.','Sorvete e pede desculpas.']
atrações = ['Jantar-Fora.', 'Pizzaria.', 'Barzinho.', 'Parque.', 'Shopping.', 'Cinema.', 'Cafeteria.']
romantico = ['Manda uma mensagem no Whats dela.', 'Posta uma foto de vocês dois juntos com uma legenda romântica.', 'Ligar pra ela e diz que ta com saudade.', 'Liga pra ela e diz que a ama.']
escolha = ['presentes','doces','atrações','romantico']

print('-='*45)
print('                           ALGORITMO DO MARIDO "PERFEITO" v1.0')
print('-='*45)
print('A gente sabe que tu fez merda, e estamos aqui para lhe ajudar!\n')
print('Primeiro de tudo, qual foi o nível de cagada que você fez dessa vez?\n')
print('1 - HARDCORE')
print('2 - PESADA')
print('3 - MODERADA')
print('4 - LEVE \n')

escolha = int(input('Digite o número da sua escolha que vamos pensar como você pode resolver ela: '))

if escolha == 1:
    print('Você fez uma merda HARDCORE...')
    time.sleep(t)
    print('Você ta de parabêns em! Pensando em como resolver a SUA cagada...\n')
    time.sleep(t)
    print(f'A única saída para amenizar essa merda é comprar para ela um(a):',random.choice(presentes))
    print()
    input('Pressione qualquer tecla para fechar...')
if escolha == 2:
    print('Você fez uma merda PESADA...')
    time.sleep(t)
    print('Vai ser difícil, mas tem solução!\n')
    time.sleep(t)
    print(f'Rapaiz a melhor opção é:',random.choice(doces))
    print()
    input('Pressione qualquer tecla para fechar...')
if escolha == 3:
    print('Você fez uma merda MODERADA...')
    time.sleep(t)
    print('Pera ai rapidão, to pensando, mas tem solução...\n')
    time.sleep(t)
    print(f'Olha, vai com ela fazer algo do tipo:',random.choice(atrações))
    print()
    input('Pressione qualquer tecla para fechar...')
if escolha == 4:
    print('Você fez uma merda LEVE...')
    time.sleep(t)
    print('Essa é molezinha...\n')
    time.sleep(t)
    print(f'Para tudo e faz isso:',random.choice(romantico))
    print()
    input('Pressione qualquer tecla para fechar...')
