#Testando uma função - Essa função inicialmente passa em nosso teste unitário
# def get_formatted_name(first, last):
#     '''Gera um nome completo formatado de modo elegante.'''
#     full_name = first + ' ' + last
#     return full_name.title()

#Testando uma função - Essa função inicialmente não passará em nosso teste unitário pois falta 1 argumento.
# def get_formatted_name(first, middle, last):
#     '''Gera um nome completo formatado de modo elegante.'''
#     full_name = first + ' ' + middle + ' ' + last
#     return full_name.title()

#Testando uma função - Essa função sempre passará em nosso teste unitário
def get_formatted_name(first, last, midle=''):
    '''Gera um nome completo formatado de modo elegante.'''
    if midle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()