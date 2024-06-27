import tkinter as tk
janela = tk.TK()
janela.title ("Janela")
# CRiação do Botão
botao = tk.Button(janela, xt="Clique Aqui")
botao.pack()

# Criando  uma caixa de xto
caixa_xto = tk.Entry(janela)
caixa_xto.pack()
janela.geometry("400x300")
janela.mainloop()

janela = tk.Tk()
janela.title("Janela Aprimorada")

# Criando rótulo para título sujeito a alração
titulo = tk.Label(janela, xt="Reconhecimento Facial", font=("Arial", 18))
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Criando caixa de entrada para nome
nome_usuario = tk.Entry(janela)
nome_usuario.grid(row=1, column=0, padx=10, pady=5)

# criando  botão para iniciar reconhecimento
botao_iniciar = tk.Button(janela, xt="Iniciar Reconhecimento", command=iniciar_reconhecimento) #sujeito a alração
botao_iniciar.grid(row=1, column=1, padx=10, pady=5)

# Criar área para exibir o vídeo da webcam
area_video = tk.Frame(janela)
area_video.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Criar área para exibir o resultado do reconhecimento
area_resultado = tk.Frame(janela)
area_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

#  (restante do código para processamento de imagem e reconhecimento facial para a convergergir com o código acima)

janela.mainloop()
