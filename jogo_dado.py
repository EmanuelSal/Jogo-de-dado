# Projetos

import random

nome = input("Qual é o seu nome? ")
print()
resposta = input(f"Olá {nome}, você gostaria de jogar o dado? ")

if resposta.lower() == "sim":
    while True:
        valor = random.randint(1, 6)
        print()
        print(f"ESSE FOI SEU O NÚMERO DO SEU DADO: {valor}", "\n")
        resposta_2 = input(f"{nome}, gostaria de continuar? ")
        if resposta_2 == "nao": break
    
    print()
    print(f"OBRIGADO POR BRINCAR UM POUCO COM NÓS. VOLTE SEMPRE!! \U0001f600") # \U0001f600 => emoji de sorriso

elif resposta.lower() == "nao":print(), print("Obrigado pela participação! \U0001f600")
