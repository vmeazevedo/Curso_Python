num = [], []    #Cria uma lista com 2 digitos dentro
valor = 0

#Imprindo 7 valores e separando dentro de uma mesma lista os valores pares e impares.
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))    #Solicita ao usuario um valor
    if valor %2 == 0:                    #Se o valor for par
        num[0].append(valor)        #Registra o valor no num[0]
    else:
        num[1].append(valor)        #Senão registra o valor no num[1]

print('-='*30)
num[0].sort()   #organiza os valores em ordem
num[1].sort()
print(f'Todos os valores: {num} ')  #Imprime a lista separando par e impar
print(f'Os valores pares digitados foram: {num[0]} ')  #Imprime o conteudo em num[0]
print(f'Os valores ímpares digitados foram: {num[1]}')  #Imprime o conteudo em num[1]