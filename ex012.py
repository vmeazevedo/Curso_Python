produto = float(input('Digite o valor do produto: '))
desconto = produto * (5/100)
novo_val = produto - desconto

print('Seu novo valor com cinco porcento de desconto é de {:.2f} reais.'.format(novo_val))

