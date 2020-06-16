#Armazenando dados
#Usando json.dump() e json.load()
import json                                             #Importamos o json
numbers = [2,3,5,7,11,13]                               #Criamos uma lista com valores aleatórios

filename = 'Arquivo_Exceções\\numbers.json'             #Declaramos nosso diretorio com a extensão .json
with open(filename, 'w') as file_object:                #Abrimos o arquivo com a função write
    json.dump(numbers, file_object)                     #Usamos a função json.dump() para armazenar a lista no arquivo

