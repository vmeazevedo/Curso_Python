ano = 2020
jovem = int(input('Digite o ano do seu nascimento: '))
calc = ano - jovem #Ca´lcula a idade do jovem
min = 18
hora = min - calc #Calcula quantos falta para o alistamento
hora2 = calc - min #Calcula quantos anos faz que a pessoa devia ser alistado.

if calc < 18:
    print('Ainda não é o momento de se alistar')
    print('Ainda falta {} anos para você se alistar.'.format(hora))
elif calc == 18:
    print('Está na hora de se alistar!')
elif calc > 18:
    print('Ja passou da hora de você se alistar')
    print('Você esta atrasado no alistamento faz {} anos.'.format(hora2))
