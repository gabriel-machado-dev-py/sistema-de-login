# Sistema de Login com Interface Gráfica e Banco de Dados 🤖

## Descrição do projeto 📋

Este é um projeto em python criado para ser um **Sistema de login** para registro de usuários.

## Funcionalidades ⚙️

1. **Registro de usuários:**

   * Permite que novos usuários se registrem com um nome de usuário, email e senha
   * Permite que o usuário veja sua senha
   * Armazena o nome de usuário e a senha criptografada no banco de dados SQLite.

2. **Login de Usuários:**

   * Permite faça login com suas credenciais (nome de usuário e
     senha).
   * Verifica as credenciais no banco de dados SQLite.
   * Permite que o usuário veja sua senha

3. **Banco de Dados:**

   * Integrado com criação e validação de usuário e senha
   * Criptografia de senha(hashlib)

## Estrutura de pastas 🧱

/graphic_interface.py  # Código-fonte principal da aplicação
/astronauta.png        # Imagem da aplicação
/requirements.txt      # Tecnologias hospedadas para instalação


# Tecnologias utilizadas 💻

- **customtkinter**: Ambiente para criação da interface gráfica
- **tkinter**: Usado para algumas funcionalidades no projeto como: messagebox
- **sqlite3**: Banco de dados usado no projeto
- **hashlib**: Usado para criptografar a senha, dando mais segurança

## Configuração para Desenvolvedores 🔧

### Requisitos

- Python 3.x 🐍
- Bibliotecas: `customtkinter`, `tkinter`, `sqlite3`

### Instalação das Dependências

1. Clone o repositório:

   ```bash
   git clone https://github.com/gabriel-machado-dev-py/sistema-de-login.git
   ```

2. Configure um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   # No Linux use `source venv/bin/activate`
   # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências usando o arquivo requirements.txt:

   ```bash
   pip install -r requirements.txt

   ```
## Executável

-> Baixe mysetup.exe



## Licença 📝

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
