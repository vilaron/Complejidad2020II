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

queue = []

#Lista de predecedores(primer padre de un nodo)
prev = [None] * len(adj)

start = 0
end = 6

#Lista de caminos/paths
path = []

def bfs():
    visitados[start] = True
    queue.append(start)
    while queue:
        v = queue.pop(0)
        print(v) 
        for u in adj[v]:
            if visitados[u] == False:
                visitados[u] = True
                queue.append(u)
                #añado a v como el padre de u
                prev[u] = v
'''
def bfs():
    goal = true
    visitados[start] = True
    queue.append(start)
    while queue and goal:
        v = queue.pop(0)
        print(v) 
        for u in adj[v]:
            if visitados[u] == False:
                visitados[u] = True
                queue.append(u)
                #añado a v como el padre de u
                prev[u] = v
            if u == end:
                goal = false
                break
'''


def build_path():
    v = end
    while v != None:
        path.append(v)
        v = prev[v]


bfs()
build_path()
print(prev)
print("el camino mas corto es:")
path.reverse()
print(path)

for i in range(len(prev)):
    print("Soy el hijo " , i , "de padre"  , prev[i])

