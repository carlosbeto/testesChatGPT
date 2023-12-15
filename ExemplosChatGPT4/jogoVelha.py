def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-----")


def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False


def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    for _ in range(9):
        imprimir_tabuleiro(tabuleiro)
        linha = int(input("Digite o número da linha (0, 1, 2): "))
        coluna = int(input("Digite o número da coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual

            if verificar_vitoria(tabuleiro, jogador_atual):
                imprimir_tabuleiro(tabuleiro)
                print(f"Parabéns! Jogador {jogador_atual} venceu!")
                break

            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Essa posição já está ocupada. Tente novamente.")

    else:
        imprimir_tabuleiro(tabuleiro)
        print("Empate!")

# Iniciar o jogo
jogar_jogo_da_velha()