#Criando listas númericas
#Usando a função range()
for value in range(1,5):
    print(value)

#Usando range() para criar uma lista de números
numbers = list(range(1,6))
print(numbers)

#Somando valores de uma lista de 2 em 2
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value **2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#Estatistica simples com uma lista de números
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

'''
4.3 - Contando até vinte: Use um laço for para exibir os números de 1 a 20, incluindo-os.'''
print('4.3 - Contando até vinte')
for n in range(1,21):
    print(n)

''' 
4.4 - Um milhão: Crie uma lista de números de um a um milhão e, então use um laço for para exibir
os números. '''
# milhão = list(range(1,1000001))
# for n in milhão:
#     print(n)

'''
4.5 - Somando um milhão: Crie uma lista de números de um a um milhão em em seguida, use min() e max() para garantir
que sua lista realmente começa com um e termina com um milhão. Além disso, utilize a função sum() par aver a rapidez com que Python é capaz de somar um milhão de números.'''
milhão = list(range(1,1000001))
print(min(milhão))
print(max(milhão))
print(sum(milhão))

'''
4.6 - Números impares: Use o terceiro argumento da função range() para criar uma lista de números impares de 1 a 20. Utilize um laço for para exibir todos os números.'''
for n in range(1,20,2):
    print(n)

''' 
4.7 - Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use o laço for para exibir os números de sua lista.'''
for n in range(3,30,3):
    print(n)

'''
4.8 - Cubos: Um número elevado a terceira potência é chamado de cubo. Por exemplo, o cubo de 2 é escrito como 2**3 em Python.
Crie uma lista dos dez primeiros cubos (isto é, o cubo de cado inteiro de 1 a 10), e utilize um laço for para exibir o valor de cada cubo.'''
for n in range(1,11):
    print(n**3)

