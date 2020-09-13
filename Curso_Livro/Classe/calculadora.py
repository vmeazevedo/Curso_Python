class Calculadora:

    def soma(self, a, b):
        return a + b

    def subtrai(self, a, b):
        return a - b

    def multiplica(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

c = Calculadora()

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))

print('\nResultados das operações')
print('Soma:', c.soma(a,b))
print('Subtração:', c.subtrai(a,b))
print('Multiplicação:', c.multiplica(a,b))
print('Divisão:', c.divide(a,b))
