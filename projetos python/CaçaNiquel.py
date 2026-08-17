import random
import sys


moeda = 100
ganho = 0
soma = 0

jogar = input(
    "====== Bem-vindo ao jogo do caça-níquel ======\n"
    "Moedas atuais: 100\n\n"
    "Deseja começar a jogar (s/n)?: "
).lower()

if jogar != "s":
    sys.exit()

while moeda > 0:
    coin = int(input("Quanto vc vai apostar?: "))

    if coin > moeda or coin <= 0:
        print("Aposta inválida!")
        continue

    x = random.choice(["🍒", "🍋", "💎"])
    y = random.choice(["🍒", "🍋", "💎"])
    z = random.choice(["🍒", "🍋", "💎"])
    
    print (f"\n{x} | {y} | {z}")

    if x == y == z:
        ganho = coin * 3
        moeda += ganho
        print(f"vc ganhou: {ganho} moedas")
        print(f"moedas atuais: {soma}")

    elif x == y or x == z or y == z:
        ganho = coin * 2
        moeda += ganho
        print(f"vc ganhou: {ganho} moedas")
        print(f"moedas atuais: {soma}")
               
    else:
        moeda = moeda - coin
        print(f"vc perdeu: {coin}")
        print(f"moedas atuais: {soma}")
else:
    moeda -= coin
    print(f"Você perdeu {coin} moedas!")

print("\nGame Over! Você ficou sem moedas.")
           
