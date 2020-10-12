#Lista de adyacencia sin pesos
adj = [
    [1 , 2],
    [0 , 3],
    [0 ,3 ,4],
    [1 , 2 , 4],
    [2 , 3]
]
#Lista de adyacencia con pesos
#  0   [ (1 , 10) , (2 , 15)] -> Se conecta con el 1 nodo con un peso de 10 y con el nodo 2 con un peso 15
adj = [
    [(1, 10) , (2 , 15)],
    [(0 , 10) , (3 , 19)],
    [(0 , 15) , (3 , 17) , (4 , 13)],
    [(1 , 19) , (2, 17 ) , (4 , 11)],
    [(2 , 13) , (3 , 11)]
]

#infinito o un valor muy grande (10 elevado a la 10)
#Se usa para comparar el menor peso acumulado y depende del problema
infinty = 10 ** 10

start = 0
end = 4

n = len(adj)

#distancia o peso acumulado minimo necesario para llegar al nodo [i]
dist = n * [infinty]
prev = n * [None]

path = []

def djikstra():
    dist[start] = 0

    #Evita repetidos
    #Ordena de forma ascendente
    #Lo uso porque quiero los nodos menores (cuando lo inicio)
    q = set()

    q.add((start , dist[0]))

    while q:
        #Toma el nodo (indice) pero no su peso
        v = q.pop()[0]
        for elem in adj[v]:
            #Toma el indice del nodo hijo de v mas no su peso
            u = elem[0]

            #Toma el peso del nodo hijo de v
            weight = elem[1]


            if dist[v] + weight < dist[u]:
                #No se puede modificar el valor de u,  lo borro , lo actualizo ...
                q.discard((u , dist[u]))
                dist[u] = dist[v] + weight
                #Y lo vuelo a poner
                q.add((u , dist[u]))

                #Se agrega a v como el previo mas cercano a u
                prev[u] = v 

def restore_path():
    v = end
    while v != None:
        path.append(v)
        v = prev[v]
    path.reverse()

djikstra()
restore_path()

print(prev)

print(dist)

print("The shortest path is " , path)
print("With a total weight of" , dist[end])
for i in range(len(path) - 1):
    node1 = path[i]
    node2 = path[i + 1]                   
    print(node1  , "->" , node2 , "peso" ,  dist[path[i + 1]] - dist[path[i]])