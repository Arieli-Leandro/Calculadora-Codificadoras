#Bibliotecas
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import paleta_de_cores as cores
import funcoes_calculadora as funcoes_matematicas

calculadora = tk.Tk() #Define a janela
calculadora.title("Calculadora") #Coloca o título da página

#Opção 1 - logo sem cor
#Coloca o ícone da página
#calculadora.iconbitmap("imagens/logo-sem-cor.ico") 

#Opção 2 - Logo com cor
#Coloca o ícone da página
calculadora.iconbitmap("imagens/logo-com-fundo.ico") 

#Opção 3 - Logo transparente
#Coloca o ícone da página
#calculadora.iconbitmap("imagens/logo-sem-fundo.ico") 

#Define o tamanho da janela
calculadora.geometry("324x245") 
calculadora.resizable(width=FALSE, height=FALSE) #Impede que o usuário expanda a janela

#Definindo os frames da Calculadora 
frame_pequeno = Frame(calculadora, width= 500, height=50, bg=cores.cinza)
frame_pequeno.grid(row=0, column=0)
frame_grande = Frame(calculadora, width= 500, height=268)
frame_grande.grid(row=1, column=0, sticky="w")

#Adicionando uma coluna invisível para separar os números das operações
frame_grande.columnconfigure(4, minsize=3)
frame_grande.rowconfigure(0, minsize=7)
frame_grande.rowconfigure(2, minsize=7)

valor_texto = StringVar()
primeiro_numero = None
operacao = None
calculadora_ligada = True

visor_calculadora = Label(frame_pequeno, textvariable=valor_texto, width= 26, height=2, padx=7, anchor='e', relief= FLAT, justify=RIGHT, font=("Ivy", 16, ""), bg=cores.cinza, fg=cores.branco)
visor_calculadora.grid(row=0, column=0)

#Funções necessárias para o funcionamento da calculadora (Vai aparecer no visor)
def inserir_valor(valor):
    global valor_texto
    atual = valor_texto.get()
    valor_texto.set(atual + str(valor))

def inserir_operacao(op):
    global primeiro_numero, operacao
    primeiro_numero = float(valor_texto.get())
    operacao = op
    valor_texto.set("")

def inserir_virgula():
    atual = valor_texto.get()

    if "." not in atual:
        if atual == "":
            valor_texto.set("0.")
        else:
            valor_texto.set(atual + ".")

def calcular():
    global primeiro_numero, operacao
    segundo_numero = float(valor_texto.get())

    match operacao:
        case "+" :
            resultado = funcoes_matematicas.soma(primeiro_numero, segundo_numero)
        case "-":
            resultado = funcoes_matematicas.subtracao(primeiro_numero, segundo_numero)
        case "*":
            resultado = funcoes_matematicas.multiplicacao(primeiro_numero, segundo_numero)
        case "÷":
            if segundo_numero != 0:
                resultado = funcoes_matematicas.divisao(primeiro_numero, segundo_numero)
            else:
                valor_texto.set("Indefinido!")
                return
        case "x^":
            resultado = funcoes_matematicas.exponenciacao(primeiro_numero, segundo_numero)
        case _:
            valor_texto.set(str("Operações unárias não precisam do '='"))

    valor_texto.set(str(resultado))

def calcula_operacoes_unarias(op):

    global operacao
    operacao = op

    try:
        numero = float(valor_texto.get())
        match operacao:
            case "√":
                resultado = funcoes_matematicas.raiz_quadrada(numero)
            case "∛":
                resultado = funcoes_matematicas.raiz_cubica(numero)
            case "sen(x)":
                resultado = funcoes_matematicas.funcao_seno(numero)
            case "cos(x)":
                resultado = funcoes_matematicas.funcao_cosseno(numero)
            case "tan(x)":
                resultado = funcoes_matematicas.funcao_tangente(numero)

        valor_texto.set(str(resultado))

    except:
        valor_texto.set("Erro, primeiro insira o número e depois a operação.")

#Função que vai ser usada na configuração do botão del
def deletar_caractere():
    atual = valor_texto.get()
    valor_texto.set(atual[:-1])

#Função que vai ser usada na configuração do botão reset
def resetar():
    global primeiro_numero, operacao
    valor_texto.set("")
    primeiro_numero = None
    operacao = None

#Verifica_pisca_ativo precisa estar aqui (quase o funcionamento de uma closure SEM RECURSÃO)
verifica_pisca_ativo = False
def pisca_texto_final():
    global verifica_pisca_ativo

    if verifica_pisca_ativo == False:
        return
    
    texto_atual = valor_texto.get()

    if texto_atual == "":
        valor_texto.set("------------------____")
    else:
        valor_texto.set("")

    #Vai reaparecer no visor depois de 500 milissegundos
    calculadora.after(500, pisca_texto_final)
    
