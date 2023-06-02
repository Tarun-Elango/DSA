# graph using adjaceny matrix


def addvertex(v):
    global graph
    global verticesNO
    global vertices

    if v in vertices:
        print("already added")

    else:
        verticesNO += 1
        vertices.append(v)

        # add zero to existing arrays in graph array. for the new vertex with '0', indicating no edge betweem them
        if verticesNO > 1 :
            for eachArray in graph:
                eachArray.append(0)
        
        # add new array to graph array, depending on size of existing array.
        temp =[]
        for eachVertex in range(verticesNO):
            temp.append(0)
        
        graph.append(temp)


def addEdge(v1,v2,e):
    # find array for v1
    if v1 not in vertices:
        return('not present')
    elif v2 not in vertices:
        return('not present')
    else:
        v1Location = vertices.index(v1)
        v2Location = vertices.index(v2)
        graph[v1Location][v2Location]= e


vertices = []
# stores the number of vertices in the graph
verticesNO = 0
graph = []
# Add vertices to the graph
addvertex(1)
addvertex(2)
addvertex(3)
addvertex(5)
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
addEdge(1, 2, 1)
addEdge(1, 3, 1)
addEdge(2, 3, 3)
addEdge(3, 5, 4)
addEdge(5, 1, 5)

print(graph)

'''
output 
[[0, 1, 1, 0], [0, 0, 3, 0], [0, 0, 0, 4], [5, 0, 0, 0]]
each array if for the corresponding vertex
each sub array is the edge connection value between that and the other array
example

'''

# pretty print below
for i in range(len(graph)):

    # subloop to loop each array
    for j in range(len(graph[i])):
        index =None
        vertice=None
        if graph[i][j] != 0:
            index = j
            vertice= vertices[j]
            print(vertices[i], f' is connected to {vertice} with edge length {graph[i][j]}')
