import sys

def main():
    notas = [2.0, 5.0, 10.0, 20.0, 50.0, 100.0]    

    while True:
        resultado_saque = saque(notas)     
        if(resultado_saque != 0):
            msg_notas_entregues = str(resultado_saque).replace("]", " reais").replace("[", "").replace(",", " reais,").replace(".0", "")
            valor_total_saque = str(sum(resultado_saque))

            print("\nVocê fez um saque de " + valor_total_saque + " reais \n")
            print("Foram entregues as notas de " + msg_notas_entregues + "\n")




def saque(notas):
        try:
            input_value = input("Informe o valor que deseja sacar (ou S para sair): ")
            valor_saque = float(input_value)
            return verificar_saque(valor_saque, notas)
        except ValueError:
            if(input_value == "S"):
                sys.exit()
            print("Valor inserido Inválido. \n")
            return 0
            

def verificar_saque(valor_saque, notas):
    if(is_valid_valor_saque(valor_saque) == True):
        return calcular_notas_utilizadas(notas, valor_saque)
    else:
        print("Possuimos somente as notas 2, 5, 10, 20, 50 e 100 reais, por favor informe uma valor que possa ser calculado com essas notas. \n")
        return 0


def is_valid_valor_saque(valor_saque):
        return (valor_saque != 0.0 and ((valor_saque % 2) == 0 or (valor_saque % 5) == 0))
         

def calcular_notas_utilizadas(notas, valor_saque):
    notas_utilizadas = []

    while(valor_saque != 0):
        if(valor_saque >= notas[5]):
            notas_utilizadas.append(notas[5])
            valor_saque -= notas[5]

        elif(valor_saque >= notas[4]):
            notas_utilizadas.append(notas[4]) 
            valor_saque -= notas[4]

        elif(valor_saque >= notas[3]):
            notas_utilizadas.append(notas[3]) 
            valor_saque -= notas[3]
                    
        elif(valor_saque >= notas[2]):
            notas_utilizadas.append(notas[2]) 
            valor_saque -= notas[2]
                     
        elif(((valor_saque - notas[1]) % 2) == 0 and valor_saque >= notas[1]):
            notas_utilizadas.append(notas[1]) 
            valor_saque -= notas[1]

        elif(valor_saque >= notas[0]):
            notas_utilizadas.append(notas[0]) 
            valor_saque -= notas[0]

    return notas_utilizadas



main()
    