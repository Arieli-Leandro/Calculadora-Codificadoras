#Bibliotecas
import tkinter as tk
import math

calculadora = tk.Tk() #Define a janela
calculadora.title("Calculadora Codificadoras") #Coloca o título da página
calculadora.iconbitmap("imagens/logo-com-fundo.ico") #Coloca o ícone da página
calculadora.geometry("250x250") #Define o tamanho da janela


#Funções das operações matemáticas
def soma():
    pass

def subtracao():
    pass

def divisao():
    pass

def multiplicacao():
    pass

def exponenciacao():
    pass

def raiz_quadrada():
    pass

def raiz_cubica():
    pass

def seno():
    pass

def cosseno():
    pass

def tangente():
    pass


# Declarando os botões referentes ao números na calculadora
botao_9 = tk.Button(calculadora, text="9")
botao_8 = tk.Button(calculadora, text="8")
botao_7 = tk.Button(calculadora, text="7")
botao_6 = tk.Button(calculadora, text="6")
botao_5 = tk.Button(calculadora, text="5")
botao_4 = tk.Button(calculadora, text="4")
botao_3 = tk.Button(calculadora, text="3")
botao_2 = tk.Button(calculadora, text="2")
botao_1 = tk.Button(calculadora, text="1")
botao_0 = tk.Button(calculadora, text="0")

# Declarando os botões referentes as operações
botao_soma = tk.Button(calculadora, text="+")
botao_subtracao = tk.Button(calculadora, text="-")
botao_multiplicacao = tk.Button(calculadora, text="*")
botao_divisao = tk.Button(calculadora, text="÷")
botao_raiz_quadrada = tk.Button(calculadora, text="√")
botao_raiz_cubica = tk.Button(calculadora, text="∛")
botao_exponenciacao = tk.Button(calculadora, text="x^")
botao_seno = tk.Button(calculadora, text="sen(x)")
botao_cosseno = tk.Button(calculadora, text="cos(x)")
botao_tangente = tk.Button(calculadora, text="tan(x)")

# Declarando os botões básicos
botao_virgula = tk.Button(calculadora, text=",")
botao_parenteses_esquerdo = tk.Button(calculadora, text="(")
botao_parenteses_direito = tk.Button(calculadora, text=")")
botao_igual = tk.Button(calculadora, text="=")
botao_on_off = tk.Button(calculadora, text="ON/OFF")
botao_del = tk.Button(calculadora, text="DEL")
botao_reset = tk.Button(calculadora, text="RESET")

# Posicionando o lugar que cada botão vai ficar (NÃO DEFINIDO A FUNÇÃO E NEM O TAMANHO DO BOTÃO)

#Posição do botão que ligar/desligar
botao_on_off.grid(row=1, column=6)

#Posição dos botão reset
botao_reset.grid(row=2, column=6)

#Posição do botão del
botao_del.grid(row=2, column=5)

#Posição das operações trigonométricas
botao_seno.grid(row=2, column=1)
botao_cosseno.grid(row=2, column=2)
botao_tangente.grid(row=2, column=3)

#Posição dos números
botao_9.grid(row=3, column=3)
botao_8.grid(row=3, column=2)
botao_7.grid(row=3, column=1)
botao_6.grid(row=4, column=3)
botao_5.grid(row=4, column=2)
botao_4.grid(row=4, column=1)
botao_3.grid(row=5, column=3)
botao_2.grid(row=5, column=2)
botao_1.grid(row=5, column=1)
botao_0.grid(row=6, column=1)

#Posição dos botões de operações matemáticas
botao_soma.grid(row=4, column=4)
botao_subtracao.grid(row=4, column=5)
botao_multiplicacao.grid(row=3, column=4)
botao_divisao.grid(row=3, column=5)
botao_raiz_quadrada.grid(row=4, column=6)
botao_raiz_cubica.grid(row=3, column=6)
botao_exponenciacao.grid(row=5, column=6)

#Posição do botão de igual
botao_igual.grid(row=5, column=4)

#Posição do botão de vírgula
botao_virgula.grid(row=5, column=5)



calculadora.mainloop() #Executa a página