def liga_desliga():
    global calculadora_ligada
    calculadora_ligada = not calculadora_ligada

    global verifica_pisca_ativo

    if calculadora_ligada == True:
        verifica_pisca_ativo = False

        valor_texto.set("")
        estado_calculadora = "normal"
    else:
        verifica_pisca_ativo = True 

        visor_calculadora.config(anchor='center', justify= CENTER, font=(tkFont.ITALIC, 13, "bold"), fg=cores.preto)
        #No valor_texto.set() tem os underscore para que ele "ajude" o justify a centralizar melhor isso no visor
        valor_texto.set("------------------____")
        pisca_texto_final()
        estado_calculadora  = "disable"

    for botao in lista_botoes:
        botao.config(state=estado_calculadora)

# Declarando os botões referentes ao números na calculadora
botao_9 = tk.Button(frame_grande, text="9", command=lambda: inserir_valor(9), width=4, height=1, padx=5, pady=5, relief="raised", bg=cores.cinza_claro, fg=cores.preto, font=("Ivy", 10, ""))
botao_8 = tk.Button(frame_grande, text="8", command=lambda: inserir_valor(8), width=4, height=1, padx=5, pady=5, relief="raised", bg=cores.cinza_claro, fg=cores.preto, font=("Ivy", 10, ""))
botao_7 = tk.Button(frame_grande, text="7", command=lambda: inserir_valor(7), width=4, height=1, padx=5, pady=5, relief="raised", bg=cores.cinza_claro, fg=cores.preto, font=("Ivy", 10, ""))
botao_6 = tk.Button(frame_grande, text="6", command=lambda: inserir_valor(6), width=4, height=1, padx=5, pady=5, relief="raised", bg=cores.cinza_claro, fg=cores.preto, font=("Ivy", 10, ""))
botao_5 = tk.Button(frame_grande, text="5", command=lambda: inserir_valor(5), width=4, height=1, padx=5, pady=5, relief="raised", bg=cores.cinza_claro, fg=cores.preto, font=("Ivy", 10, ""))
botao_4 = tk.Button(frame_grande, text="4", command=lambda: inserir_valor(4), width=4, height=1, padx=5, pady=5, relief="raised", bg=cores.cinza_claro, fg=cores.preto, font=("Ivy", 10, ""))
botao_3 = tk.Button(frame_grande, text="3", command=lambda: inserir_valor(3), width=4, height=1, padx=5, pady=5, relief="raised", bg=cores.cinza_claro, fg=cores.preto, font=("Ivy", 10, ""))
botao_2 = tk.Button(frame_grande, text="2", command=lambda: inserir_valor(2), width=4, height=1, padx=5, pady=5, relief="raised", bg=cores.cinza_claro, fg=cores.preto, font=("Ivy", 10, ""))
botao_1 = tk.Button(frame_grande, text="1", command=lambda: inserir_valor(1), width=4, height=1, padx=5, pady=5, relief="raised", bg=cores.cinza_claro, fg=cores.preto, font=("Ivy", 10, ""))
botao_0 = tk.Button(frame_grande, text="0", command=lambda: inserir_valor(0), width=4, height=1, padx=4, pady=4, relief="raised", bg=cores.cinza_claro, fg=cores.preto, font=("Ivy", 10, ""))

# Declarando os botões referentes as operações
botao_soma = tk.Button(frame_grande, text="+",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.prata,fg=cores.preto,font=("Ivy", 10, ""))
botao_subtracao = tk.Button(frame_grande, text="-",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.prata,fg=cores.preto,font=("Ivy", 10, ""))
botao_multiplicacao = tk.Button(frame_grande,text="*",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.prata,fg=cores.preto,font=("Ivy", 10, ""))
botao_divisao = tk.Button(frame_grande, text="÷",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.prata,fg=cores.preto,font=("Ivy", 10, ""))
botao_raiz_quadrada = tk.Button(frame_grande, text="√",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.prata,fg=cores.preto,font=("Ivy", 10, ""))
botao_raiz_cubica = tk.Button(frame_grande, text="∛",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.prata,fg=cores.preto,font=("Ivy", 10, ""))
botao_exponenciacao = tk.Button(frame_grande, text="x^",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.prata,fg=cores.preto,font=("Ivy", 10, ""))
botao_seno = tk.Button(frame_grande, text="sen(x)",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.prata,fg=cores.preto,font=("Ivy", 10, ""))
botao_cosseno = tk.Button(frame_grande, text="cos(x)",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.prata,fg=cores.preto,font=("Ivy", 10, ""))
botao_tangente = tk.Button(frame_grande, text="tan(x)",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.prata,fg=cores.preto,font=("Ivy", 10, ""))

# Declarando os botões básicos
botao_virgula = tk.Button(frame_grande, text=".",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.prata,fg=cores.preto,font=("Ivy", 10, ""))
botao_igual = tk.Button(frame_grande, text="=",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.prata,fg=cores.preto,font=("Ivy", 10, ""))
botao_on_off = tk.Button(frame_grande, text="ON/OFF", relief="raised",bg=cores.magenta, fg=cores.preto,font=("Ivy", 10, ""))
botao_del = tk.Button(frame_grande, text="DEL", relief="raised", bg=cores.prata, fg=cores.preto,font=("Ivy", 10, ""))
botao_reset = tk.Button(frame_grande, text="RESET", relief="raised", bg=cores.prata, fg=cores.preto,font=("Ivy", 10, ""))

