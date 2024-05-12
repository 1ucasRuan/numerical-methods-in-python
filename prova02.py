import math
import matplotlib.pyplot as plt
import numpy as np

def calcular_raio_circunferencia(D, L):
    # Calcula o comprimento do cateto usando o teorema de Pitágoras
    cateto = math.sqrt((L/2)**2 - (D/2)**2)

    # Verifica se o comprimento do cateto é não negativo
    if cateto < 0:
        raise ValueError("Os comprimentos fornecidos não formam um triângulo válido.")

    # Calcula o raio da circunferência
    raio = L**2 / (8 * cateto) + cateto / 2

    return raio

def plotar_circunferencia(D, L, raio):
    # Gera pontos da circunferência
    theta = np.linspace(0, 2*np.pi, 100)
    x_circunferencia = raio * np.cos(theta)
    y_circunferencia = raio * np.sin(theta)

    # Pontos do poste
    x_poste = np.array([-D/2, D/2])
    y_poste = np.array([-12, -12])

    # Plotagem da circunferência e do poste
    plt.figure()
    plt.plot(x_circunferencia, y_circunferencia, label='Circunferência')
    plt.plot(x_poste, y_poste, 'ro-', label='distancia dos postes')
    plt.title('Circunferência e Distancia entre os postes')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Exemplo de uso
try:
    D = 20
    L = 30

    raio_calculado = calcular_raio_circunferencia(D, L)

    print(f"O raio da circunferência é: {raio_calculado}")

    # Plotagem do grafico
    plotar_circunferencia(D, L, raio_calculado)

except ValueError as e:
    print(f"Erro: {e}")