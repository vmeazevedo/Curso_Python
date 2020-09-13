#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

dic = {'vermelho':'red','azul':'blue','verde':'green','preto':'black'}
cor = input('Bem vindo,escolha a cor que deseja traduzir: ').lower()
traducao = dic.get(cor,'Esta cor não consta no meu dicionário')
print(traducao) 

