import random

# Definições de constantes
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}

# Funções auxiliares
def cria_mapa(N):
    matriz = []
    for i in range(N):
        linha = []
        for j in range(N):
            linha.append(' ')
        matriz.append(linha)
    return matriz

def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    tamanho_mapa = len(mapa)

    if orientacao == 'v':
        if linha + blocos > tamanho_mapa:
            return False
        for i in range(linha, linha + blocos):
            if mapa[i][coluna] != ' ':
                return False
    elif orientacao == 'h':
        if coluna + blocos > tamanho_mapa:
            return False
        for j in range(coluna, coluna + blocos):
            if mapa[linha][j] != ' ':
                return False
    else:
        return False

    return True

def aloca_navios(mapa, frota):
    tamanho_mapa = len(mapa)
    for navio, quantidade in frota.items():
        for _ in range(quantidade):
            while True:
                linha = random.randint(0, tamanho_mapa - 1)
                coluna = random.randint(0, tamanho_mapa - 1)
                orientacao = random.choice(['h', 'v'])
                if posicao_suporta(mapa, CONFIGURACAO[navio], linha, coluna, orientacao):
                    if orientacao == 'v':
                        for i in range(linha, linha + CONFIGURACAO[navio]):
                            mapa[i][coluna] = 'N'
                    elif orientacao == 'h':
                        for j in range(coluna, coluna + CONFIGURACAO[navio]):
                            mapa[linha][j] = 'N'
                    break
    return mapa

def exibir_tabuleiro(tabuleiro):
    tamanho_tabuleiro = len(tabuleiro)
    print('   ' + ' '.join(ALFABETO[:tamanho_tabuleiro]))
    for i, linha in enumerate(tabuleiro):
        print(f'{i+1:2} ', end='')
        for celula in linha:
            print(celula + ' ', end='')
        print()

def selecionar_nacao():
    print("\nEscolha o número da nação para sua frota:")
    while True:
        escolha = input("Número da nação: ")
        if escolha.isdigit() and 1 <= int(escolha) <= 5:
            return int(escolha)
        else:
            print("Número inválido! Escolha um número de 1 a 5.")