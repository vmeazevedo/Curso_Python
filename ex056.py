n = ''
iv = 0
mi = 0
i = 0

for p in range(1,5) :
	print('<======{}°Pessoa !=====>'.format(p))
	np = str(input('nome ?'))
	sx = str(input('sexo [F/M] ?'))
	id = int(input('Idade ?'))
	if sx in 'Mm':
		if id > iv:
			n = np
			iv = id
			i += id
		else :
			i += id
	if sx in 'Ff':
		i += id
		if id <= 20:
			mi += 1
mid = i / 4
print('\033[36 m O homem mais velho e {}, ele tem {} anos !'.format(n, iv))
print('A media de idade dos participantes e',mid)
print('Há {} mulhere(s) com menos de 20 anos'.format(mi))