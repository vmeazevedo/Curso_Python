times = ('Goias','Bahia','Corinthians','Ceará','Flamengo','Fortaleza','Grêmio','Palmeiras','Santos','São Paulo')

print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*15)
print('Times em ordem alfabética: ', sorted(times))
print('O Flamengo está na', times.index('Flamengo')+1,'ª posição.')