#Fazendo uma lista de botões porque vou precisar dela para fazer a função de ligar e  desligar o botão
lista_botoes = [botao_0, botao_1, botao_2, botao_3, botao_4, botao_5, botao_6, botao_7, botao_8, botao_9, 
                botao_soma, botao_subtracao, botao_multiplicacao, botao_divisao, botao_exponenciacao, botao_raiz_cubica, 
                botao_raiz_quadrada, botao_del, botao_reset, botao_virgula, botao_igual, botao_seno, botao_cosseno, botao_tangente]

# Posicionando o lugar que cada botão vai ficar (NÃO DEFINIDO A FUNÇÃO E NEM O TAMANHO DO BOTÃO)

#Posição dos números
#Padx e Pady definem o espaçamento interno dos botões
botao_9.grid(row=3, column=3, padx=1, pady=1, sticky="nsew")
botao_8.grid(row=3, column=2, padx=1, pady=1, sticky="nsew")
botao_7.grid(row=3, column=1, padx=1, pady=1, sticky="nsew")
botao_6.grid(row=4, column=3, padx=1, pady=1, sticky="nsew")
botao_5.grid(row=4, column=2, padx=1, pady=1, sticky="nsew")
botao_4.grid(row=4, column=1, padx=1, pady=1, sticky="nsew")
botao_3.grid(row=5, column=3, padx=1, pady=1, sticky="nsew")
botao_2.grid(row=5, column=2, padx=1, pady=1, sticky="nsew")
botao_1.grid(row=5, column=1, padx=1, pady=1, sticky="nsew")
botao_0.grid(row=6, column=1,columnspan=3,sticky="we",padx=1,pady=1)

#Posição dos botões de operações matemáticas
botao_soma.grid(row=5, column=5, padx=1, pady=1,sticky="nsew")
botao_subtracao.grid(row=5, column=6,padx=1, pady=1, sticky="nsew")
botao_multiplicacao.grid(row=4, column=5, padx=1, pady=1, sticky="nsew")
botao_divisao.grid(row=4, column=6, padx=1, pady=1, sticky="nsew")
botao_raiz_quadrada.grid(row=5, column=7, padx=1, pady=1, sticky="nsew")
botao_raiz_cubica.grid(row=4, column=7, padx=1, pady=1, sticky="nsew")
botao_exponenciacao.grid(row=6, column=7, padx=1, pady=1, sticky="nsew")

#Posição das operações trigonométricas
botao_seno.grid(row=3, column=5, padx=1, pady=1, sticky="nsew")
botao_cosseno.grid(row=3, column=6, padx=1, pady=1,sticky="nsew")
botao_tangente.grid(row=3, column=7, padx=1, pady=1, sticky="nsew")

#Posição do botão de igual
botao_igual.grid(row=6, column=5, padx=1, pady=1,sticky="nsew")

#Posição do botão de vírgula
botao_virgula.grid(row=6, column=6, padx=1, pady=1,sticky="nsew")

#Posição do botão que ligar/desligar
botao_on_off.grid(row=1, column=7)

#Posição dos botão reset
botao_reset.grid(row=1, column=6)

#Posição do botão del
botao_del.grid(row=1, column=5, sticky="nsew")

#Configurando os botões das operações matemáticas
botao_multiplicacao.config(command=lambda: inserir_operacao("*"))
botao_exponenciacao.config(command=lambda: inserir_operacao("x^"))
botao_subtracao.config(command=lambda: inserir_operacao("-"))
botao_divisao.config(command=lambda: inserir_operacao("÷"))
botao_soma.config(command=lambda: inserir_operacao("+"))

#Configurando os botões das operações unárias (Tem que ser uma função diferente das básicas porque elas precisam só de um número)
botao_tangente.config(command=lambda: calcula_operacoes_unarias("tan(x)"))
botao_raiz_quadrada.config(command=lambda: calcula_operacoes_unarias("√"))
botao_cosseno.config(command=lambda: calcula_operacoes_unarias("cos(x)"))
botao_raiz_cubica.config(command=lambda: calcula_operacoes_unarias("∛"))
botao_seno.config(command=lambda: calcula_operacoes_unarias("sen(x)"))

#Configurando o botão de igual
botao_igual.config(command=calcular)

#Configurando o botão da vírgula
botao_virgula.config(command=inserir_virgula)

#Configurando o botão DEL
botao_del.config(command=deletar_caractere)

#Configurando o botão RESET
botao_reset.config(command=resetar)

#Configurando o botão de ligar e desligar
botao_on_off.config(command=liga_desliga)

calculadora.mainloop() #Executa a página
