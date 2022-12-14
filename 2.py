

def findCheapestPrice(n, flights, src, dst, k):
    #CODE HERE
    # visited = {src}
    # price = []
    # graph = []
    # for i in range(n):
    #     price.append(float('inf'))
    # # for s, t, w in flights:
    # price[0] = 0
    # for i in range(len(flights)):
    #     for j in range(len(flights)):
    #         if flights[j][1] == j:
    #             if flights[i][2] < price[j]:
    #                 price[j] = flights[i][2]
    graph = {}
    for i in range(len(flights)):
        graph[i] = []
        for j in range(len(flights)):
            if flights[j][0] == i:
                graph[i].append(flights[j][1])

    # print(graph)

    queue = [src]
    candidate = [([src], 0)]
    paths = []
    while queue:
        pop = queue.pop(0)
        path = candidate.pop(0)
        differenceSet = set(graph[pop]) - set(path[0])
        for element in differenceSet:
            if element == dst:
                price = 0
                for p in flights:
                    if p[0] == path[0][-1] and p[1] == element:
                        price = p[2]
                paths.append((path[0] + [element], path[1] + price))
            else:
                price = 0
                for p in flights:
                    if p[0] == path[0][-1] and p[1] == element:
                        price = p[2]
                queue.append(element)
                candidate.append((path[0] + [element], path[1] + price))

    answer = False
    min = float('inf')
    for path in paths:
        if path[1] < min and len(path[0])-2 <= k:
            min = path[1]
            answer = True

    if answer:
        return min
    else:
        return -1

print(findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))  # Prints 200
print(findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))  # Prints 500
