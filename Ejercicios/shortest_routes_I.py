#import sys, resource
#resource.setrlimit(resource.RLIMIT_STACK, (2**32, -1))
#sys.setrecursionlimit(10**9)
adj = []

#n es el numero de vertices y m es el numero de aristas 
n  , m = [ int(x) for x in input().split()]

for i in range(n):
    adj.append([])

for i in range(m):
    x , y , z = [int(r) for r in input().split()]
    x -=1
    y -=1
    adj[x].append((y , z))


#print(adj)

infinity = 10**14

#Syrjälä
start = 0   

n = len(adj)

dist = [infinity] * n

prev = [None] * n

def djikstra():
    dist[start] = 0 
    q = set()
    q.add((start , 0  ))
    while q:
        v = q.pop()[0]
        for elem in adj[v]:
            u = elem[0]
            w = elem[1]
            if(dist[v] + w < dist[u]):
                q.discard((u , dist[u]))
                dist[u] = dist[v] + w 
                q.add((u , dist[u]))
                prev[u] = v

djikstra()
for i in range(len(dist)):
    print(dist[i], end=" ", sep=" ")