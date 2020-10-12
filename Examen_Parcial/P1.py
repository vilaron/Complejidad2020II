
adj = [
 [1,4],
 [0,5],
 [3,4,5],
 [2,4],
 [0,2,3,5],
 [1,2,4]
]

visitados = [False] * len(adj)

color = [""] * len(adj)

prev = [None] * len(adj)

queue = []


start = 0

def bfs():
    visitados[start] = True
    color[start] = "Black"
    queue.append(start)
    while queue:
        v = queue.pop(0)
        for u in adj[v]:
            if visitados[u] == False:
                if(color[v] == "White"):
                    color[u] = "Black"
                else:
                    color[u] = "White"
                
                visitados[u] = True
                queue.append(u)
            prev[u] = v

bfs()
colorcan = color

#print(prev)
#print(color)
for i in range(1 , len(prev)):
    if(color[i] == "Black"):
        j = prev[i]
        if(color[j] == "Black"):
            #print("aca se cumple")
            colorcan[i] = "White"


for i in range(len(color)):
    print("Del Nodo", i + 1 , "su color es" ,color[i] )