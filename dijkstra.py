from math import inf

graph= [[0,4,0,0,0,0,0,8,0],
        [4,0,8,0,0,0,0,11,0],
        [0,8,0,7,0,4,0,0,2],
        [0,0,7,0,9,14,0,0,0],
        [0,0,0,9,0,10,0,0,0],
        [0,0,4,14,10,0,2,0,0],
        [0,0,0,0,0,2,0,1,6],
        [8,11,0,0,0,0,1,0,7],
        [0,0,2,0,0,0,6,7,0]]

def dijkstra(graph,s):
    S = [] #Nodos visitados
    length = len(graph)
    dist = [inf]*length #vector de distancias
    dist[s] = 0
    while len(S) < length:
        l = []
        for i in range(length):
            if i not in S:
                l.append(dist[i])
        smallest = min(l)
        indexSmallest=dist.index(smallest)
        S.append(indexSmallest)
        index=0
        for j in graph[indexSmallest]:        
            if j != 0:
                alt = dist[indexSmallest] + graph[indexSmallest][index]
                if alt < dist[index]:
                    dist[index]=alt
            index+=1    
    return dist

print('Distancias minimas desde 0 a todos los vertices')
print(dijkstra(graph,0))
            







       



