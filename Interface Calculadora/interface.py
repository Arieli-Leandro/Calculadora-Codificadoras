#Bibliotecas
import tkinter as tk
from tkinter import *
import paleta_de_cores as cores
#import funcoes_calculadora as funcoes_matematicas

calculadora = tk.Tk() #Define a janela
calculadora.title("Calculadora") #Coloca o título da página

#Opção 1 - logo sem cor
#Coloca o ícone da página
#calculadora.iconbitmap("imagens/logo-sem-cor.ico") 

#Opção 2 - Logo com cor
#Coloca o ícone da página
calculadora.iconbitmap("imagens/logo-com-fundo.ico") 

#Define o tamanho da janela
calculadora.geometry("350x300") 





#Definindo os frames da Calculadora 
frame_pequeno = Frame(calculadora, width= 350, height=50, bg=cores.cinza_escuro)
frame_pequeno.grid(row=0, column=0)


frame_grande = Frame(calculadora, width= 250, height=268)
frame_grande.grid(row=1, column=0, sticky="w")

#Adicionando uma coluna invisível para separar os números das operações
frame_grande.columnconfigure(4, minsize=3)
frame_grande.rowconfigure(0, minsize=7)
frame_grande.rowconfigure(2, minsize=7)


valor_texto =StringVar()

visor_calculadora = Label(frame_pequeno, textvariable=valor_texto, width=16, height=2, padx=7, anchor='e', relief= FLAT, justify=RIGHT, font='Ivy 18',bg=cores.cinza_escuro, fg=cores.branco)
visor_calculadora.place(x=0, y=0)


#Funções das operações matemáticas


# Declarando os botões referentes ao números na calculadora
botao_9 = tk.Button(frame_grande, text="9",width=4,height=1,padx=5,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_8 = tk.Button(frame_grande, text="8",width=4,height=1,padx=5,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_7 = tk.Button(frame_grande, text="7",width=4,height=1,padx=5,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_6 = tk.Button(frame_grande, text="6",width=4,height=1,padx=5,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_5 = tk.Button(frame_grande, text="5",width=4,height=1,padx=5,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_4 = tk.Button(frame_grande, text="4",width=4,height=1,padx=5,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_3 = tk.Button(frame_grande, text="3",width=4,height=1,padx=5,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_2 = tk.Button(frame_grande, text="2",width=4,height=1,padx=5,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_1 = tk.Button(frame_grande, text="1",width=4,height=1,padx=5,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_0 = tk.Button(frame_grande, text="0",width=4,height=1,padx=4,pady=4,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))

# Declarando os botões referentes as operações
botao_soma = tk.Button(frame_grande, text="+",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_subtracao = tk.Button(frame_grande, text="-",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_multiplicacao = tk.Button(frame_grande,text="*",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_divisao = tk.Button(frame_grande, text="÷",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_raiz_quadrada = tk.Button(frame_grande, text="√",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_raiz_cubica = tk.Button(frame_grande, text="∛",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_exponenciacao = tk.Button(frame_grande, text="x^",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_seno = tk.Button(frame_grande, text="sen(x)",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_cosseno = tk.Button(frame_grande, text="cos(x)",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_tangente = tk.Button(frame_grande, text="tan(x)",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))

# Declarando os botões básicos
botao_virgula = tk.Button(frame_grande, text=",",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_igual = tk.Button(frame_grande, text="=",width=4,height=1,padx=3,pady=5,relief="raised",bg=cores.cinza_claro,fg=cores.preto,font=("Ivy", 10, ""))
botao_on_off = tk.Button(frame_grande, text="ON/OFF", relief="raised", fg=cores.preto,font=("Ivy", 10, ""))
botao_del = tk.Button(frame_grande, text="DEL", relief="raised", fg=cores.preto,font=("Ivy", 10, ""))
botao_reset = tk.Button(frame_grande, text="RESET", relief="raised", fg=cores.preto,font=("Ivy", 10, ""))

# Posicionando o lugar que cada botão vai ficar (NÃO DEFINIDO A FUNÇÃO E NEM O TAMANHO DO BOTÃO)

#Posição do botão que ligar/desligar
botao_on_off.grid(row=1, column=7)

#Posição dos botão reset
botao_reset.grid(row=1, column=6)

#Posição do botão del
botao_del.grid(row=1, column=5, sticky="nsew")

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



calculadora.mainloop() #Executa a página
