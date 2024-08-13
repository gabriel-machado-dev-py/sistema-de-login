import customtkinter as tk
from tkinter import PhotoImage
import sqlite3

class App(tk.CTk):
    def __init__(self):
        super().__init__()
        self.configuracao_da_janela_inicial()
        self.tela_de_login()
        
    """
    Configuração da janela principal
    """
    def configuracao_da_janela_inicial(self):
        self.title("Sistema de Login")
        self.geometry("720x400")
        self.resizable(False, False)
    
    """
    Configuração da tela de login
    
    1. Configuração da imagem de fundo
    2. Configuração do formulário de login
    """
    def tela_de_login(self):
      # Configuração da imagem de fundo
      self.img = PhotoImage(file="astronauta.png")
      self.img = self.img.subsample(6)
      self.lb_img = tk.CTkLabel(self, text=None, image=self.img)
      self.lb_img.grid(row=1, column=0, padx=10)

      # Titulo sob imagem de fundo
      self.title = tk.CTkLabel(self, text="Faça seu login ou Cadastra-se", font=("Century Gothic", 18, "bold"))
      self.title.grid(row=0, column=0, pady=10)
      
      # Configuração do formulário de login
      self.frame_login = tk.CTkFrame(self, width=350, height=380)
      self.frame_login.place(x=350, y=10)
      
      # Colocando os widgets dentro do frame - Formulário de login
      self.lb_title = tk.CTkLabel(self.frame_login, text="Faça seu login", font=("Century Gothic", 22, "bold"))
      self.lb_title.grid(row=0, column=0, padx=10, pady=10)
      
      # Campo Usuário 
      self.user_name = tk.CTkEntry(self.frame_login, width=300, placeholder_text="Digite seu nome de usuário", font=("Century Gothic bold", 16, "bold"), corner_radius=15)
      self.user_name.grid(row=1, column=0, padx=10, pady=10)
      
      # Campo Senha
      self.password = tk.CTkEntry(self.frame_login, width=300, placeholder_text="Digite sua senha", font=("Century Gothic bold", 16, "bold"), show="*", corner_radius=15)
      self.password.grid(row=2, column=0, padx=10, pady=10)
      
      # Mostrar senha
      self.show_password = tk.CTkCheckBox(self.frame_login, text="Clique para ver a senha", font=("Century Gothic", 12))
      self.show_password.grid(row=3, column=0, padx=10, pady=10)
      
      # Botões de ação - Login e Cadastro
      self.btn_login = tk.CTkButton(self.frame_login, width=300, text="Fazer login".upper(), font=("Century Gothic bold", 16, "bold"), corner_radius=15, fg_color="#9370DB")
      self.btn_login.grid(row=4, column=0, padx=10, pady=10)
      
      # Botões de ação - Login e Cadastro
      self.span = tk.CTkLabel(self.frame_login, text="Não tem uma conta? Clique aqui para se cadastrar", font=("Century Gothic bold", 12))
      self.span.grid(row=5, column=0, padx=10, pady=10)
        
      self.btn_signup = tk.CTkButton(self.frame_login, width=30, text="Cadastre-se".upper(), font=("Century Gothic bold", 14, "bold"), corner_radius=15, fg_color="#099", hover_color="#099666")
      self.btn_signup.grid(row=6, column=0, padx=10, pady=10)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()