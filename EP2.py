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

def alocar_navios_jogador(mapa, frota):
    numero_nacao = selecionar_nacao()
    nacao = list(PAISES.keys())[numero_nacao - 1]
    frota_selecionada = PAISES[nacao]
    print(f"\nVocê selecionou a frota do país {nacao}")
    print("Alocando navios...")
    for navio, quantidade in frota_selecionada.items():
        print(f"Alocando {quantidade} navios do tipo {navio}...")
        for _ in range(quantidade):
            while True:
                exibir_tabuleiro(mapa)
                posicao = input(f"Escolha a posição para o navio {navio} (ex: A1): ")
                orientacao = input("Escolha a orientação do navio (h para horizontal, v para vertical): ").lower()
                linha = int(posicao[1:]) - 1
                coluna = ALFABETO.index(posicao[0].upper())
                if posicao_suporta(mapa, CONFIGURACAO[navio], linha, coluna, orientacao):
                    if orientacao == 'v':
                        for i in range(linha, linha + CONFIGURACAO[navio]):
                            mapa[i][coluna] = 'N'
                    elif orientacao == 'h':
                        for j in range(coluna, coluna + CONFIGURACAO[navio]):
                            mapa[linha][j] = 'N'
                    break
                else:
                    print("Posição inválida! Tente novamente.")

def realizar_ataque(mapa, linha, coluna):
    if mapa[linha][coluna] == 'N':
        mapa[linha][coluna] = 'X'
        print("Acertou um navio!")
    else:
        mapa[linha][coluna] = 'O'
        print("Errou o alvo!")

def verificar_vitoria(mapa):
    for linha in mapa:
        if 'N' in linha:
            return False
    return True

def foi_derrotado(matriz):
    for linha in matriz:
        if 'N' in linha:
            return False
    return True

def jogar_batalha_naval():
    tamanho_tabuleiro = 10
    tabuleiro_jogador1 = cria_mapa(tamanho_tabuleiro)
    tabuleiro_jogador2 = cria_mapa(tamanho_tabuleiro)

    print("=" * 37)
    print("|                                     |")
    print("| Bem-vindo ao INSPER - Batalha Naval |")
    print("|                                     |")
    print("=" * 37)
    print("Iniciando o Jogo!\n")

    print("Frotas disponíveis:")
    for numero, nacao in PAISES.items():
        print(f"{numero}: {nacao}")
        for navio, quantidade in nacao.items():
            print(f"   {quantidade} {navio}")

    alocar_navios_jogador(tabuleiro_jogador1, PAISES)

    print("\nComputador está alocando os navios de guerra do país Japão...")
    aloca_navios(tabuleiro_jogador2, PAISES['Japão'])

    print("\nComputador já está em posição de batalha!\n")

    vez_do_jogador1 = True

    while True:
        if vez_do_jogador1:
            print("\nVez do Jogador 1:")
            exibir_tabuleiro(tabuleiro_jogador2)
            while True:
                ataque = input("Escolha a posição para atacar (ex: A1): ")
                linha = int(ataque[1:]) - 1
                coluna = ALFABETO.index(ataque[0].upper())
                if 0 <= linha < tamanho_tabuleiro and 0 <= coluna < tamanho_tabuleiro:
                    if tabuleiro_jogador2[linha][coluna] == ' ':
                        realizar_ataque(tabuleiro_jogador2, linha, coluna)
                        break
                    else:
                        print("Posição já foi atacada! Escolha outra.")
                else:
                    print("Posição inválida! Tente novamente.")
            if verificar_vitoria(tabuleiro_jogador2):
                print("\nParabéns! Jogador 1 venceu!")
                break
        else:
            print("\nVez do Computador:")
            linha = random.randint(0, tamanho_tabuleiro - 1)
            coluna = random.randint(0, tamanho_tabuleiro - 1)
            print(f"O computador ataca a posição {ALFABETO[coluna]}{linha + 1}")
            realizar_ataque(tabuleiro_jogador1, linha, coluna)
            if verificar_vitoria(tabuleiro_jogador1):
                print("\nO Computador venceu!")
                break

        vez_do_jogador1 = not vez_do_jogador1

# Iniciar o jogo
jogar_batalha_naval()
