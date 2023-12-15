import numpy as np
from scipy.optimize import least_squares
import plota_graficos
import sistemas_para_resolver

# x nas funções é um vetor pois na realidade, cada posição desse vetor corresponde a uma variável
def newton_raphson_system(func, jacobian, x0, tol=1e-5, max_iter=100):
    iteracoes = []
    distancias_do_zero = []
    x = x0
    for i in range(max_iter):
        a = -func(x)
        delta_x = np.linalg.solve(jacobian(x), -func(x))
        x = x + delta_x
        iteracoes.append(i)
        distancias_do_zero.append(np.linalg.norm(delta_x)/np.linalg.norm(x))
        
        if distancias_do_zero[i] < tol:
            break
        
    return x, iteracoes, distancias_do_zero

# RESOLVENDO SISTEMAS

# Chutes inicias
chute_inicial_func_1__duas_equacoes =  np.array([1.0, 5.0])
# Calculando um chute inicial melhor usando least_squares
res = least_squares(sistemas_para_resolver.func_1__tres_equacoes, np.array([1.0, 2.0, 3.0]))
#chute_inicial_func_1__tres_equacoes = res.x
chute_inicial_func_1__tres_equacoes = np.array([1.0, 2.0, 3.0])
chute_inicial_func_2__duas_equacoes =  np.array([0.5,3])
chute_inicial_func_2__tres_equacoes = np.array([0.0, 3.0, 2.0])


# Resolvendo o sistema usando o método de Newton-Raphson
solucao, n_iteracoes, distancias_do_zero = newton_raphson_system(sistemas_para_resolver.func_1__duas_equacoes, sistemas_para_resolver.jacobian_func1__duas_equacoes, chute_inicial_func_1__duas_equacoes, 1e-7, 100)
solucao_2, n_iteracoes_2, distancias_do_zero_2 = newton_raphson_system(sistemas_para_resolver.func_2__duas_equacoes, sistemas_para_resolver.jacobian_func2__duas_equacoes, chute_inicial_func_2__duas_equacoes, 1e-7, 100)
solucao_3, n_iteracoes_3, distancias_do_zero_3 = newton_raphson_system(sistemas_para_resolver.func_1__tres_equacoes, sistemas_para_resolver.jacobian_func1__tres_equacoes, chute_inicial_func_1__tres_equacoes, 1e-7, 1000)
solucao_4, n_iteracoes_4, distancias_do_zero_4 = newton_raphson_system(sistemas_para_resolver.func_2__tres_equacoes, sistemas_para_resolver.jacobian_func2__tres_equacoes, chute_inicial_func_2__tres_equacoes, 1e-7, 1000)

# Print das soluções
print(solucao)
print(sistemas_para_resolver.func_1__duas_equacoes(solucao))
print()
print(solucao_2)
print(sistemas_para_resolver.func_2__duas_equacoes(solucao_2))
print()
print(solucao_3)
print(sistemas_para_resolver.func_1__tres_equacoes(solucao_3))
print()
print(solucao_4)
print(sistemas_para_resolver.func_2__tres_equacoes(solucao_4))

plota_graficos.plota_grafico_parte1(n_iteracoes, distancias_do_zero,"Grafico_Sistema_1_Duas_Equacoes")
#plota_graficos.plota_grafico_parte1(n_iteracoes_2, distancias_do_zero_2,"Grafico_Sistema_2_Duas_Equacoes")
plota_graficos.plota_grafico_parte1(n_iteracoes_3, distancias_do_zero_3,"Grafico_Sistema_1_Tres_Equacoes")
#plota_graficos.plota_grafico_parte1(n_iteracoes_4, distancias_do_zero_4,"Grafico_Sistema_2_Tres_Equacoes")