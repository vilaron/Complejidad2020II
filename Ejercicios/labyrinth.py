n , m = [int(x) for x in input().split()]
    
#leemos la matriz

matrix = [[] for x in range(n)]
for i in range(n):
    matrix[i] = list(input())

visitados = [[False for j in range(m)] for i in range(n)]

queue = []

prev = [[None for j in range(m)] for i in range(n)]


path = []

def bfs(i, j):
    #i es la fila y j es la columna
     visitados[i][j] = True
     queue = [(i, j)]
     while queue:
        vcoor = queue.pop(0)
        #print("Estoy en " , vcoor[0] , " " , vcoor[1] )
        if(vcoor[0] + 1 < n ):
            if( visitados[vcoor[0] + 1][vcoor[1]] == False and matrix[vcoor[0] + 1][vcoor[1]] != "#"):
                visitados[vcoor[0] + 1][vcoor[1]] = True
                queue.append([vcoor[0] +1 , vcoor[1]])
                prev[vcoor[0] + 1][vcoor[1]] = (vcoor[0] , vcoor[1] )                
        if( vcoor[0] - 1 >= 0):
            if(visitados[vcoor[0] - 1][vcoor[1]] == False and matrix[vcoor[0] - 1][vcoor[1]] != "#"):
                visitados[vcoor[0] - 1][vcoor[1]] = True
                queue.append([vcoor[0] - 1 , vcoor[1]])
                prev[vcoor[0] - 1][vcoor[1]] = (vcoor[0] , vcoor[1] )  
                
        if(vcoor[1]+ 1 < m):
            if(visitados[vcoor[0]][vcoor[1] + 1] == False and matrix[vcoor[0]][vcoor[1] + 1] != "#"):
                visitados[vcoor[0]][vcoor[1] + 1] = True
                queue.append([vcoor[0]  , vcoor[1] + 1])
                prev[vcoor[0]][vcoor[1] + 1] = (vcoor[0] , vcoor[1] )
        if(vcoor[1] - 1 >= 0):
            if(visitados[vcoor[0]][vcoor[1] - 1] == False and matrix[vcoor[0]][vcoor[1] - 1] != "#"):
                visitados[vcoor[0]][vcoor[1] - 1] = True
                queue.append([vcoor[0]  , vcoor[1] - 1])
                prev[vcoor[0]][vcoor[1] - 1] = (vcoor[0] , vcoor[1] ) 

'''
def build_path():
    v = end
    while v != None:
        path.append(v)
        v = prev[v]
'''



def build_path(i , j):
    vi = i
    vj = j
    while prev[vi][vj] != None:
        path.append((vi , vj))
        coord = prev[vi][vj]
        vi = coord[0]
        vj = coord[1]
    path.append((vi , vj))
        
        


for i in range(n):
    for j in range(m):
       if(matrix[i][j] == 'A'):
           bfs(i , j)


#print(prev)

for i in range(n):
    for j in range(m):
        if(matrix[i][j] == 'B'):
            build_path(i , j)

path.reverse()

s=""
for i in range(len(path) - 1):
    t = path[i]
    t2 = path[i + 1]
    if(t[0] < t2[0]):
        s+="D"
    if(t[0] > t2[0]):
        s+="U"
    if(t[1] < t2[1]):
        s+="R"
    if(t[1] > t2[1]):
        s+="L"

if(len(s) == 0):
    print("NO")
else:
    print("YES")
    print(len(s))
    print(s)





#print(path)