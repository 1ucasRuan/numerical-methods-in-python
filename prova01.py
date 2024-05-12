import numpy as np 
import sys

arq_saida = "arq_saida.txt"

def lendo_arquivos():
    arq_resistencia = "resistencias.in"
    arq_tensao = "tensoes.in"

    if len(sys.argv) > 1: arq_resistencia = sys.argv[1]
        
    if len(sys.argv) > 2: arq_tensao = int(sys.argv[2])
        
    if len(sys.argv) > 3: arq_saida = sys.argv[3]

    try:
        r = np.loadtxt(arq_resistencia)
    except:
        print("Erro ao ler arquivo", arq_resistencia)
        sys.exit()

    try:
        v = np.loadtxt(arq_tensao)
    except:
        print("Erro ao ler arquivo", arq_tensao)
        sys.exit()
    
    return r, v

def calculando_matriz(resistencias, tensoes):
    n = len(tensoes) 
    m = len(tensoes[0]) 

    qtd_coluna = (n * (m - 1)) + 1
    qtd_linha = (n * (m - 1))
    linhas = 0
    colunas = 0
    matriz = np.zeros((qtd_linha, qtd_coluna))

    for lin in range(0, m-1):
        for col in range(0, n): 
            if col == (n-1):
                matriz[linhas, colunas] = resistencias[lin][col] + resistencias[lin][col+1] 
                matriz[linhas, qtd_coluna-1] = tensoes[lin][col] - tensoes[lin][col+1]    
            else:
                matriz[linhas, colunas] = resistencias[lin][col] + resistencias[lin][col+1] 
                matriz[linhas, colunas+1] = - resistencias[lin][col+1]
                matriz[linhas, qtd_coluna-1] = tensoes[lin][col] - tensoes[lin][col+1]
            linhas += 1    
            colunas += 1
    matriz = np.round(matriz, decimals=2)
    return matriz

def salvando_matriz_expandida(matriz_expandida):
    try:
        np.savetxt(arq_saida, matriz_expandida, fmt='%.2f', delimiter=' ')
        print('\n \u2713 Matriz salva com sucesso!')
        print(f'Arquivo salvo como: {arq_saida}')
    except:
        print(f'\n \u2717 Erro ao salvar matriz no arquivo {arq_saida}.txt')

def main():
    resistencias, tensoes = lendo_arquivos()
    matriz_expandida = calculando_matriz(resistencias, tensoes)
    print('Matriz expandida Ab')
    print(matriz_expandida)
    salvando_matriz_expandida(matriz_expandida)

# Inicializando o programa
main()