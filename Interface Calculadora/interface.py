import tkinter as tk

janela = tk.Tk() #Define a janela
janela.title("Calculadora Codificadoras") #Coloca o título da página

# Declarando os botões referentes ao números na calculadora
botao_9 = tk.Button(janela, text="9")
botao_8 = tk.Button(janela, text="8")
botao_7 = tk.Button(janela, text="7")
botao_6 = tk.Button(janela, text="6")
botao_5 = tk.Button(janela, text="5")
botao_4 = tk.Button(janela, text="4")
botao_3 = tk.Button(janela, text="3")
botao_2 = tk.Button(janela, text="2")
botao_1 = tk.Button(janela, text="1")
botao_0 = tk.Button(janela, text="0")

# Declarando os botões referentes as operações
botao_soma = tk.Button(janela, text="+")
botao_subtracao = tk.Button(janela, text="-")
botao_multiplicacao = tk.Button(janela, text="*")
botao_divisao = tk.Button(janela, text="÷")
botao_raiz_quadrada = tk.Button(janela, text="√")
botao_raiz_cubica = tk.Button(janela, text="∛")
botao_exponenciacao = tk.Button(janela, text="x^")
botao_seno = tk.Button(janela, text="sen(x)")
botao_cosseno = tk.Button(janela, text="cos(x)")
botao_tangente = tk.Button(janela, text="tan(x)")
botao_pi = tk.Button(janela, text="π")


# Declarando os botões básicos
botao_virgula = tk.Button(janela, text=",")
botao_parenteses_esquerdo = tk.Button(janela, text="(")
botao_parenteses_direito = tk.Button(janela, text=")")
botao_igual = tk.Button(janela, text="=")
botao_on_off = tk.Button(janela, text="ON/OFF")
botao_del = tk.Button(janela, text="DEL")
botao_reset = tk.Button(janela, text="RESET")


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



janela.mainloop() #Executa a página
