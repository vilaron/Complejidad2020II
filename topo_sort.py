#Sirve para graficos dirigidos  aciclicos
#todas las flechas van de izquierda a derecha (no siempre estan seguidas) y no necesariamente va a existir una sola solucion
adjd = [
    [2],
    [2 , 3], 
    [0 , 1], 
    [1]
    ]

visitados = [False] * len(adjd)

topo = []

#el dfs va a nod padre a nodo hijo 
def dfs(v):
    visitados[v] = True
    for u in adjd[v]:
        if visitados[u] == False:
            dfs(u)
    #se asegura que v ya no tiene mas hijos posibles/ninguno
    topo.append(v)

dfs(0)
topo.reverse()
print(topo)