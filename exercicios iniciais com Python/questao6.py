#Faça um programa que receba 10 números e conte quantos deles estão no intervalo
# entre 10 e 20, inclusive, e quantos deles estão fora do intervalo, escrevendo estas informações.
dentro = []
fora = []
cont = 0
cont2 = 0
soma = 0
for n in range (1,11):
    num = int(input('Digite um valor:'.format(n)))
    if num > 10 and num < 20:
         soma += num
         cont += 1
         dentro.append(num)
    else:
        cont2 += 1
        fora.append(num)

print('teste {} soma {}'.format(cont,soma))
print('Nu{}'.format(dentro))
print('Numeros {} '.format(fora))

