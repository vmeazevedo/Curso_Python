#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

# importa o modulo para interface grafica
import tkinter 
# importa strftime para mostrar a hora
from time import strftime 

#CRIANDO NOSSO RELÓGIO
rel = tkinter.Label() # criar uma label vazia
rel.pack() # deixa o conteudo visivel dentro da label
rel['text'] = strftime('%H:%M:%S') # formato de hora
rel['font'] = 'Arial 50 bold' # define a fonte do relogio
rel['foreground'] = 'white' # define a cor dos numeros
rel['bg'] = 'black' # define a cor do fundo bg e a abreviatura de background

def contador(): 
        agora = strftime('%H:%M:%S') # a variavel agora recebe a hora do sistema
        if rel['text'] != agora: # se a hora passada para rel['text'] for diferente de agora, rel['text'] recebe o conteudo de agora que e a hora do sistema
                rel['text'] = agora
        rel.after(100, contador) # a cada 100 milisegundos a funcao contador sera chamada e a hora sera atualizada !
contador() # chama a funcao contador

rel.mainloop()