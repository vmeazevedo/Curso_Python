'''
11.1 - Cidade, país: Escreva uma função que aceite dois parâmetros: o nome de uma cidade e o nome de um país.
A função deve devolver uma única string no formato Cidade, País, por exemplo, Santiago, Chile. Armazene a função
em um módulo chamado city_functions.py

Crie um arquivo de nome test_cities.py que teste essa função que você acabou de escrever (lembre-se de que é 
necessário importar unittest e a função que você quer testar). Escreva um método chamado test_city_country() para
conferir se a chamada a sua função com valores como 'santiago, chile' resulta na strin correta. Execute test_cities.py
e garanta que test_city_country() passe no teste.
'''
import unittest
from city_functions import dados_pais

class NamesTestCase(unittest.TestCase):                        #Criamos uma classe que conterá varios testes de unidades, essa classe deve herdar da classe unittest.TestCase
    '''Testes para 'city_function.py'.'''

    def test_city_country(self):                                #Criei um metodo para conferir se a função funciona com os dois valores
        info_pais = dados_pais('santiago','chile')              #Chamei a função que vou testar e armazei os dados em um valor de retorno
        self.assertEqual(info_pais, 'Santiago, Chile')          #Comparei o valor de retorno com a string esperada

unittest.main()


'''
11.2 - População: Modifique sua função para que ela exija um terceiro parametro, population. Agora ela deve devovler uma unica string
no formato Cidade, Pais - população xxx, por exemplo, Santiago, Chile - população 50000000. Execute test_cities.py novamente. Certifique-se de que
test_city_country() falhe dessa vez.

Modifique a função para que o parametro population seja opcional. Execute test_cities.py novamente e garanta que o test_city_country() passe.

Escreva um segundo teste chamado test_city_country_population() que verifique se voce pode chamar sua função com os valores 'santiago', 'chile'
e 'population=50000000'. Execute test_cities.py novamente e garanta que esse novo teste passe.
'''