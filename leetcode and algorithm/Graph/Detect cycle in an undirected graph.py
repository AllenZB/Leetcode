# Python Program to detect cycle in an undirected graph
from collections import defaultdict


# This class represents a undirected
# graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def isCyclicUtil(self, v, visited, parent):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, v)):
                    return True
            elif parent != i:
                return True

        return False

    def isCyclic(self):


        visited = [False] * (self.V)

        # Call the recursive helper
        # function to detect cycle in different
        # DFS trees
        for i in range(self.V):
            if visited[i] == False:
                if (self.isCyclicUtil
                    (i, visited, -1)) == True:
                    return True

        return False


# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)

if g.isCyclic():
    print
    "Graph contains cycle"
else:
    print
    "Graph does not contain cycle "
g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)

if g1.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")

# This code is contributed by Neelam Yadav
