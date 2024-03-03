import os


def clear_terminal():
    # Limpa o terminal usando a sequência de escape ANSI
    os.system('cls' if os.name == 'nt' else 'clear')