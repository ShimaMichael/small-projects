from collections import deque

#Iteratively for trees
def bfs(start, target):
    if not start:
        return False

    stack = deque(start)
    while stack:
        current = stack.pop()
        if current == target:
            return current
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    
    return False

#Iteratively for graphs
def bfsG(graph, start, target):
    seen = set()
    queue = deque([start])

    if not start:
        return False
    
    while queue:
        current = queue.pop()
        if current == target:
            return current
        seen.add(current)
        for node in graph.neigbors:
            if node not in seen:
                queue.append(node)
    return False

#bfs Recursion trees
def bfsTR(nodes, target):
    if not nodes:
        return False
    level = []
    for node in nodes:
        if node == target:
            return node
        if node.left:
            level.append(node.left)
        if node.right:
            level.append(node.right)
    return bfsTR(level, target)


