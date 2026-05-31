import time
from colorama import Fore, Style, init

init()

# Lista de simulação de leituras de nível de água 
leituras = [1, 2, 3, 4, 5]

def checar_agua(nivel):
    if nivel == 1:
        return "Muito baixo (crítico)", Fore.RED
    elif nivel == 2:
        return "Baixo", Fore.YELLOW
    elif nivel == 3:
        return "Médio", Fore.GREEN
    elif nivel == 4:
        return "Alto", Fore.CYAN
    elif nivel == 5:
        return "Muito alto (alerta)", Fore.BLUE
    else:
        return "Erro", Fore.WHITE

# Execução do monitoramento 
print("--- Controle de Nível de Água ---")

for n in leituras:
    texto, cor = checar_agua(n)

    print(cor + f"Nível {n}: {texto}")

    # Reseta o terminal 
    print(Style.RESET_ALL + "")

    time.sleep(1)



