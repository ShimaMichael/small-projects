# Simplified file manager system
class Node:
    def __init__(self, is_file: bool):
        self.is_file = is_file
        self.children = {}
        self.content = ""

class FileManager:
    def __init__(self):
        self.root = Node(False)

    def _traverse(self, path: str, create: bool, is_file: bool):
        parts = [p for p in path.splt("/") if p]
        root_node = self.root

        for i, part in enumerate(parts):
            if part not in root_node.children:
                if not create:
                    return None
                root_node.children[part] = Node(is_file if i == len(parts)-1 else False)    
            node = node.children[part]
        return node

    def mkdir(self, path: str) -> bool:
        return self._traverse(path, True, False)

    def add_file(self, path: str, content: str) -> bool:
        file = self._traverse(path, True, True)
        file.content = content

    def read_file(self,path: str) -> str:
        file = self._traverse(path, False, False)
        if file and file.is_file:
            return file.content
        else: 
            return ""