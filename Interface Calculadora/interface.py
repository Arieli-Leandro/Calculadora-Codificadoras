import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora Codificadoras")

#Botões referentes ao números na calculadora
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

#Botões referentes as operações
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


#Botões básicos
botao_virgula = tk.Button(janela, text="∙")
botao_parenteses_esquerdo = tk.Button(janela, text="(")
botao_parenteses_direito = tk.Button(janela, text=")")
botao_igual = tk.Button(janela, text="=")
botao_on_off = tk.Button(janela, text="ON/OFF")
botao_del = tk.Button(janela, text="DEL")
botao_reset = tk.Button(janela, text="RESET")






botao_9.grid(row=10, column=0)


janela.mainloop()







