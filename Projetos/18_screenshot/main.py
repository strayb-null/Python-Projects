import pyscreenshot as ImageGrab
from datetime import datetime
import os

def tirar_print():
    # Cria uma pasta se não existir
    os.makedirs("screenshots", exist_ok=True)
    
    # Nome do arquivo com data e hora
    nome_arquivo = datetime.now().strftime("screenshots/print_%d-%m-%Y_%H-%M-%S.png")
    
    image = ImageGrab.grab()
    image.save(nome_arquivo)
    print(f"Screenshot salvo como: {nome_arquivo}")

tirar_print()