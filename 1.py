
Weight = [
      [0,  4,  0,  0,  0,  0,   0,  8,  0],
      [4,  0,  8,  0,  0,  0,   0, 11,  0],
      [0,  8,  0,  7,  0,  4,   0,  0,  2],
      [0,  0,  7,  0,  9, 14,   0,  0,  0],
      [0,  0,  0,  9,  0, 10,   0,  0,  0],
      [0,  0,  4, 14, 10,  0,   2,  0,  0],
      [0,  0,  0,  0,  0,  2,   0,  1,  6],
      [8, 11,  0,  0,  0,  0,   1,  0,  7],
      [0,  0,  2,  0,  0,  0,   6,  7,  0]]

V = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def prim(Vertex, Weight, Starting_Vertex):
    """
    :type Vertex: given as above
    :type Weight: given as above
    :type Starting Vertex: integer ie) 0
    :rtype: MST from starting point, ie) [None, 0, 5, 2, 3, 6, 7, 0, 2]
    """
    result = [None]
    for _ in range(len(result) - 1):
        result.append(-1)
    queue = [Starting_Vertex]
    visited = []

    while queue:
        dequeue = queue.pop(0)
        # result.append(dequeue)

        visited.append(dequeue)

        if len(visited) == len(Weight):
            break

        min = float('inf')
        next = -1
        for v in visited:
            vertex = 0
            for w in Weight[v]:
                if w < min and vertex not in visited and w != 0:
                    min = w
                    next = vertex
                vertex += 1

        min2 = float('inf')
        adding = 0
        for v in visited:
            if Weight[v][next] < min2 and Weight[v][next] != 0:
                min2 = Weight[v][next]
                adding = v
        result.insert(next, adding)


        queue.append(next)



    return result

print(prim(V, Weight, 0))
