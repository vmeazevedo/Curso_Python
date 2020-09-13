import json

filename = 'Arquivo_Exceções\\numbers.json'             #Garantimos que se trata do mesmo arquivo
with open(filename) as file_oject:                      #Acessamos o arquivo em modo de leitura
    numbers = json.load(file_oject)                     #Usamos a função json.load() para carregar as informações armazenadas, e guardamos na var numbers
print(numbers)                                          #Apresentamos a lista de numeros armazenada na var numbers

