import random

jogadas=["","Pedra","Papel","Tesoura"]

while(True):
    continuar= input("deseja jogar joquempo novamente? (s/n)")
    if continuar == "s":
        pass
    elif continuar == "n":
        break
    else:
        print("digite apenas s para sim  ou n para nao")
        print("-="*11)
        continue
        
    while (True):
        jogador=input(f"Use os numeros de 1 a 3 para fazer sua jogada: \n 1.Pedra \n 2.Papel \n 3.Tesoura \n ")
        if jogador.isnumeric(): 
            jogador=int(jogador)
            if jogador > 0 and  jogador < 4:
                break
            else:
                print("digite um numero valido")
                print("-="*11)
                continue
        else:
            print("digite um numero valido")
            print("-="*11)
            continue

    npc= random.randint(1,3)

    npc_jogada=jogadas[npc]
    jogador_jogada=jogadas[jogador]



    if  npc_jogada == "Pedra":
        if jogador_jogada == "Pedra":
            print(F"Você escolheu {jogador_jogada}, e o npc escolheu {npc_jogada}, foi por pouco, porem deu empate")
            print("-="*11)
        elif jogador_jogada == "Papel":
            print(F"Você escolheu {jogador_jogada}, e o npc escolheu {npc_jogada}, parabéns você ganhou ")
            print("-="*11)
        else:
            print(F"Você escolheu {jogador_jogada}, e o npc escolheu {npc_jogada}, que pena, você perdeu mais sorte na próxima ")
            print("-="*11)

    if npc_jogada == "Papel":
        if jogador_jogada == "Pedra":
            print(F"Você escolheu {jogador_jogada}, e o npc escolheu {npc_jogada}, que pena, você perdeu mais sorte na próxima")
            print("-="*11)
        elif jogador_jogada == "Papel":
            print(F"Você escolheu {jogador_jogada}, e o npc escolheu {npc_jogada}, foi por pouco, porem deu empate")
            print("-="*11)
        else:
            print(F"Você escolheu {jogador_jogada}, e o npc escolheu {npc_jogada}, parabéns você ganhou ")
            print("-="*11)

    if npc_jogada == "Tesoura":
        if jogador_jogada == "Pedra":
            print(F"Você escolheu {jogador_jogada}, e o npc escolheu {npc_jogada}, parabéns você ganhou")
            print("-="*11)
        elif jogador_jogada == "Papel":
            print(F"Você escolheu {jogador_jogada}, e o npc escolheu {npc_jogada}, que pena, você perdeu mais sorte na próxima")
            print("-="*11)
        else:
            print(F"Você escolheu {jogador_jogada}, e o npc escolheu {npc_jogada}, foi por pouco, porem deu empate ")
            print("-="*11)