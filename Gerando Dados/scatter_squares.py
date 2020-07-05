#Plotando e estilizando pontos individuais com scatter()
# import matplotlib.pyplot as plt

# plt.scatter(2,4, s=200)                                     #S é o tamanho do ponto a ser apresentado

# '''Define o título do gráfico e nomeia os eixos'''
# plt.title('Square Numbers', fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)

# '''Define o tamanho dos rótulos das marcações'''
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()

#Plotando uma série de pontos com scatter()
# import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5]                                      #Dados de entrada
# y_values = [1,4,9,16,25]                                    #Dados de saída
# plt.scatter(x_values, y_values, s=100)                      #S é o tamanho do ponto a ser apresentado

# '''Define o título do gráfico e nomeia os eixos'''
# plt.title('Square Numbers', fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)

# '''Define o tamanho dos rótulos das marcações'''
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()

#Calculando dados automaticamente
# import matplotlib.pyplot as plt

# x_values = list(range(1,1001))                          #Criamos uma lista de valores de x de 1 a 1000
# y_values = [x**2 for x in x_values]                     #Analisamos os valores de x da lista x_values e elevamos ele ao quadrados

# plt.scatter(x_values, y_values, s=40)                   #Passamos os valores de x e y para o scatter

# '''Define o título do gráfico e nomeia os eixos'''
# plt.title('Square Numbers', fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)

# '''Define o intervalo para cada eixo'''
# plt.axis([0, 1100, 0, 1100000])                 #Especificamos o intervalo de cada eixo, a função axis exige 4 valores: os valores min e max para cada eixo.
# plt.show()

#Definindo cores personalizadas
# import matplotlib.pyplot as plt

# x_values = list(range(1,1001))                          #Criamos uma lista de valores de x de 1 a 1000
# y_values = [x**2 for x in x_values]                     #Analisamos os valores de x da lista x_values e elevamos ele ao quadrados

# # plt.scatter(x_values, y_values, c='red', s=40)                   #Passando c no scatter podemos selecionar outra cor para a linha
# plt.scatter(x_values, y_values, c=(0, 1, 0), s=40)                 #Passando c no scatter podemos selecionar outra cor para a linha

# '''Define o título do gráfico e nomeia os eixos'''
# plt.title('Square Numbers', fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)

# '''Define o intervalo para cada eixo'''
# plt.axis([0, 1100, 0, 1100000])                 #Especificamos o intervalo de cada eixo, a função axis exige 4 valores: os valores min e max para cada eixo.
# plt.show()


#Usando um colormap
# import matplotlib.pyplot as plt

# x_values = list(range(1,1001))                          #Criamos uma lista de valores de x de 1 a 1000
# y_values = [x**2 for x in x_values]                     #Analisamos os valores de x da lista x_values e elevamos ele ao quadrados

# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=40)                 #Passando c no scatter podemos selecionar outra cor para a linha

# '''Define o título do gráfico e nomeia os eixos'''
# plt.title('Square Numbers', fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)

# '''Define o intervalo para cada eixo'''
# plt.axis([0, 1100, 0, 1100000])                 #Especificamos o intervalo de cada eixo, a função axis exige 4 valores: os valores min e max para cada eixo.
# plt.show()

#Salvando seus gráficos automaticamente
# import matplotlib.pyplot as plt

# x_values = list(range(1,1001))                          #Criamos uma lista de valores de x de 1 a 1000
# y_values = [x**2 for x in x_values]                     #Analisamos os valores de x da lista x_values e elevamos ele ao quadrados

# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=40)                 #Passando c no scatter podemos selecionar outra cor para a linha

# '''Define o título do gráfico e nomeia os eixos'''
# plt.title('Square Numbers', fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)

# '''Define o intervalo para cada eixo'''
# plt.axis([0, 1100, 0, 1100000])                 #Especificamos o intervalo de cada eixo, a função axis exige 4 valores: os valores min e max para cada eixo.
# plt.savefig('Gerando Dados\\squares_plot.png', bbox_inches='tight')     #Salva a imagem do gráfico no diretório que estamos trabalhando.



'''15.1 - Cubos: Um número elevado a terceira potência é chamado de cubo. Faça a plotagem dos cinco primeiros números elevados ao cubo
e em seguida, dos primeiros 5000 números elevados ao cubo.'''
print('\n15.1 - Cubos')
import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,8,27,64,125]

plt.scatter(x_values, y_values, s=40)
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, s=40)
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.axis([0, 5500, 0, 16000000000]) 
plt.show()

'''15.2 - Cubos Coloridos: Aplique um colormap ao seu gráfico de cubos.'''
print('\n15.1 - Cubos Coloridos')
import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=50)
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.axis([0, 5500, 0, 16000000000]) 
plt.show()