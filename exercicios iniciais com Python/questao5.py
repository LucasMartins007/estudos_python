soma = 0
cont = 0
for c in range (1,7):
    num = int (input('Digite um valor:'.format(c)))
    if num % 2 == 1:
      soma += num
      cont += 1
print('Voce informou {} numeros impares a soma foi {}'.format(cont,soma))