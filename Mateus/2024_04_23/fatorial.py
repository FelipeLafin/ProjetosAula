print('')
print('-----------------------------------------------------------------------------')
n1 = int(input('Digite o número que deseja calcular o fatorial: '))
fatorial = 1
resultado = []
numeros = []
for i in range(n1):
    fatorial = fatorial * (i+1)
    resultado.append(fatorial)
    numeros.append(i+1)
print('')
print(n1, '! =', sorted(numeros, reverse = True), '=', fatorial)
print('-----------------------------------------------------------------------------')