import customtkinter as ctk

def minimizar():
    # Minimiza a janela
    root.iconify()

# Criação da janela principal
root = ctk.CTk()

# Título da janela
root.title("Minimizar Janela")

# Tamanho da janela
root.geometry("300x200")

# Criação do botão que minimiza a janela
botao_minimizar = ctk.CTkButton(root, text="Minimizar", command=minimizar)
botao_minimizar.pack(pady=20)

# Iniciar o loop da aplicação
root.mainloop()
