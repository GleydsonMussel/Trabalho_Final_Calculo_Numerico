import numpy as np
import plota_graficos
# Disretizar o domínio dado, [a,b] em N pontos
# Passo para cada ponto: (b-a)/N, b>a
# Aproximação para a segunda derivada: (y_antes - 2*y_atual + y_depois)/passo^2

# y'' = f(x)

# Dado os N pontos oriundos da discretização, originam-se N-1 equações do tipo: (y_(i-1) - 2*y_(i)) + y_(i+1))/passo^2 

# Sempre y_0 = a e y_N = b

# PROBLEMA DE FATO

def imprime_jacobiano(jac):
    for i in range(len(jac[0])):
        for j in range(len(jac[0])):
            print(str(jac[i][j]) + " ", end = "")
        print()
    

def funcao(u, x, lambida, h, N):
    vetor_retorno = np.zeros(N-2) 
    vetor_retorno[0] = (0 + 2 * u[0] - u[1]) - (h**2)*(lambida * np.exp(u[0]) + ((np.pi)**2) * np.sin(np.pi * x[0]) - lambida * np.exp(np.sin(np.pi * x[0])))
    vetor_retorno[N-3] = (-u[N-4] + 2 * u[N-3] - 0 ) - (h**2)*(lambida * np.exp(u[N-3]) + ((np.pi)**2) * np.sin(np.pi * x[N-3]) - lambida * np.exp(np.sin(np.pi * x[N-3])))
    
    for i  in range(1, N-3):
        vetor_retorno[i] = (-1*u[i-1] + 2 * u[i] - u[i+1]) -(h**2)*(lambida * np.exp(u[i]) + ((np.pi)**2) * np.sin(np.pi * x[i]) - lambida * np.exp(np.sin(np.pi * x[i])))

    return vetor_retorno

def derivada_u_ant():
    return -1

def derivada_u_atual(u, lambida, h):
    return (2 - (h**2) * lambida * np.exp(u))
 
def derivada_u_prox():    
    return -1

def monta_jacobiano2(u, N, lambida, h):
    jacobiano = np.zeros([N-2,N-2])
    jacobiano[0][0] = derivada_u_atual(u[0], lambida, h)
    jacobiano[0][1] = -1
    jacobiano[N-3][N-3] = derivada_u_atual(u[len(u)-1], lambida, h)
    jacobiano[N-3][N-4] = -1
    
    for i in range(1, N-3):
        jacobiano[i][i] = derivada_u_atual(u[i], lambida, h)
        jacobiano[i][i+1] = -1
        jacobiano[i][i-1] = -1
    
    imprime_jacobiano(jacobiano)

    return jacobiano

# x nas funções é um vetor pois na realidade, cada posição desse vetor corresponde a uma variável
def newton_raphson_system(lambida, x, h, N, u0, funcao, jacobian, tol=1e-7, max_iter=100):
    iteracoes = []
    distancias_do_zero = []
    u = u0
    for i in range(1, max_iter):
        #imprime_jacobiano(jacobian(u, N, lambida, h))
        delta_u = np.linalg.solve(jacobian(u, N, lambida, h), -funcao(u, x, lambida, h, N))
        u = u + delta_u
        iteracoes.append(i)
        distancias_do_zero.append(np.linalg.norm(delta_u)/np.linalg.norm(u))
        if distancias_do_zero[i-1] < tol:
            break
    return iteracoes, distancias_do_zero, u 

# Discretização
N = 10
# Passo da Discretização
h = 1.0/N
# Vetor para os valores de x 
x = np.linspace(0, 1.0, N)
xloc = x[1:-1]
# Vetor u para as variáveis inicial
u0 = np.zeros([N-2])
# Lambda
lambida = 2

n_iteracoes, distancias_do_zero, solucoes = newton_raphson_system(lambida, xloc, h, N, u0, funcao, monta_jacobiano2, tol=1e-5, max_iter=100)

# Uma vez que o vetor de soluções está aqui, ele ainda não tem anexado nele os valores da condição de contorno, logo, é necessário anexar aqui
solucao_plot = np.array([])
solucao_plot = np.append(solucao_plot, 0)
# Anexando condição de contorno SUPERIOR
solucoes = np.append(solucoes, 0)
# Anexando condição de contorno INFERIOR
solucao_plot = np.append(solucao_plot, solucoes)

plota_graficos.plota_grafico_parte1(n_iteracoes, distancias_do_zero,"Problema_Solucao_de_Contorno_Itercaoes_N_"+str(N))
plota_graficos.plota_EDO(x, solucao_plot,"Problema_Solucao_de_Contorno_N_"+str(N))



