import numpy as np
import matplotlib.pyplot as plt
import csv

nome_arquivo = 'dados.csv'

X = []
Y = []

# Abrir o arquivo CSV para leitura
with open(nome_arquivo, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    cabecalho = next(leitor_csv, None)
    
    for linha in leitor_csv:
        
        X.append(float(linha[0]))
        Y.append(float(linha[1]))


def regressao_polinomial(X, Y, grau):
    # Realizar a regressão polinomial
    coeficientes = np.polyfit(X, Y, grau)

    # Criar uma função polinomial a partir dos coeficientes
    polinomio = np.poly1d(coeficientes)

    return polinomio

# Informar grau do polinômio
grau_polinomio = int(input("Informe o grau do polinômio: "))

# Regressão polinomial
polinomio_aproximacao = regressao_polinomial(X, Y, grau_polinomio)

# Pontos para a curva ajustada
X_aprox = np.linspace(min(X), max(X), 100)
Y_aprox = polinomio_aproximacao(X_aprox)

# Plotagem
plt.scatter(X, Y, label='Pontos Originais')
plt.plot(X_aprox, Y_aprox, 'r', label=f'Aproximação Polinomial (Grau {grau_polinomio})')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
