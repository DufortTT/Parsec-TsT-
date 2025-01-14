import argparse
import time
from pyautogui import write, press, hotkey

def parse_args():
    parser = argparse.ArgumentParser(description="Login automático no Parsec")
    parser.add_argument("--email", required=True, help="E-mail do Parsec")
    parser.add_argument("--password", required=True, help="Senha do Parsec")
    return parser.parse_args()

def login(email, password):
    # Abrir o Parsec
    print("Abrindo o Parsec...")
    hotkey("win", "r")
    write("parsec.exe")
    press("enter")
    time.sleep(5)  # Aguarda o aplicativo carregar

    # Inserir e-mail
    print("Inserindo e-mail...")
    write(email)
    press("tab")

    # Inserir senha
    print("Inserindo senha...")
    write(password)
    press("enter")
    time.sleep(3)

    print("Login concluído com sucesso!")

if __name__ == "__main__":
    args = parse_args()
    login(args.email, args.password)
  
