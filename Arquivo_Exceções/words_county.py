def count_words(filename):
    '''Conta o número aproximado de palavras em um arquivo.'''
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = 'Sorry, the file ' + filename + ' doest not exist.'
        print(msg)
    else:
        '''Conta o número aproximado de palavras no arquivo.'''
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) + ' words.')

filenames = 'Arquivo_Exceções\\alice.txt', 'Arquivo_Exceções\\siddharta.txt', 'Arquivo_Exceções\\moby_dick.txt', 'Arquivo_Exceções\\litte_women.txt'
for n in filenames:
    count_words(n)

