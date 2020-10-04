#cada posicion de la lista representa a un nodo y lo que hay en esa posicion representa los nodos adyacentes a ese nodo
#lista de adj, visitados y cola o queue 
#grafo no dirigido
adj = [
    [1,2],
    [0, 3 , 4], 
    [0 ,4 , 5], 
    [1, 6],
    [1 , 2  , 6 ],
    [2 ,6],
    [3 , 4 , 5]
]

visitados = [False] * len(adj)

#FiFo (First in , First out)
#se comporta como cola
queue = []

#punto de inicio
start = 0

#se lee por niveles
def bfs():
    visitados[start] = True
    queue.append(start)
    while queue:
        #se borra el elemento del principio y lo guardas a la misma vez en v
        v = queue.pop(0)
        print(v) 
        for u in adj[v]:
            if visitados[u] == False:
                visitados[u] = True
                queue.append(u)

bfs()