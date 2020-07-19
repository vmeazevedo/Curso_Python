idade = int(input('Digite o ano do seu nascimento: '))
inf_id = 2020 - idade

print('Sua categoria é: ')

if inf_id <= 9:
    print('MIRIM')
elif inf_id > 9 and inf_id <= 14:
    print('INFANTIL')
elif inf_id > 14 and inf_id <=19:
    print('JUNIOR')
elif inf_id == 20:
    print('SÊNIOR')
elif inf_id > 20:
    print('MASTER')
