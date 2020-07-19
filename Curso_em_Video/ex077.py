tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'estudar')

for palavras in tupla:
    print(f'Na palavra {palavras} temos', end=' ')
    for letras in palavras:
        if letras in 'aeiou':
            print(letras, end= ' ')
    print()