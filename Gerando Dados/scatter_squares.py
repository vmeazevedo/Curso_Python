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
import matplotlib.pyplot as plt

x_values = list(range(1,1001))                          #Criamos uma lista de valores de x de 1 a 1000
y_values = [x**2 for x in x_values]                     #Analisamos os valores de x da lista x_values e elevamos ele ao quadrados

# plt.scatter(x_values, y_values, c='red', s=40)                   #Passando c no scatter podemos selecionar outra cor para a linha
plt.scatter(x_values, y_values, c=(0, 1, 0), s=40)                 #Passando c no scatter podemos selecionar outra cor para a linha

'''Define o título do gráfico e nomeia os eixos'''
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

'''Define o intervalo para cada eixo'''
plt.axis([0, 1100, 0, 1100000])                 #Especificamos o intervalo de cada eixo, a função axis exige 4 valores: os valores min e max para cada eixo.
plt.show()