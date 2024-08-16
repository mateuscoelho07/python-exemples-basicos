import tkinter as tk 

# Função para transferir texto so input para label
def mostrar_mensagem():
    texto = caixa_texto.get() # Obter o texto da caixa texto
    label_resultado.config(text=texto) # Atualiza o texto do label 

# Janela principal
janela = tk.Tk()
janela.title("Exemplo de interface")
janela.geometry("400x150")

# criar uma caixa de texto para entrada 
caixa_texto = tk.Entry(janela, width=50)
caixa_texto.pack(pady=10)

# Criar um botão
botao = tk.Button(janela, text= "Mostrar texto" , command=mostrar_mensagem)
botao.pack(pady=5)

#Criar Rotulo para mostrar o resultado "Label"
label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

# Executar a janela principal
janela.mainloop()