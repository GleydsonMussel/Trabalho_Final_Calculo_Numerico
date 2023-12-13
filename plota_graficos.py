import matplotlib.pyplot as plt
import numpy as np

# Configuração das fontes
fonte_titulo={  
              "fontsize":14,
              "fontweight": 'bold',
              "fontname":'Times New Roman',
              }
fonte_labels={
            "fontsize":12,
            "fontweight":'bold',
            'fontname':'Times New Roman',
            }
fonte_legenda={
            "size":9,
            "weight":'normal',
            'family':'Times New Roman',
            }


def plota_grafico_parte1(vetor_x, vetor_y, nome_graficos):
    
    plt.title("Iterações x Erro Relativo", fontdict = fonte_titulo)
    plt.xlabel("Iterações", fontdict = fonte_labels)
    plt.ylabel("Erro Relativo", fontdict = fonte_labels)
    #plt.xticks(np.arange(0,100,1))
    #plt.xlim(5,19)
    #plt.yticks(np.arange(0,5,1))
    #plt.ylim(-1,9)
    plt.grid()
    plt.plot(vetor_x, vetor_y, '.')
    plt.savefig("./Graficos/"+nome_graficos+".png")
    plt.close()

def plota_EDO(vetor_x, vetor_y, nome_graficos):
    
    plt.title("Gráfico Aproximado da EDO", fontdict = fonte_titulo)
    plt.xlabel("x", fontdict = fonte_labels)
    plt.ylabel("u(x)", fontdict = fonte_labels)
    #plt.xticks(np.arange(0,100,1))
    #plt.xlim(5,19)
    #plt.yticks(np.arange(0,5,1))
    #plt.ylim(-1,9)
    plt.grid()
    plt.plot(vetor_x, vetor_y)
    plt.savefig("./Graficos/"+nome_graficos+".png")
    plt.close()

def plota_parte_b(xs, solucoes, nome_graficos, lambida ):
    
    labesls_linhas = ["N = 10", "N = 50", "N = 100"]
    plt.title("Gráfico Aproximado da EDO para Lambida = "+str(lambida), fontdict = fonte_titulo)
    
    plt.xlabel("x", fontdict = fonte_labels)
    plt.ylabel("u(x)", fontdict = fonte_labels)
    
    #plt.xticks(np.arange(0,100,1))
    #plt.xlim(5,19)
    #plt.yticks(np.arange(0,5,1))
    #plt.ylim(-1,9)
    plt.grid()
    for [x, solucao, label] in zip(xs, solucoes, labesls_linhas):
        plt.plot(x, solucao, label = label)
        
    plt.legend()
    plt.savefig("./GraficosParteB/"+nome_graficos+".png")
    plt.close()