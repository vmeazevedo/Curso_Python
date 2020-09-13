#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone
    microfone = sr.Recognizer()
    
    #Usando o microfone
    with sr.Microphone() as source:
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')
        #Retorna a frase pronunciada
        print("Você disse: " + frase)
        
        #Se nao reconheceu o padrao de fala, exibe a mensagem
    except:
        print("Não entendi")
        
    return frase

#Funcao responsavel por falar 
def cria_audio(audio):
    tts = gTTS(audio,lang='pt-br')
    #Salva o arquivo de audio
    tts.save('Sua_frase.mp3')
    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    playsound('Sua_frase.mp3')

frase = ouvir_microfone()
cria_audio(frase)
    



