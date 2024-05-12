import numpy as np

def normalizar_dados(X, A, B, P):
    valor_maximo = np.max(np.abs(np.concatenate([X, A, B.flatten(), P.flatten()])))
    X_normalizado = X / valor_maximo
    A_normalizado = A / valor_maximo
    B_normalizado = B / valor_maximo
    P_normalizado = P / valor_maximo
    return X_normalizado, A_normalizado, B_normalizado, P_normalizado

def funcao_objetivo(X, A, B, P):
    N = len(A)
    M = len(B[0])
    soma_total = 0.0
    for i in range(N):
        soma_interna = 0.0
        for j in range(N):
            for k in range(M):
                soma_interna += B[j][k] * (X[k] - P[i, k])**2
        soma_total += A[i] * np.exp(-soma_interna)
    return soma_total

def gradiente(X, A, B, P):
    N = len(A)
    grad = np.zeros_like(X, dtype=float)
    for i in range(N):
        soma_interna = 0.0
        for j in range(len(X)):
            for k in range(len(X)):
                derivada_parcial = 2 * B[j, k] * (X[k] - P[i, k]) * np.exp(-np.sum(B[j, :] * (X - P[i, :])**2))
                soma_interna += derivada_parcial
        grad += soma_interna * A[i] * (X - P[i, :])
    return grad

def erro_absoluto(x_antigo, x_novo):
    return np.max(np.abs(x_novo - x_antigo))

def gradiente_descendente(X_inicial, taxa_aprendizado, iteracoes, A, B, P, limite_erro):
    X = X_inicial.copy()
    for _ in range(iteracoes):
        grad = gradiente(X, A, B, P)
        X_novo = X - taxa_aprendizado * grad
        if erro_absoluto(X, X_novo) < limite_erro:
            break
        X = X_novo
    return X, funcao_objetivo(X, A, B, P)


taxa_aprendizado = 0.1
iteracoes = 1000
limite_erro = 1e-6

# Dados de entrada
A = np.array([-2, -2])
B = np.array([[-2, 0], [0, -2]])
P = np.array([[0, 0], [0, 0]])
X0 = np.array([10, 10])

X0, A, B, P = normalizar_dados(X0, A, B, P)

resultado, valor_minimo = gradiente_descendente(X0, taxa_aprendizado, iteracoes, A, B, P, limite_erro)
resultado_truncado = list(map(lambda x: round(x, 1), resultado))

print('Resultado:', resultado_truncado)
print("Valor Mínimo:", valor_minimo)