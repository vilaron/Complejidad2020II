#nota extra: no funciona con valores muy altos (por python)
def solucion():
    #n es el numero de filas y m es el numero de columnas 
    n , m = [int(x) for x in input().split()]
    
    #leemos la matriz
    matrix = [[] for x in range(n)]
    for i in range(n):
        matrix[i] = list(input())
    
    #creamos la matriz de los nodos visitados
    visitados = [[False for j in range(m)] for i in range(n)]
    
    arreT = []
    ar = []
    #matriz[i][j] i es la fila y j es la columna
    def dfs(i , j , s  , arl):
        #print("Estoy en la posicion" , i , " " , j)
        visitados[i][j] = True
        if(i + 1 < n ):
            if( visitados[i + 1][j] == False and matrix[i + 1][j] == "."):
                dum = arl
                dum.append("D")
                print(dum)
                dfs(i + 1 , j , s + 1 , dum  )
            elif(matrix[i + 1][j] == "B"):
                ar.append(s)
                arreT.append(arl)
        if(i - 1 >= 0):
            if(visitados[i - 1][j] == False and matrix[i - 1][j] == "."):
                dum = arl
                dum.append("U")
                print(dum)
                dfs(i - 1 , j,s +1 , dum)
            elif(matrix[i - 1][j] == "B" ):
                ar.append(s)
                arreT.append(arl)
        if(j + 1 < m):
            if(visitados[i][j + 1] == False and matrix[i][j + 1] == "."):
                dum = arl
                dum.append("R")
                print(dum)
                dfs(i , j + 1 , s+1 , dum)
            elif(matrix[i][j + 1] == "B" ):
                ar.append(s)
                arreT.append(arl)
        if(j - 1 >= 0):
            if(visitados[i][j - 1] == False and matrix[i][j - 1] == "."):
                dum = arl
                dum.append("L")
                print(dum)
                dfs(i  , j - 1 , s+ 1 , dum)
            elif(matrix[i][j - 1] == "B" ):
                ar.append(s)
                arreT.append([])
                arreT.append(arl)
        print(arl)
    
    
    dfs(1,1,0 , [])
    print(ar)
    print(arreT)
solucion()