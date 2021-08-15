# Route Between Nodes: Given a directed graph, design an algorithm to find out
# whether there is a route between two nodes.

# For example, depth-first search is a bit simpler to implement since it can
# be done with simple recursion. Breadth-first search can also be useful to find the shortest path, whereas
# depth-first search may traverse one adjacent node very deeply before ever going onto the immediate
# neighbors.

# program to check if there is exist a path between two vertices
# of a graph


# This class represents a directed graph using adjacency list representation


from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Use BFS to check path between s and d
    def isReachable(self, s, d):
        # Mark all the vertices as not visited
        visited = [False]*(self.V)
        # Create a queue for BFS
        queue = []
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
        while queue:
            # Dequeue a vertex from queue
            n = queue.pop(0)

            # If this adjacent node is the destination node,
            # then return true
            if n == d:
                return True

            #  Else, continue to do BFS
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return False


# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
u = 1
v = 2

if g.isReachable(u, v):
    print("There is a path from %d to %d" % (u, v))
else:
    print("There is no path from %d to %d" % (u, v))

u = 3
v = 1
if g.isReachable(u, v):
    print("There is a path from %d to %d" % (u, v))
else:
    print("There is no path from %d to %d" % (u, v))
# This code is contributed by Neelam Yadav
