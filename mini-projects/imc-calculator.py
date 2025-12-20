import tkinter as tk
from tkinter import messagebox

# Cores (definição de paleta para a interface gráfica - dark mode)
BG = "#1e1e1e"
FG = "#ffffff"
BTN_BG = "#2d2d2d"
ENTRY_BG = "#3a3a3a"

# Estrutura geral de um programa Tkinter:
#imports
#↓
#funções (lógica)
#↓
#janela Tk()
#↓
#widgets
#↓
#mainloop()

# -------------------
# FUNÇÕES (LÓGICA)
historico_imc = []
# -------------------
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        classificacao = "Peso normal"
    elif 25 <= imc < 29.9:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 34.9:
        classificacao = "Obesidade grau I"
    elif 35 <= imc < 39.9:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"
    return imc, classificacao

def erro_entry(entry):
    entry.config(bg="#5c1a1a")  # cor de fundo vermelha quando erra

def normal_entry(entry):
    entry.config(bg=ENTRY_BG)  # cor de fundo normal

def calcular():
    nome = entry_nome.get().strip()
    peso_txt = entry_peso.get().replace(',', '.').strip()
    altura_txt = entry_altura.get().replace(',', '.').strip()

    # validar nome
    if not nome:
        messagebox.showerror("Erro", "Por favor, insira seu nome.")
        return

    if nome.isnumeric():
        messagebox.showerror("Erro", "Nome inválido. Use letras.")
        return

    # validar peso
    try:
        peso = float(peso_txt) # converter para float
        if peso <= 0:
            raise ValueError
    except ValueError:
        erro_entry(entry_peso) # destaca o campo com erro
        messagebox.showerror("Erro", "Peso inválido. Use um número maior que zero.") # exibe mensagem de erro(popup)
        return # sai da função se houver erro
    else:
        normal_entry(entry_peso) # restaura a cor normal se não houver erro

    # validar altura
    try:
        altura = float(altura_txt)
        if altura <= 0 or altura > 2.5:
            raise ValueError
    except ValueError:
        erro_entry(entry_altura)
        messagebox.showerror("Erro", "Altura inválida. Exemplo: 1.75")
        return
    else:
        normal_entry(entry_altura)
    # cálculo do IMC
    imc, classificacao = calcular_imc(peso, altura)

    # salvar no histórico
    historico_imc.append({
        "nome": nome,
        "peso": peso,
        "altura": altura,
        "imc": imc,
        "classificacao": classificacao
    })

    resultado_label.config(
        text=f"{nome} | IMC: {imc:.2f} — {classificacao}"
    )

    
def validar_decimal(texto):
    if texto == "":
        return True  # permite apagar tudo
    texto = texto.replace(',', '.')

    # só números e ponto
    if not all(c.isdigit() or c == '.' for c in texto):
        return False

    # só um ponto
    if texto.count('.') > 1:
        return False

    # limitar casas decimais
    if '.' in texto:
        parte_inteira, parte_decimal = texto.split('.', 1)
        if len(parte_decimal) > 2:
            return False

    return True

def mostrar_historico():
    janela_hist = tk.Toplevel(janela) # Cria uma nova janela filha/secundária (toplevel)
    janela_hist.title("Histórico de IMC")

    frame_hist = tk.Frame(janela_hist, padx=20, pady=20)
    frame_hist.pack()

    janela_hist.configure(bg=BG)
    frame_hist.configure(bg=BG)

    titulo = tk.Label(
        frame_hist,
        text="Histórico de IMC",
        font=("Arial", 14, "bold"),
        bg=BG,
        fg=FG
    )

    titulo.pack(pady=10)

    if not historico_imc:
        tk.Label(
            frame_hist,
            text="Nenhum cálculo realizado ainda.",
            bg=BG,
            fg=FG
        ).pack()
        return
    
    for registro in historico_imc:
        texto = (
            f"{registro['nome']} | "
            f"{registro['imc']:.2f} — "
            f"{registro['classificacao']}"
        )
        tk.Label(
            frame_hist,
            text=texto,
            bg=BG,
            fg=FG
        ).pack(anchor="w")


def limpar_historico():
    historico_imc.clear()
    resultado_label.config(text="Histórico limpo com sucesso!!")

# -------------------
# INTERFACE
# -------------------

janela = tk.Tk() #tk = janela principal
vcmd = janela.register(validar_decimal)
janela.title("Calculadora de IMC")

frame = tk.Frame(janela, padx=20, pady=20)
frame.grid()

janela.configure(bg=BG)
frame.configure(bg=BG)

titulo = tk.Label(
    frame,
    text="Calculadora de IMC",
    font=("Arial", 16, "bold"),
    bg=BG,
    fg=FG
)
titulo.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(
    frame,
    text="Nome:",
    bg=BG,
    fg=FG
).grid(row=1, column=0, sticky="e", pady=5)
tk.Label(
    frame,
    text="Altura (m):",
    bg=BG,
    fg=FG
).grid(row=2, column=0, sticky="e", pady=5)

tk.Label(
    frame,
    text="Peso (kg):",
    bg=BG,
    fg=FG
).grid(row=3, column=0, sticky="e", pady=5)

entry_nome = tk.Entry(
    frame,
    bg=ENTRY_BG,
    fg=FG,
    insertbackground=FG
)

entry_altura = tk.Entry(
    frame,
    bg=ENTRY_BG,
    fg=FG,
    insertbackground=FG,
    validate="key",
    validatecommand=(vcmd, "%P"),
)

entry_peso = tk.Entry(
    frame,
    bg=ENTRY_BG,
    fg=FG,
    insertbackground=FG,
    validate="key",
    validatecommand=(vcmd, "%P"),
)
entry_nome.grid(row=1, column=1, pady=5)
entry_altura.grid(row=2, column=1, pady=5)
entry_peso.grid(row=3, column=1, pady=5)

btn_calcular = tk.Button(
    frame,
    text="Calcular IMC",
    command=calcular,
    width=20
)
btn_calcular.grid(row=4, column=0, columnspan=2, pady=10)

btn_historico = tk.Button(
    frame,
    text="Ver Histórico",
    command=mostrar_historico,
    width=20
)
btn_historico.grid(row=5, column=0, columnspan=2, pady=5)

btn_limpar = tk.Button(
    frame,
    text="Limpar Histórico",
    command=limpar_historico,
    width=20
)
btn_limpar.grid(row=6, column=0, columnspan=2, pady=5)

resultado_label = tk.Label(
    frame,
    text="",
    font=("Arial", 11),
    bg=BG,
    fg=FG,
)
resultado_label.grid(row=7, column=0, columnspan=2, pady=10)

janela.mainloop()#mantém a janela aberta até que o usuário a feche
