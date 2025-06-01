# Criar o tabuleiro vazio
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro():
    print("  0   1   2")
    for i, linha in enumerate(tabuleiro):
        print(i, " | ".join(linha))
        if i < 2:
            print("  ---------")

def jogada(simbolo, nome_jogador):
    while True:
        try:
            linha = int(input(f"{nome_jogador} ({simbolo}), digite a linha (0, 1 ou 2): "))
            coluna = int(input(f"{nome_jogador} ({simbolo}), digite a coluna (0, 1 ou 2): "))
            if linha in [0, 1, 2] and coluna in [0, 1, 2]:
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = simbolo
                    break
                else:
                    print("Essa posição já está ocupada. Tente outra.")
            else:
                print("Linha ou coluna inválida. Use 0, 1 ou 2.")
        except ValueError:
            print("Por favor, digite um número válido.")

def verificar_vitoria():
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != " ":
            return linha[0]
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] != " ":
            return tabuleiro[0][col]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]
    for linha in tabuleiro:
        if " " in linha:
            return None
    return "Empate"

# Entrada dos nomes dos jogadores
jogador_1 = input("Digite o nome do Jogador 1 (X): ")
jogador_2 = input("Digite o nome do Jogador 2 (O): ")

jogador_atual = "X"

while True:
    mostrar_tabuleiro()
    if jogador_atual == "X":
        jogada("X", jogador_1)
    else:
        jogada("O", jogador_2)

    resultado = verificar_vitoria()
    if resultado == "X":
        mostrar_tabuleiro()
        print(f"Parabéns! {jogador_1} venceu! 🎉")
        break
    elif resultado == "O":
        mostrar_tabuleiro()
        print(f"Parabéns! {jogador_2} venceu! 🎉")
        break
    elif resultado == "Empate":
        mostrar_tabuleiro()
        print("Deu empate! Ninguém venceu. 🤝")
        break

    jogador_atual = "O" if jogador_atual == "X" else "X"
