def isSafe(tabuleiro, passoDado, x, y):
    n = tamanhoTabuleiro
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    célula = tabuleiro[x][y]
    if passoDado[x][y]:
        return True

    passoDado[x][y] = True

    if célula == ">" and isSafe(tabuleiro, passoDado, x, y + 1):
        return True
    if célula == "V" and isSafe(tabuleiro, passoDado, x + 1, y):
        return True
    if célula == "<" and isSafe(tabuleiro, passoDado, x, y - 1):
        return True
    if célula == "A" and isSafe(tabuleiro, passoDado, x - 1, y):
        return True

    return False

def contagem_células_seguras(tabuleiro):
    passoDado = [[False] * tamanhoTabuleiro for i in range(tamanhoTabuleiro)]
    contador_seguro = 0
    for i in range(tamanhoTabuleiro):
        for j in range(tamanhoTabuleiro):
            if isSafe(tabuleiro, passoDado , i, j):
                contador_seguro += 1
    return contador_seguro

tamanhoTabuleiro = int(input())
# faz o Tabuleiro
tabuleiro = []
for i in range(tamanhoTabuleiro):
    linha = [x for x in input().split()]
    tabuleiro.append(linha)

células_seguras = contagem_células_seguras(tabuleiro)

print(células_seguras)