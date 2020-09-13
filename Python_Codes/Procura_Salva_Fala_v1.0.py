#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

import wikipedia
import os
from playsound import playsound
from gtts import gTTS
import unicodedata
import re
import speech_recognition as sr
import pyaudio

def removerAcentosECaracteresEspeciais(palavra):
    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

class AssistenteDeBusca:
    def __init__(self, pesquisa):
        self.pesquisa = removerAcentosECaracteresEspeciais(pesquisa)
        # pasta onde ficara as pastas dos arquivos
        #self.pesquisa = pesquisa
        self.nome_pasta = 'Arquivos_da_wiki'
        # diretório atual onde o python esta sendo executado
        self.diretorio_atual = os.getcwd()
        # caminho do diretorio da pasta
        self.diretorio_pasta = os.path.join(self.diretorio_atual, self.nome_pasta)
        # caminho do diretorio da pasta arquivo
        self.diretorio_pasta_arquivo = os.path.join(self.diretorio_pasta, pesquisa)
        # caminho do arquivo mp3
        self.caminho_arquivo_mp3 = os.path.join(self.diretorio_pasta_arquivo, pesquisa + '.mp3')

        print('Por favor, Aguarde enquanto terminamos a tarefa!')

        # configurando linguagem da pesquisa para português
        wikipedia.set_lang('pt')

        self.texto_recebido = wikipedia.summary(self.pesquisa)

        # verificando pasta base existe
        if not os.path.exists(self.diretorio_pasta):
            # cria a pasta se mão existir
            os.mkdir(self.diretorio_pasta)

        # verifica se a pasta do arquivo existe
        if not os.path.exists(self.diretorio_pasta_arquivo):
            os.mkdir(self.diretorio_pasta_arquivo)

        self.cria_arquivo()

        self.cria_executa_mp3()

    def cria_executa_mp3(self):
        # verifica se o arquivo mp3 existe
        if not os.path.exists(self.caminho_arquivo_mp3):
            audio = gTTS(text=self.texto_recebido, lang='pt-br', slow=False)
            audio.save(self.caminho_arquivo_mp3)

        playsound('Arquivos_da_wiki/' + self.pesquisa + '/' + self.pesquisa + '.mp3')

    def cria_arquivo(self):
        with open(os.path.join(self.diretorio_pasta_arquivo, self.pesquisa), 'w', encoding='utf-8') as recebido:
            cont = 0
            contador = 0
            while contador != len(self.texto_recebido.split()):

                if cont == 10:
                    recebido.write(self.texto_recebido.split()[contador] + '\n')
                    cont = 0
                else:
                    recebido.write(self.texto_recebido.split()[contador] + ' ')
                    cont += 1
                contador += 1

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone
    microfone = sr.Recognizer()

    # Usando o microfone
    with sr.Microphone() as source:
        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        # Frase para o usuario dizer algo
        print("Diga alguma coisa: ")
        # Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

    try:
        # Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-br')
        print(type(frase))
        # Retorna a frase pronunciada
        print("Você disse: " + frase)
        # Se nao reconheceu o padrao de fala, exibe a mensagem
    except:
        print("Não entendi")
    else:
        return frase

if __name__ == '__main__':
    AssistenteDeBusca(ouvir_microfone())


