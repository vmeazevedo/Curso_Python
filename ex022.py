nome = str(input('Digite o seu nome completo: '))
print(nome.upper()) #1
print(nome.lower()) #2


#Imprimir os nomes sem espaço algum
sem = nome.replace(' ','') #4
print(sem)

#Quantas letras tem o primeiro nome
dividido = nome.split() #4
print(len(dividido[0]))




