import math
 
# Função f(x)
def func( x ):
    return  x * math.exp(x)
 
# Calculando a integral aproximada
def simpsons(ll, ul,intervalos ):
 
    # Calculando valores para h
    h = ( ul - ll ) / intervalos
 
    # Criando listas para armazenar os valores para x e f(x)
    x = list()
    fx = list()
     
    # Calculando valores para x e f(x)
    i = 0
    while i<=intervalos:
        x.append(ll + i * h)
        fx.append(func(x[i]))
        i += 1
 
    # Calculando a resposta
    res = 0
    i = 0
    while i<=intervalos:
        if i == 0 or i == intervalos:
            res+= fx[i]
        elif i % 2 != 0:
            res+= 4 * fx[i]
        else:
            res+= 2 * fx[i]
        i+= 1
    res = res * (h / 3)
    return res
     
limite_inferior = 2.12
limite_superior = 4
intervalos = 12
print(f"{simpsons(limite_inferior, limite_superior,intervalos)}")