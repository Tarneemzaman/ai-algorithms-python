import heapq

def a_star(graph,start_node,goal_node,heuristic):
  pq=[]
  heapq.heappush(pq,(0,start_node))

  distance = {node:float('inf') for node in graph.keys()}
  distance[start_node] = 0

  parent = {}
  visited = set()

  while pq:
    current_f,current_node = heapq.heappop(pq)

    if current_node in visited:
      continue
    visited.add(current_node)

    if current_node == goal_node:
      break

    for neighbour, weight in graph[current_node].items():
      new_distance = distance[current_node] + weight   # g(n)
      if new_distance < distance[neighbour]:
        parent[neighbour] = current_node
        distance[neighbour] = new_distance
        f_value = new_distance + heuristic[neighbour]  # f(n) = g(n)+h(n)
        heapq.heappush(pq,(f_value, neighbour))

  return distance,parent


graph = {
    "A":{"B":1,"C":4},
    "B":{"A":1,"C":2,"D":6},
    "C":{"A":4,"B":2,"D":3},
    "D":{"B":6,"C":3}
}

# heuristic values (estimated distance to goal 'D')
heuristic = {
    "A":4,
    "B":2,
    "C":2,
    "D":0
}

start_node = "A"
goal_node = "D"

result,parent = a_star(graph,start_node,goal_node,heuristic)

temp = goal_node
path = [temp]
while temp!= start_node:
  temp = parent[temp]
  path.append(temp)

path.reverse()
print("Path:",path)
print("Cost:", result[goal_node])
