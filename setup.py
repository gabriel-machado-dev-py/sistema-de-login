from cx_Freeze import setup, Executable
import sys

files = ["astronauta.png", "robot.ico"]

base = None
if sys.platform == "win32":
    base = "Win32GUI"

Executable(
    script="graphic_interface.py",
    base="Win32GUI",
    icon="robot.ico"
  )

setup(
  
  name = "Sistema de login",
  version = "1.0",
  description = "Sistema onde o usuário pode cadastrar e logar",
  author = "Gabriel Machado",
  executables = [Executable("graphic_interface.py", base=base, icon="robot.ico")],
  options = {
    "build_exe": {
      "packages": ["tkinter", "sqlite3", "customtkinter"],
      "include_files": files,
      "include_msvcr": True
    }
  }
)