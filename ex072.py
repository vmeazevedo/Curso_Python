num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')

while True:
    entrada = int(input('Digite um número entre 0 e 20: '))
    if entrada < 0:
        print(f'O número {entrada} não está entre 0 e 20. Tente novamente. Digite um número entre 0 e 20: ')
    if entrada > 20:
        print(f'O número {entrada} não está entre 0 e 20. Tente novamente. Digite um número entre 0 e 20: ')
    if entrada >= 0 and entrada <=20:
        print(f'Você digitou o número {num[entrada]}')
        break