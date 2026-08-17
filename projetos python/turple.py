tuple = ("domingo","segunda", "terça", "quarta", "quinta", "sexta", "sabado")

dia = int (input("DIgite o número do dia da semana 1 a 7: "))

if dia == 1:
    print(f"seu dia é {tuple[0]}")
elif dia == 2:
    print(f"seu dia é {tuple[1]}")
elif dia == 3:
    print(f"seu dia é {tuple[2]}")
elif dia == 4:
    print(f"seu dia é {tuple[3]}")
elif dia == 5:
    print(f"seu dia é {tuple[4]}")
elif dia == 6:
    print(f"seu dia é {tuple[5]}")
elif dia == 7:
    print(f"seu dia é {tuple[6]}")
else:
    print("Vc n digitou nenhum número")