# =--- Bibliotecas ---=
import math
import pyfiglet
from rich.console import Console

# =--- Funções ---=
def soma(numero1, numero2):
    conta = numero1 + numero2
    return conta

def subtracao(numero1, numero2):
    conta = numero1 - numero2
    return conta

def multiplicacao(numero1, numero2):
    conta = numero1 * numero2
    return conta

def divisao(numero1, numero2, opcao):
    if opcao == 0:
        conta = numero1 / numero2
    elif opcao == 1:
        conta = numero1 / numero2
    else:
        conta = numero2 / numero1

    return conta

def raiz_quadrada(numero):
   conta = math.sqrt(numero)
   return conta


def exponenciacao(base, expoente):
    conta = math.pow(base, expoente)
    return conta


def raiz_cubica(numero):
    conta = math.cbrt(numero)
    return conta


def funcao_seno(numero):
    conta = math.sin(numero)
    return conta


def funcao_cosseno(numero):
    conta = math.cos(numero)
    return conta

def funcao_tangente(numero):

    conta = math.tan(numero)
    return conta

# =--- Fim das funções ---=

# =--- Main ---=
sair_calculadora = False

console = Console()
console.print("[bold magenta]Bem-vinda à Calculadora das Codificadoras![/bold magenta]")

while sair_calculadora != True:

    #Menu de opções da calculadora
    while True:
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Raiz quadrada")
        print("6 - Raiz cúbica")
        print("7 - Exponenciação")
        print("8 - Seno")
        print("9 - Cosseno")
        print("10 - Tangente")
        print("Pressione 11 para sair da Calculadora ")

        #Tratamento de erro para caso o usuário digite uma string em vez de um inteiro
        try:
            opcao_conta_matematica = int(input("Digite sua opção:"))
            print("\n")
        except:
            print("O valor recebido foi uma string, por favor digite um número!")

        if(opcao_conta_matematica >= 1 and opcao_conta_matematica <=11):
            break
        else:
            print("Você escolheu uma opção inválida, por favor escolha uma opção válida!")
    #while para tratamento de erro de opção inválida

    #Recebendo os valores dos números de acordo com a opção do usuário
    if opcao_conta_matematica >= 1 and opcao_conta_matematica <=4:
        #Para fazer as contas das opções 1 à 4 precisamos de 2 números
        numero1 = float(input("Digite o primeiro número:"))
        numero2 = float(input("Digite o segundo número:"))
    elif opcao_conta_matematica >= 5 and opcao_conta_matematica <=10:
        #Para fazer as contas da opção 5 à 10 precisamos somente de um número
        numero3 = float(input("Digite um número:"))

        #Como para calcular a raiz quadrada precisamos de um número positivo, caso for recebido um número negativo, multiplicaremos por -1 para torná-lo positivo
        if opcao_conta_matematica == 5 and numero3 < 0:
            numero3 = numero3 * -1

    #Usando um Match para cada caso das operações matemáticas
    match opcao_conta_matematica:
        case 1:
            resultado = soma(numero1, numero2)
            print(f"{numero1} + {numero2} = {resultado} \n")
        #fecha caso 1

        case 2:
           resultado = subtracao(numero1, numero2)
           print(f"{numero1} - {numero2} = {resultado} \n")
        #fecha caso 2

        case 3:
            resultado = multiplicacao(numero1, numero2)
            print(f"{numero1} * {numero2} = {resultado} \n")
        #fecha caso 3

        case 4:
            if(numero1 == numero2):
                opcao_divisao = 0
                resultado = divisao(numero1, numero2, opcao_divisao)

                print(f"{numero1} dividivo por {numero2} = {resultado} \n")
            else:
                while True:
                    print("Escolha uma das opções abaixo:")
                    print(f"1 - Dividir {numero1} por {numero2}")
                    print(f"2 - Dividir {numero2} por {numero1}")
                    opcao_divisao = int(input("Digite sua opção:"))

                    if opcao_divisao == 1 or opcao_divisao == 2:
                        break
                    else:
                        print("Por favor, digite uma opção válida!")

                resultado = divisao(numero1, numero2, opcao_divisao)

                if opcao_divisao == 1:
                    print(f"A divisão de {numero1} por {numero2} = {resultado} \n")
                else:
                    print(f"A divisão de {numero2} por {numero1} = {resultado} \n")

        case 5:
           resultado = raiz_quadrada(numero3)
           print(f"A raiz quadrada de {numero3} é {resultado} \n")

        case 6:
            resultado = raiz_cubica(numero3)
            print(f"A raiz cúbica de {numero3} é {resultado} \n")

        case 7:
            expoente = int(input(f"Digite o número a qual {numero3} vai estar elevado"))
            resultado = exponenciacao(numero3, expoente)

            print(f"{numero3} elevado à {expoente} = {resultado} \n")

        case 8:
            resultado = funcao_seno(numero3)
            print(f"O seno de {numero3} é {resultado} \n")

        case 9:
            resultado = funcao_cosseno(numero3)
            print(f"O cosseno de {numero3} é {resultado} \n")

        case 10:
            resultado = funcao_tangente(numero3)
            print(f"A tangente de {numero3} é {resultado} \n")

        case 11:
            sair_calculadora = True

print("Obrigada por utilizar a calculadora das Codificadoras!")

   