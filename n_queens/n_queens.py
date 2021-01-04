from itertools import permutations
TAMANHO_TABULEIRO = 8

def eh_solucao(estado):
    tabuleiro_completo = todas_pecas(estado) 
    if not tabuleiro_completo:
        return False

    ataque_linha  = mesma_linha(estado) 
    if ataque_linha:
        return False 
    ataque_diagonal = ataque_diagonais(estado)
    return not ataque_diagonal

def mesma_linha(estado):
    len_estado_inicial = len(estado)
    estado_distinto = set(estado)
    len_estado_distinto = len(estado)
    if len_estado_distinto != len_estado_inicial:
        return True 
    return False
def ataque_diagonais(estado):
    posicoes = [(i+1, estado[i]) for i in range(len(estado))]
    diagonais_atacadas = []
    #print("posicoes", posicoes)
    for posicao in posicoes:
        diagonais_atacadas += diagonais(posicao[0], posicao[1])
    #print("diagonais", diagonais_atacadas)
    for posicao in posicoes:
        #print("posicao ", posicao, "esta ? ", posicao in diagonais_atacadas)
        if posicao in diagonais_atacadas:
            return True
    return False

def diagonais_direita_superior(linha, coluna):
    if linha == TAMANHO_TABULEIRO or coluna == TAMANHO_TABULEIRO:
        return [(linha, coluna)]
    return [(linha +1, coluna +1)] + diagonais_direita_superior(linha + 1, coluna + 1)



def diagonais_direita_inferior(linha, coluna):
    if linha == 1 or coluna == TAMANHO_TABULEIRO:
        return [(linha, coluna)]
    return [(linha - 1, coluna +1)] + diagonais_direita_inferior(linha - 1, coluna + 1)

def todas_pecas(estado):
    zeros = list(filter(lambda p: p != 0, estado))
    return len(zeros) == TAMANHO_TABULEIRO

def diagonais_esquerda_inferior(linha, coluna):
    if linha == TAMANHO_TABULEIRO  or coluna == 1:
        return [(linha, coluna)]
    return [(linha + 1, coluna -1)] + diagonais_esquerda_inferior(linha  + 1, coluna - 1)

def diagonais_esquerda_superior(linha, coluna):
    if linha == 1 or coluna == 1:
        return [(linha, coluna)]
    return [(linha - 1, coluna -1)] + diagonais_esquerda_superior(linha -1, coluna - 1)
def diagonais(linha, coluna):

    ei = diagonais_esquerda_inferior(linha, coluna) 
    es = diagonais_esquerda_superior(linha, coluna)
    di = diagonais_direita_inferior(linha, coluna) 
    ds = diagonais_direita_superior(linha, coluna)
    diagonais = ei + es + di + ds
    diagonais = list(filter (lambda x: x != (linha, coluna), diagonais))
    return diagonais

def n_queens():
    for estado in permutations(range(1, TAMANHO_TABULEIRO + 1)):
        if (eh_solucao(estado)):
            imprime_estado(estado)

def imprime_estado(estado):
    print("#"*10)
    print("\t", estado)
    print("#"*10)
    for linha in range(1, TAMANHO_TABULEIRO + 1):
        for coluna in range(1, TAMANHO_TABULEIRO + 1):
            if (estado[linha - 1] == coluna):
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
    print("#"*10)

def main():
    n_queens()

main()
