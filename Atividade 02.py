import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

# Dados de entrada
secoes_nominais_mm2 = np.array([0.5, 0.75, 1, 1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240, 300, 400, 500, 630, 800, 1000])
a1_2 = np.array([7, 9, 11, 14.5, 19.5, 26, 34, 46, 61, 80, 99, 119, 151, 182, 210, 240, 273, 321, 367, 438, 502, 578, 669, 767])
a1_3 = np.array([7, 9, 10, 13.5, 18, 24, 31, 42, 56, 73, 89, 108, 136, 164, 188, 216, 245, 286, 328, 390, 447, 514, 593, 679])

# Criando DataFrame
df = pd.DataFrame({'Secao_Nominal_mm2': secoes_nominais_mm2, 'A1_2': a1_2, 'A1_3': a1_3})

# Estimando a seção nominal
def encontrar_secao_nominal(corrente, num_condutores):
    coluna = f'A1_{num_condutores}'
    interpolacao = interp1d(df[coluna], df['Secao_Nominal_mm2'], kind='linear', fill_value='extrapolate')
    secao_estimada = interpolacao(corrente)
    return secao_estimada

# Correntes de 10A a 100A para 2 condutores (A1-2)
for corrente in range(10, 101):
    secao = encontrar_secao_nominal(corrente, 2)
    print(f"Corrente: {corrente}A, Seção Nominal Estimada: {secao:.2f} mm²")

# Correntes de 10A a 100A para 3 condutores (A1-3)
for corrente in range(10, 101):
    secao = encontrar_secao_nominal(corrente, 3)
    print(f"Corrente: {corrente}A, Seção Nominal Estimada: {secao:.2f} mm²")