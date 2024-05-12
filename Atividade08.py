import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def F(x1, x2):
    return (3 * x1 - np.cos(x2) - 1.5)**2 + (x1**2 - x2**2 + 2 * x2 - 1)**2

def gradient(x1, x2):
    df_dx1 = 2 * (3 * x1 - np.cos(x2) - 1.5) * 3 + 2 * (x1**2 - x2**2 + 2 * x2 - 1) * 2 * x1
    df_dx2 = 2 * (3 * x1 - np.cos(x2) - 1.5) * np.sin(x2) + 2 * (x1**2 - x2**2 + 2 * x2 - 1) * (-2 * x2 + 2)
    return np.array([df_dx1, df_dx2])

def gradient_descent(initial_x, learning_rate, num_iterations):
    x = initial_x
    for _ in range(num_iterations):
        grad = gradient(x[0], x[1])
        x = x - learning_rate * grad       
        x = np.clip(x, -5, 5)

    return x

def grafico_3d():
    x1_values = np.linspace(-5, 5, 100)
    x2_values = np.linspace(-5, 5, 100)
    x1_mesh, x2_mesh = np.meshgrid(x1_values, x2_values)
    F_values = F(x1_mesh, x2_mesh)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x1_mesh, x2_mesh, F_values, cmap='viridis', alpha=0.8)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('F(x1, x2)')

    ax.scatter(min_params[0], min_params[1], F(min_params[0], min_params[1]), color='red', s=100, label='Valor mínimo da Função: ' + str(min_value))

    ax.view_init(elev=20, azim=125)

    plt.legend()
    plt.show()

initial_params = np.array([0.0, 0.0])
learning_rate = 0.01
num_iterations = 1000
min_params = gradient_descent(initial_params, learning_rate, num_iterations)
min_value = F(min_params[0], min_params[1])

grafico_3d()
print(f"Parâmetros mínimos: [{min_params[0]}, {min_params[1]}]")
print("Valor mínimo da função:", min_value)