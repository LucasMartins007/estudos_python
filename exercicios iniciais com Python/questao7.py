import sys

def validar_idade():
    try:
        idade = int(input("informe sua idade: "))
        if(idade <= 0):
            return -1
        else:
            return idade
    except ValueError:
        print("Idade deve ser um numero")
        return validar_idade()
    

def validar_genero():
    try:
        genero = str(input("informe seu genero: "))
        
        if(genero != 'M' and genero != "F"):
            print("Genero deve ser M ou F")
            validar_genero()
        else:
            return genero

    except ValueError:
        print("Genero deve ser M ou F")
        return validar_genero()


def validar_salario():
    try:
        return float(input("informe seu sálario: "))
    except ValueError:
        print("Valor digitado inválido")
        return validar_salario()

def calcular_media(salarios):
    totalSalario = 0
    counter = 0
    for x in salarios:
        counter+=1
    return sum(salarios) / counter

    
def get_maior(idades):
    return max(idades)

def get_menor(idades):
    return min(idades)

def get_homens(generos):
    homens = 0
    for gen in generos:
        if(gen == "M"):
            homens += 1
    return homens

def get_mulheres(generos):
    mulheres = 0
    for gen in generos:
        if(gen == "F"):
            mulheres += 1
    return mulheres


def get_pessoa_menor_salario(salarios, pessoas):
    pessoa_menor_salario = []
    for pessoa in pessoas:
        if(pessoa[3] == min(salarios)):
            pessoa_menor_salario.append(pessoa)
    return pessoa_menor_salario

def gerar_pessoa(dados, count, idade, genero, salario, pessoas):
    dados.append(count)
    dados.append(idade)
    dados.append(genero)
    dados.append(salario)
    pessoas.append(dados)
    return pessoas

def main():
    controle = False
    salario = 0
    idade = 0
    genero = 0
    idades = []
    generos = []
    salarios = []
    dados_pessoa = []
    pessoas = []

    print("Para sair da aplicação digite uma idade negativa.. ")
    count = 0
    while(controle == False):
        dados_pessoa = []
        count += 1

        idade = validar_idade()
        if (idade == -1):
            break
        else:
            idades.append(idade)

        genero = validar_genero()
        generos.append(genero)

        salario = validar_salario()
        salarios.append(salario)
        

        pessoas = gerar_pessoa(dados_pessoa, count, idade, genero, salario, pessoas)
        
    
    if(salarios.count(salario) == 0 or generos.count(genero) == 0 or idades.count(idade) == 0):
        print("Não foi digitado valores suficientes para o calculo.")
    else:
        pessoa_menor_salario = get_pessoa_menor_salario(salarios, pessoas)

        print("\n\nExercício A:\n   A média dos salários do grupo é: " + str(calcular_media(salarios)))

        print("\n\nExercício B:\n   A maior idade do grupo é: " + str(get_maior(idades)) 
                + "\n   A menor idade do grupo é: " + str(get_menor(idades)))

        print("\n\nExercício C:\n   A quantidae de homens é: " + str(get_homens(generos)) 
                + "\n   A quantiade de mulheres é: " + str(get_mulheres(generos)))

        print("\n\nExercício D:\n   A idade da pessoa com o menor salário é: " + str(pessoa_menor_salario[0][1]) 
                + "\n   o gênero da pessoa com o menor salário é: " + str(pessoa_menor_salario[0][2]))
        


main()