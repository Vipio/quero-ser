j1 = input("escolha do jogador 1: ")
j2 = input("escolha do jogador 2: ")


if j2 == "papel" and j1 == "pedra":
    print("Jogador 2 GANHOU")
elif j2 == "tesoura" and j1 == "pedra":
    print("Jogador 1 GANHOU")
elif j1 == "papel" and j2 == "pedra":
    print("Jogador 1 GANHOU")
elif j1 == "tesoura" and j2 == "pedra":
    print("Jogador 2 GANHOU")    
else:
    print("empate")
        
