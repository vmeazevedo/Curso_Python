#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

# MENU EM PYTHON 3
      
def print_menu():       ## Design de menu
    print ("Bem vindo ao sistema básico de MENU\n")
    print ("1. Opção 1")
    print ("2. Opção 2")
    print ("3. Opção 3")
    print ("4. Opção 4")
    print ("5. Sair\n")
   
loop=True      
  
while loop:          ## While loop vai continuar até que seja = False
    print_menu()    ## Apresenta o menu
    choice = int(input("Escolha uma opção de 1-5: "))
     
    if choice== 1:     
        print ("\nOpção 1 foi selecionada\n")
        ## Pode adicionar o seu cógigo a ser executado aqui
    elif choice==2:
        print ("\nOpção 2 foi selecionada\n")
        ## Pode adicionar o seu cógigo a ser executado aqui
    elif choice==3:
        print ("\nOpção 2 foi selecionada\n")
        ## Pode adicionar o seu cógigo a ser executado aqui
    elif choice==4:
        print ("\nOpção 3 foi selecionada\n")
        ## Pode adicionar o seu cógigo a ser executado aqui
    elif choice==5:
        print ("\nAté logo!\n")
        ## Pode adicionar o seu cógigo a ser executado aqui
        loop=False # Isso vai fazer o while loop parar, "setar" False

    else:
        # Qualquer input diferente dos valores de 1-5 será apresentado a mensagem de erro abaixo
        print("\nOpção inválida. Entre com uma opção válida para prosseguir...\n")
      
