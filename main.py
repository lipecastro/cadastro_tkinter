import tkinter as tk
from tkinter import messagebox

def cadastrar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()

    if nome and email:
        with open("usuarios.txt", "a") as file:
            file.write(f"Nome: {nome}, Email: {email}\n")
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

def fazer_login():
    nome = entry_nome_login.get()
    email = entry_email_login.get()

    with open("usuarios.txt", "r") as file:
        usuarios = file.read()

    if f"Nome: {nome}, Email: {email}\n" in usuarios:
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Erro", "Usuário não encontrado.")

# janela
window = tk.Tk()
window.title("Cadastro e Login de Usuário")

# Login
label_login = tk.Label(window, text="Login")
label_login.pack()

label_nome_login = tk.Label(window, text="Nome:")
label_nome_login.pack()
entry_nome_login = tk.Entry(window)
entry_nome_login.pack()

label_email_login = tk.Label(window, text="Email:")
label_email_login.pack()
entry_email_login = tk.Entry(window)
entry_email_login.pack()

btn_login = tk.Button(window, text="Login", command=fazer_login)
btn_login.pack()

label_nao_cadastro = tk.Label(window, text="Não possui cadastro?")
label_nao_cadastro.pack()


btn_cadastrar = tk.Button(window, text="Cadastrar", command=lambda: show_frame(cadastro_frame))
btn_cadastrar.pack()

# Tela de cadastro
cadastro_frame = tk.Frame(window)

label_cadastro = tk.Label(cadastro_frame, text="Cadastro de Usuário")
label_cadastro.pack()

label_nome = tk.Label(cadastro_frame, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(cadastro_frame)
entry_nome.pack()

label_email = tk.Label(cadastro_frame, text="Email:")
label_email.pack()
entry_email = tk.Entry(cadastro_frame)
entry_email.pack()

btn_cadastrar = tk.Button(cadastro_frame, text="Cadastrar", command=cadastrar_usuario)
btn_cadastrar.pack()


def show_frame(frame):
    cadastro_frame.pack_forget()  
    frame.pack()  

# Iniciar 
window.mainloop()
