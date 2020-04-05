a = float(input('Digite o valora da primeira reta: '))
b = float(input('Digite o valora da segunda reta: '))
c = float(input('Digite o valora da terceira reta: '))

if a < b+c and b < a+c and c < a+b:
    print('As retas podem formar um triângulo.')
    if a == b and a == c and b == c:
        print('Esse triângulo é um Equilátero.')
    elif a == b or c == a:
        print('Esse triângulo é um Isósceles.')
    elif a != b and a != c and b != c:
        print('Esse triângulo é um Escaleno.')
else:
    print('As retas não podem formar um triangulo.')

    