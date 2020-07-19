entrada = int(input('Digite o número que gostaria de converter: '))

print('\nMenu:')
print('1. Binário')
print('1. Octal')
print('1. Hexadecimal')

sel = int(input('\n Por favor, selecione a opção desejada: '))
if sel == 1:
    print('Binário foi selecionado.')
    int_bin = bin(entrada)[2:]
    print(int_bin)

elif sel == 2:
    print('Octal foi selecionado.')
    int_octal = oct(entrada)[2:]
    print(int_octal)

elif sel == 3:
    print('Hexadecimal foi selecionado.')
    int_hex = hex(entrada)[2:]
    print(int_hex)

