
def main():
    conta = []
    saldo_inicial = 0
    conta.append(saldo_inicial)
    opcao = 0
    
    while opcao != "D":
        opcao = mostrar_perguntas()
        
        if opcao == "A":
            print("Seu saldo atual é: " + str(consulta_saldo(conta)) + "\n")

        elif opcao == "B":
            sacar(conta)
            print("Seu saldo atual é: " + str(consulta_saldo(conta)) + "\n")

        elif opcao == "C":
            depositar(conta)
            print("Seu saldo atual é: " + str(consulta_saldo(conta)) + "\n")


def is_opcao_invalida(opcao):
    return opcao == "A" or opcao == "B" or opcao == "C" or opcao == "D"


def consulta_saldo(conta):
    return sum(conta)

def atualizar_saldo(conta, valor):
    return conta.append(valor)


def validar_opcao():
    try:
        opcao = str(input("Informe a opção que deseja: "))
        if is_opcao_invalida(opcao) == False:
            print("Você deve digitar uma das opções acima")
            validar_opcao()
        return opcao
    except ValueError:
        print("Você deve digitar uma das opções citadas anteriormmente. ")
        validar_opcao()


def sacar(conta):
    try:
        valor = float(input("Informe o valor a ser sacado: "))
        if (valor > consulta_saldo(conta)):
            print("Você não possui esse valor na sua conta")
            sacar(conta)
        else:
            return atualizar_saldo(conta, -valor)
    except ValueError:
        print("Valor inválido")


def depositar(conta):
    try:
        valor = float(input("Informe o valor a depositar: "))
        if (valor < 0):
            print("Você não pode depositar um valor negativo")
            depositar(conta)
        else:
            return atualizar_saldo(conta, valor)
    except ValueError:
        print("Valor inválido")
        

def mostrar_perguntas():
    print("O que deseja fazer?")
    print("A - Consultar saldo")
    print("B - Sacar ")
    print("C - Depóstio ")
    print("D - Sair ")
    return validar_opcao()




main()