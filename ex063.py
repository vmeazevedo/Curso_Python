numero = int(input('Digite um número para saber a sua sequência de Fibonacci: '))
num_anterior = 0

while(numero < 50):
    print(numero)
    numero = numero + num_anterior
    num_anterior = numero - num_anterior
    if(numero == 0):
        numero = numero + 1