#nos indica hallar la cantidad de componentes fuertemente conexas asi como los nodos que las contituyen
#un grafo desde el cual en un nodo se puede a un nodo pertenecientes a ese grafo
#necesitamos: adjacencia, visitados , topo , adjacencia transpuesta(mismo grafo diregido en el cual se inverte la relacion padre hijo ej de a -> b sera  a <- b)
adj = [
    [1],
    [2],
    [0, 3],
    []
]

adj_trans = [
    [2], 
    [0],
    [1],
    [2]
]

visitados = [False] * len(adj)

topo = []
comp = []

#Recorrer el primer grafo
def dfs(v):
    visitados[v] = True
    for u in adj[v]:
        if visitados[u] == False:
            dfs(u)
    topo.append(v)

t = 0
#aseguramos que todos los nodos esten visaitados
for i in range(len(adj)):
    if(visitados[i] == False):
        dfs(i)

#Recorrer el grafo transpuesto
def dfs2(v):
    comp.append(v) #0 , 2 , 1
    visitados[v] = True
    for u in adj_trans[v]:
        if visitados[u] == False:
            dfs2(u)

topo.reverse()

#es otro visitado , pero por conveniencia reinicio la antigua
visitados = [False] * len(adj_trans)
print("Ordenamiento topologico" , topo)
#me asegura que todos los elementos del ordanamiento topo esten visitados
for i in range(len(adj_trans)):
    v = topo[i]
    if(visitados[v] == False):
        dfs2(v)
        print(comp)
        comp.clear()
        t += 1


print(t)


