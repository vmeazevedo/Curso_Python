#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

print("\tBem vindo!\n Calculos de Regra de 3\n")

def print_menu():       ## Design de menu

    print("\n As operações de regra de 3 que você pode fazer nessa calculadora são:\n")
    print ("1. Calculos com numeros inteiros.")
    print ("2. Calculos de numeros com virgula.")
    print ("3. Sair\n")

#Variaveis
inteiros = 1
numeros = 2
sair = 3

loop=True      
  
while loop:          ## While loop vai continuar até que seja = False
  print_menu()    ## Apresenta o menu
  operacao = int(input("Qual opção de calculos iremos utilizar?"))

#ESTRUTURA DE CALCULO
#
#  Variavel	     Incognita	
#    A     	  =   	 C
#    B  	    	     X

  if operacao == 1:
    print ("\nOpção 1 foi selecionada\n")
    print ("A estrutura de calculo é: A/B = C/X\n")
    print ("Coloque os dados de acordo com o solicitado\n")
    a = int(input("Digite o primeiro valor (A) da regra, conforme a estrutura de calculo:"))
    b = int(input("Digite o segundo valor (B) da regra, conforme a estrutura de calculo:"))
    c = int(input("Digite o terceiro valor (C) da regra, conforme a estrutura de calculo:"))
    print("O valor de X é:",(b*c)/a)
    print("\n")

  elif operacao == 2:
    print ("\nOpção 2 foi selecionada\n")
    print ("A estrutura de calculo é: A/B = C/X\n")
    print ("Coloque os dados de acordo com o solicitado\n")
    a = float(input("Digite o primeiro valor (A) da regra, conforme a estrutura de calculo:"))
    b = float(input("Digite o segundo valor (B) da regra, conforme a estrutura de calculo:"))
    c = float(input("Digite o terceiro valor (C) da regra, conforme a estrutura de calculo:"))
    print("O valor de X é:",(b*c)/a)
    print("\n")
  
  elif operacao == 3:
    print ("\nAté logo!\n")
    loop=False
    break

  else:
    print("\nOpção inválida. Entre com uma opção válida para prosseguir...\n")
