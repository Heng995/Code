#指定作業九(程式作業)
#利用白話演算法Ch07投影片或課本之程式碼(兩者皆有提供)，
#嘗試自行宣告主程式，並重新組合(1)串列宣告(2)函數與(3)程式片段為一支可以完整執行的程式，
#需提供 .py 程式並將執行結果截圖上傳！

nodes = ('A', 'B', 'C', 'D', 'E')
distances = {
    'A': {'D': 2, 'B': 5},
    'B': {'A': 4, 'D': 2, 'E': 4},
    'C': {'B': 7, 'E': 2},
    'D': {'A': 5, 'B': 9, 'E': 2},
    'E': {'D': 2, 'B': 1, 'C': 5},
}

unvisited = {node: None for node in nodes}
visited = {}
current = 'A'
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited:
            continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance      
    visited[current] = currentDistance
    
    del unvisited[current]
    if not unvisited:
        break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]
print(visited)