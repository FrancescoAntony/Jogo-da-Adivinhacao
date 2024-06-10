import random

def jogo_adivinhação():
    # Gerar um número aleatório entre 1 e 10
    numero = random.randint(1, 10)
    tentativas = 0
    adivinhou = True

    print("Robô: Bem vindo ao jogo da advinhação!")
    print("Robô: Eu escolhi um número entre 1 e 10. Tenta adivinhar.")

    while adivinhou:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero:
            print("Seu palpite é menor do que o número secreto. Tente novamente.")
        elif palpite > numero:
            print("Seu palpite é maior do que o número secreto. Tente novamente")
        else: 
            adivinhou = True
            print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")

jogo_adivinhação()
