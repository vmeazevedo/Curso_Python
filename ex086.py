#Matrizes 3x3

matriz = [0,0,0],[0,0,0],[0,0,0]    #Matriz

#Adicionando os dados da matriz
for l in range(0,3):                        #laço para todas as linhas
    for c in range(0,3):                    #laço para todas as colunas
        #Armazenamento dos dados do laço
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) 

#Imprime o laço a cada 3 colunas preenchidas pulando uma linha
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')    #Imprime os 3 valores e pula uma linha
    print()
    