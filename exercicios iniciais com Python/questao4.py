import sys


# print('Digite 10 idades para ser calculado a média')

# idade1 = int (input('Digite uma idade'))
# idade2 = int (input('Digite uma idade'))
# idade3 = int (input('Digite uma idade'))
# idade4 = int (input('Digite uma idade'))
# idade5 = int (input('Digite uma idade'))
# idade6 = int (input('Digite uma idade'))
# idade7 = int (input('Digite uma idade'))
# idade8 = int (input('Digite uma idade'))
# idade9 = int (input('Digite uma idade'))
# idade10 = int (input('Digite uma idade'))

# média = (idade1 + idade2 + idade3 + idade4 + idade5 + idade6 + idade7 + idade8 + idade9 + idade10) / 10
# print('media das idades é', média)


print("Digite 10 idade para ser calculado a média: ")
idades = []
count = 0
for idade in range(10):
    try:
        idade = int(input('Digite uma idade: '))
        idades.append(idade)
        count += 1
    except ValueError:
        sys.exit()

media = sum(idades) / count
print('media das idades é', media)
