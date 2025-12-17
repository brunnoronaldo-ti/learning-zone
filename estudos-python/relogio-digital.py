from tkinter import * # Importa a biblioteca Tkinter para criar a interface gráfica
from time import strftime # Importa a função strftime para formatar a hora

# Função para atualizar o relógio
def atualizar_relogio():
    hora_atual = strftime('%H:%M:%S %p') # Formato da hora
    label_relogio.config(text=hora_atual) # Atualiza o texto do rótulo com a hora atual
    label_relogio.after(1000, atualizar_relogio) # Chama a função novamente após 1000 ms (1 segundo)

# Configuração da janela principal
janela = Tk() # Criar a janela principal
janela.title("Relógio Digital") # Título da janela
janela.geometry("300x100") # Tamanho da janela
label_relogio = Label(janela, font=('calibri', 40, 'bold'), background='purple', foreground='white') # Configuração do rótulo do relógio
label_relogio.pack(anchor='center') # Posicionar o rótulo no centro da janela
atualizar_relogio() # Iniciar a atualização do relógio
janela.mainloop() # Iniciar o loop principal da interface gráfica
