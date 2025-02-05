from collections import deque

def recursiveDFS(root, target):
    if not root:
        return
    if root == target:
        return root
    leftSearch = recursiveDFS(root.left, target)
    if leftSearch:
        return leftSearch
    return recursiveDFS(root.right, target)

def iterativeDFS(root, target):
    stack = deque([root])
    seen = set()
    seen.add(root)

    while stack:
        currentNode = stack.popleft()
        for node in currentNode.adjencyList:
            if node in seen:
                continue
            if node:
                continue #do something
        stack.append(node.left)
        stack.append(node.right)
        seen.add(node.left)
        seen.add(node.right)