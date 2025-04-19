class node:
    def __init__(self, key: int, value: int):
        self.next
        self.prev
        self.key = key
        self.value = value

class cache:
    def __init__(self, cap: int):
        self.capacity = cap
        self.cache = {}

        self.dummy_head = node(0,0)
        self.dummy_tail = node(0,0)
        self.dummy_head.prev = self.dummy_tail
        self.dummy_tail.next = self.dummy_head

    # add node to the right
    def add(self, node):
        
    # remove node from list
    def remove(self, ndoe):

    def get(self, key: int):
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].value 
        return -1

    
    def put(self, key: int, value: int):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            