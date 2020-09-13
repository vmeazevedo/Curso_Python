#Gerando um gráfico linear simples
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()

#Alterando o tipo do rótulo e a espessura do gráfico
import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
plt.plot(squares, linewidth=5)                          #Aumenta o tamanho da linha de informações

'''Define o título do gráfico e nomeia os eixos'''
plt.title('Square Numbers', fontsize=20)                #Define o título do gráfico
plt.xlabel('Value', fontsize=14)                        #Define o título do eixo X
plt.ylabel('Square of Value', fontsize=14)              #Define o título do eixo Y

'''Define o tamanho dos rótulos das marcações'''
plt.tick_params(axis='both', labelsize=10)              #Define o tamanho dos números dos eixos X e Y

plt.show()                                              #Apresenta o gráfico


#Corrigindo o gráfico
import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]                              #Valores de entrada
squares = [1,4,9,16,25]                                 #Valores de saída
plt.plot(input_values, squares, linewidth=5)                          #Aumenta o tamanho da linha de informações

'''Define o título do gráfico e nomeia os eixos'''
plt.title('Square Numbers', fontsize=20)                #Define o título do gráfico
plt.xlabel('Value', fontsize=14)                        #Define o título do eixo X
plt.ylabel('Square of Value', fontsize=14)              #Define o título do eixo Y

'''Define o tamanho dos rótulos das marcações'''
plt.tick_params(axis='both', labelsize=10)              #Define o tamanho dos números dos eixos X e Y

plt.show()                                              #Apresenta o gráfico
