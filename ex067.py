vezes = 0

#Tabuado em loop infinito
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for num in range(1,11): 
        multi = n * num
        print(f'{n} x {num} = {multi}')
        vezes = vezes +1

print('Programa encerrado')