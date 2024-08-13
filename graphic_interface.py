import customtkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3


class BackEnd():
    """
    Configuração do banco de dados
    1. Conexão com o banco de dados
    2. Desconexão do banco de dados
    3. Criação da tabela
    4. Cadastro de usuários
    """
    def conect_db(self):
        self.conn = sqlite3.connect("Sistema_de_login.db")
        self.cursor = self.conn.cursor()
         
    def desconect_db(self):
        self.conn.close()
        print("Banco de dados desconectado")
        
    def criar_tabela(self):
        self.conect_db()
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                confirm_password TEXT NOT NULL
            )       
            """)
        self.conn.commit()
        print("Tabela criada com sucesso")
        self.desconect_db()
    
    def cadastrar_usario(self):
        self.username_entry = self.user_name_cadastro.get()
        self.email_entry = self.user_email_cadastro.get()
        self.password_entry = self.password_cadastro.get()
        self.confir_password_entry = self.confirm_password_cadastro.get()
        
        self.conect_db()
        
        self.cursor.execute("""
                            INSERT INTO Usuarios(user, email, password, confirm_password)
                            VALUES (?, ?, ?, ?)
                            """, (self.username_entry, self.email_entry, self.password_entry, self.confir_password_entry))
        try: 
            if (self.username_entry == "" or self.email_entry == "" or self.password_entry == "" or self.confir_password_entry == ""):
                messagebox.showerror(title="Sistema de login", message="Por favor preencha todos os campos!")
                
            elif (len(self.username_entry) < 6):
                messagebox.showwarning(title="Sistema de login", message="O nome do usuário precisa ter no mínimo 6 caracteres")
            
            elif (len(self.password_entry) < 6):
                messagebox.showwarning(title="Sistema de login", message="O nome do usuário precisa ter no mínimo 6 caracteres")
                
            elif (self.password_entry != self.confir_password_entry):
                messagebox.showerror(title="Sistema de login", message="As senhas não coicidem!")
                
            else:
                self.conn.commit()
                messagebox.showinfo(title="Sistema de login", message=f"Usuário {self.username_entry} cadastrado!!!")
                
        except:
            messagebox.showerror(title="Sistema de login", message="Erro ao cadastrar o usuário, tente novamente.")
    
class App(tk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.configuracao_da_janela_inicial()
        self.tela_de_login()  
        self.criar_tabela()
          
    """
    Configuração da janela principal
    """  
    def configuracao_da_janela_inicial(self):
        self.title("Sistema de Login")
        self.geometry("720x400")
        self.resizable(False, False)  
        
    """
    Configuração da tela de login
    
    1. Configuração da imagem 
    2. Configuração do formulário de login
        1. Campo de usuario e senha
        2. Botões de login e cadastro
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
      
      # Botão cadastro
      self.btn_signup = tk.CTkButton(self.frame_login, width=30, text="Cadastre-se".upper(), font=("Century Gothic bold", 14, "bold"), corner_radius=15, fg_color="#099", hover_color="#099666", command=self.tela_de_cadastro)
      self.btn_signup.grid(row=6, column=0, padx=10, pady=10)
      
    """
        Configuração da tela de cadastro
        1. Campo de usuario
        2. Campo de email
        3. Campo de senha e confirmar senha
        4. Campo de voltar a tela de login
        """  
    def tela_de_cadastro(self):
        # Remover o formulário de login 
        self.frame_login.place_forget()
        
        # Frame de formulario de cadastro
        self.frame_cadastro = tk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350, y=10)
        
        # Criar os widgets da tela de cadastro
        self.lb_title = tk.CTkLabel(self.frame_cadastro, text="Faça seu cadastro", font=("Century Gothic", 22, "bold"))
        self.lb_title.grid(row=0, column=0, padx=10, pady=5)
        
        # campo usuario
        self.user_name_cadastro = tk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Digite seu nome de usuário", font=("Century Gothic bold", 16, "bold"), corner_radius=15)
        self.user_name_cadastro.grid(row=1, column=0, padx=10, pady=5)
        
        # campo email
        self.user_email_cadastro = tk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Digite seu email", font=("Century Gothic bold", 16, "bold"), corner_radius=15)
        self.user_email_cadastro.grid(row=2, column=0, padx=10, pady=5)
        
        # Campo Senha
        self.password_cadastro = tk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Digite sua senha", font=("Century Gothic bold", 16, "bold"), show="*", corner_radius=15)
        self.password_cadastro.grid(row=3, column=0, padx=10, pady=5)
        # confirma senha
        self.confirm_password_cadastro = tk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Confirme sua senha", font=("Century Gothic bold", 16, "bold"), show="*", corner_radius=15)
        self.confirm_password_cadastro.grid(row=4, column=0, padx=10, pady=5)
        # mostrar senha
        self.show_password = tk.CTkCheckBox(self.frame_cadastro, text="Clique para ver a senha", font=("Century Gothic", 12))
        self.show_password.grid(row=5, column=0, padx=10, pady=5)
        
        # Fazer cadastro
        self.btn_signup_user = tk.CTkButton(self.frame_cadastro, width=300, text="Cadastre-se".upper(), font=("Century Gothic bold", 14, "bold"), corner_radius=15, fg_color="#099", hover_color="#099666", command=self.cadastrar_usario)
        self.btn_signup_user.grid(row=6, column=0, padx=10, pady=5)
        
        # voltar a tela de login
        self.btn_login_back = tk.CTkButton(self.frame_cadastro, width=300, text="Voltar a tela de login".upper(), font=("Century Gothic bold", 12, "bold"), corner_radius=15, fg_color="#9370DB", command=self.tela_de_login)
        self.btn_login_back.grid(row=7, column=0, padx=10, pady=5)
    
    """
    Limpeza dos campos de input da tela de cadastro e login
    
    """    
    def limpa_campo_cadastro(self):
        self.user_name_cadastro.delete(0, END)
        self.user_email_cadastro.delete(0, END)
        self.password_cadastro.delete(0, END)
        self.confirm_password_cadastro.delete(0, END)        
    def limpa_campo_login(self):
        self.user_name.delete(0, END)
        self.password.delete(0, END)
       
if __name__ == "__main__":
    app = App()
    app.mainloop()