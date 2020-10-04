#cada posicion de la lista representa a un nodo y lo que hay en esa posicion representa los nodos adyacentes a ese nodo
adjd = [
    [2],
    [2 , 3], 
    [0 , 1], 
    [1]
    ]

adjNd = [
    [2],
    [3], 
    [1], 
    []
    ]

#necesitar una lista de visitados para evitar repetir los nodos repetidos 
#for i in range(len(visitados)):
#    visitados.append(False)

visitados = [False] * len(adjd)

def dfs(v):
    visitados[v] = True
    print(v)
    for u in adjd[v]:
        if visitados[u] == False:
            dfs(u)

dfs(0)


