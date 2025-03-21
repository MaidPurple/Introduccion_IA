import numpy as np
import random
import matplotlib.pyplot as plt
import itertools

n_puntos=8
ancho, alto=1500,1500
v_ini_feromonas =5
alpha= 0.5
beta= 4
delt= 0.2
Q=1
puntos=[(random.randint(0,ancho),random.randint(0,alto))for i in range(n_puntos)]

#%%time
m_distancia=np.zeros((n_puntos, n_puntos))
m_feromonas=np.full((n_puntos, n_puntos), v_ini_feromonas)
#rellenamos la matriz de distancias
for i in range(n_puntos):
    for j in range(i, n_puntos):  # Iterar solo sobre la diagonal superior
        distancia = ((puntos[i][0] - puntos[j][0])**2 + (puntos[i][1] - puntos[j][1])**2)**0.5
        m_distancia[i][j] = distancia
        m_distancia[j][i] = distancia 

def probabilidad(inicio, destinos, alpha, beta):
    # Calcula las probabilidades usando una comprensión de listas
    dis_fero = [(m_distancia[inicio][destino]**-1)**beta * (m_feromonas[inicio][destino])**alpha for destino in destinos]

    # Suma total de los valores
    total = sum(dis_fero)

    # Calcula las probabilidades normalizadas
    probabilidades = [df / total for df in dis_fero]

    # Selecciona el destino basado en las probabilidades
    destino = random.choices(destinos, probabilidades, k=1)[0]

    return probabilidades, destino

def ruta(puntos, alpha, beta):
    inicio = 0
    ruta = [inicio]  # Inicia en el punto 0
    p = puntos.copy()  # Copia de la lista de puntos
    p.remove(puntos[inicio])  # Elimina el punto inicial de los destinos posibles

    while len(p) > 0:
        destinos = [puntos.index(punto) for punto in p]  # Índices de los destinos restantes
        siguiente_p = probabilidad(inicio, destinos, alpha, beta)[1]  # Selección probabilística del próximo destino
        ruta.append(siguiente_p)  # Agrega el siguiente punto a la ruta
        p.remove(puntos[siguiente_p])  # Elimina el punto visitado de la lista
        inicio = siguiente_p  # Actualiza el punto actual

    ruta.append(0)  # Regresa al punto inicial
    return ruta
longitudes=[]
for i in range(10000):
    for j in range(2):
        listado_de_aristas=[]
        camino=ruta(puntos, alpha, beta)
        aristas=[(camino[j],camino[j+1])for j in range(len(camino)-1)]
        longitud=sum([m_distancia[arista[0]][arista[1]] for arista in aristas ])
        if i==0:
            camino_min=camino
            long_min=longitud
            aristas_min=aristas

        else:
            if longitud<long_min:
                camino_min=camino
                aristas_min=aristas
                long_min=longitud

            else:
                pass
        aristas=[(camino[j],camino[j+1])for j in range(len(camino)-1)]
        longitud=sum([m_distancia[arista[0]][arista[1]] for arista in aristas ])
        longitudes.append(longitud)
        #print('hormiga {} {} longitud:{}'.format(i,camino, longitud))
        #actualizamos la matriz de feromonas
        listado_de_aristas+=aristas
    m_feromonas=m_feromonas*(1-delt)
    
    for arista in aristas_min:
        m_feromonas[arista[0]][arista[1]]=m_feromonas[arista[0]][arista[1]]+(Q/long_min)
print('longitud minima: {}'.format(min(longitudes)))
fig, ax=plt.subplots(1,1, figsize=(12,12))
etiqueta=0
print('hormiga {} {} longitud:{}'.format(i,camino, longitud))
for punto in puntos:
    
    ax.scatter(punto[0],punto[1], color='blue')
    ax.text(punto[0]+5,punto[1]+5,str(etiqueta))
    etiqueta+=1
for par in itertools.combinations(range(n_puntos),2):
    ax.plot([puntos[i][0] for i in par],[puntos[j][1] for j in par], color='grey',alpha=0.2)
ax.plot([puntos[i][0] for i in camino],[puntos[i][1] for i in camino])

ax.plot([puntos[i][0] for i in camino_min],[puntos[i][1] for i in camino_min],color='red')
plt.show()

