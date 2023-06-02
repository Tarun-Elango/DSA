# consists of vertices, which are connected to each other by edges

# using adjacency list
# stored in the format of vertex, adjacent vertex, edge connecting them

# methods to add vertice(vertex), add edges(v1,v2,e), print

def add_vertex(v, graph):
    global verticesNo
    if v in graph:
        print(f'vertice ${v} already added')
    else:
        verticesNo += 1
        graph[v] =[] # add the vertex to the grapch dict 

def add_edge(v1,v2,e, graph):
    global verticesNo
    if v1 not in graph:
        print(f'{v1} does not exist')
    elif v2 not in graph:
        print(f'{v2} does not exist')
    else:
        temp = [v2,e]
        graph[v1].append(temp)

#pretty print
def prettyPrint(graph):
    for i in graph:
        for j in graph[i]:
            print(f'node {i} is connected to {j[0]} with edge length {j[1]}')


graph ={} # either send as parameter
verticesNo=0 # or create a global variable inside the methods and initialize outside

add_vertex(1, graph)
add_vertex(2, graph)
add_vertex(3, graph)
add_vertex(5, graph)
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
add_edge(1, 2, 1, graph)
add_edge(1, 3, 1, graph)
add_edge(2, 3, 3, graph)
add_edge(3, 5, 4, graph)
add_edge(5, 1, 5, graph)

print("graph stored as dict",graph)
prettyPrint(graph)

'''
the output
{1: [[2, 1], [3, 1]], 2: [[3, 3]], 3: [[5, 4]], 5: [[1, 5]]}
example 
1->2 with edge length 1
1->3 with edge length 1
3->5 with edge length 4

'''
    
