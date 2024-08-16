import tkinter as tk
from tkinter import ttk

# Função para atualizar (Nome e Escolhas do usuário)
def atualizar_resultado():
    # Obter um nome usuario
    nome = caixa_texto.get()

    #Obter preferencias bebida "Radio"
    preferencia = var_radio.get()

    # Verificar tipo de saudação marcada "CheckBox"
    
    #Formal
    if var_check_saudacao.get():
        saudacao = "Olá"
    else:
        saudacao = f"{saudacao }, caro(a)"


# janela principal
janela = tk.tk()
janela.title("Interface Avançada")
janela.geometry("400x500")

# Criar caixa entrada 
label_nome = tk.Label(janela, text="Digite seu nome: ")
label_nome.pack(pady=5)
caixa_texto = tk.Entry(janela, width=40)
caixa_texto.pack(pady=5)

# Criar botões de rádio
label_preferencia = tk.label(janela, text="Digite sua preferencia :")
label_preferencia.pack(pady=5)
var_radio = tk.StringVar(value="Agua")
radio_Cafe= tk.Radiobutton(janela, text="Café", variable=var_radio,value="Café")

radio_Chá= tk.Radiobutton(janela, text="Chá", variable=var_radio,value="Chá")

radio_Suco= tk.Radiobutton(janela, text="Suco", variable=var_radio,value="Suco")

radio_Agua= tk.Radiobutton(janela, text="Agua", variable=var_radio,value="Agua")

radio_Cafe.pack()
radio_Chá.pack()
radio_Suco.pack()
radio_Agua.pack()

# Criar Caixas de seleção "CheckBox"
var_check_saudacao = tk.BooleanVar

check_saudacao = tk.Checkbutton(janela, text="usar saudação informal", variable=var_check_saudacao)
check_saudacao.pack(pady=5)

var_check_personalizada = tk.BooleanVar
check_personalizada = tk.Checkbutton(janela, text="usar saudação personalizada", variable=var_check_personalizada)
var_check_personalizada.pack(pady=5)

# Lista de opções "ComboBox"
label_cor = tk.Label(janela, text="Digite sua cor favorita: ")
label_cor.pack(pady=5)
combo_cor = ttk.Combobox(janela, values={"Vermelho" "Azul" "Verde" "Amarelo" "Preto" "Branco" })
combo_cor.pack(pady=5)

# Criar botões 
botao_atualizar = tk.Button(janela, text="Atualizar")
botao_atualizar.pack(pady=10)

botao_limpar = tk.Button(janela, text="Limpar")
botao_limpar.pack(pady=10)

# Criar um rótulo para mostrar o resultado "Label"
label_resultado = tk.Label(janela, text="", wraplength=350)
label_resultado.pack(pady=10)








# Executar a janela principal
janela.mainloop()