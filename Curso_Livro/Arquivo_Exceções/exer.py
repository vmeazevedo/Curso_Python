'''
10.1 - Aprendendo Python: Abra um arquivo em branco em seu editor de texto e escreva algumas linhas que
sintetizem o que você aprendeu sobre Python até agora. Comece cada linha com a expressão Em Python podemos...
Salve o arquivo como learning_python.txt no mesmo diretório em que estão seus exercícios deste capítulo.
Escreva um programa que leia o arquivo e mostre o que você escreveu, três vezes. Exiba o conteúdo uma vez
lendo o arquivo todo, uma vez percorrendo o objeto arquivo com um laço, e outra armazenando as linhas em uma lista
e então trabalhando com ela fora do bloco with.
'''
#Exiba o conteúdo uma vez lendo o arquivo todo
filename = 'C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\learning_python.txt'     #Identificamos o local do arquivo
with open(filename) as file_object:                                                                             #Abrimos o arquivo como objeto
    conteudo = file_object.read()                                                                               #Acessamos a variavel com o metodo read.
    print(conteudo)                                                                                             #Printamos o conteudo do arquivo    
    print()

#Uma vez percorrendo o objeto arquivo com um laço
filename = 'C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\learning_python.txt'     #Identificamos o local do arquivo
with open(filename) as file_object:                                                                             #Abrimos o arquivo como objeto                 
    for line in file_object:                                                                                    #Acessamos cada linha do conteudo do arquivo com um laço
        print(line.rstrip())                                                                                    #Printamos o conteúdo formatado
print()

#E outra armazenando as linhas em uma lista e então trabalhando com ela fora do bloco with
filename = 'C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\learning_python.txt'     #Identificamos o local do arquivo     
with open(filename) as file_object:                                                                             #Abrimos o arquivo como objeto
    lines = file_object.readlines()                                                                             #Acessamos a variável com o metodo readlines

for n in lines:                                                                                                 #Para cada item dentro da variável            
    print(n.rstrip())      
print()                                                                                         #Printamos o conteúdo formatado

'''
10.2 - Aprendendo C: Você pode usar o metodo replace() para substituir qualquer palavra por uma palavra
diferente em uma string. Eis um exemplo rápido que mostra como substituir a palavra 'dog' por 'cat' em
uma frase:
message = 'I really like dogs.'
message.replace('dog','cat')
I really like cats.

Leia cada linha do arquivo learning_python.txt que você acabou de criar e substitua a palavra Python pelo
nome de outra linguagem, por exemplo, C. Mostre cada linha modificada na tela.
'''
filename = 'C:\\Users\\pqcir\\Documents\\MeusProjetos\\Curso_Python\\Arquivo_Exceções\\learning_python.txt'     #Identificamos o local do arquivo
with open(filename) as file_object:
    conteudo = file_object.read()
    X = conteudo.replace('Python','C')                                                     #Como objeto não tem o atributo replace, precisamos salvar ele em uma variável
    print(X.rstrip())