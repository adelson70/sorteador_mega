# Importando bibliotecas
import tkinter as tk
from tkinter.font import Font
from random import sample

numeros = [n for n in range(1,61)]


#  Função para escolher os números
def escolher_numeros(data):
    lista_numeros_sortidos = sample(data,6)
    lista_numeros_sortidos.sort(reverse=False)
    str_numeros_sortidos = ""

    for n in lista_numeros_sortidos:
        n = str(n)

        str_numeros_sortidos += f" {n}"

    #print(type(str_numeros_sortidos))

    atualizar_label(str_numeros_sortidos)

# Função para atualizar a label dos números sortidos que ira aparecer na GUI
def atualizar_label(texto):
    global label_numeros_sortidos

    label_numeros_sortidos.config(text=texto)
    janela_principal.update


# Função para ajustar a janela principal conforme o conteudo que estiver nela
def ajustar_janela_ao_conteudo(root):
    root.update_idletasks()  # Atualiza a geometria da janela
    largura = root.winfo_reqwidth()  # Largura requisitada pelo conteúdo
    altura = root.winfo_reqheight()  # Altura requisitada pelo conteúdo

    # Obtém as dimensões da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calcula a posição para centralizar a janela
    x_pos = (largura_tela - largura) // 2
    y_pos = (altura_tela - altura) // 2

    # Define a geometria da janela
    root.geometry(f"{largura+166}x{altura}+{x_pos-50}+{y_pos-120}")

# Main da Janela
janela_principal = tk.Tk()

# Fontes personalizadas
fonte_titulo = Font(family="Segoe UI", size=15, weight="bold")
fonte_numeros = Font(family="Segoe UI", size=20, weight="bold")

# Titulo da Janela Principal
janela_principal.title('Sorteador da Mega da Virada')

# label titulo
label_titulo = tk.Label(janela_principal, text='Mega da Virada', font=fonte_titulo).pack(pady=5)

# label dos números
label_numeros_sortidos = tk.Label(janela_principal,text='',font=fonte_numeros)
label_numeros_sortidos.pack(pady=10)

# Botão para chamar a função de gerar os números
tk.Button(janela_principal, text='Gerar Números', font=fonte_titulo, command=lambda: escolher_numeros(numeros)).pack(pady=10)

ajustar_janela_ao_conteudo(janela_principal)
janela_principal.mainloop()