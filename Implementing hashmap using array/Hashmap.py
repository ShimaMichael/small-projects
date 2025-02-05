class Hashmap:
    def __init__(self):
        self.map = [ [] for _ in range(30)]

    def _hash(self, key):
        return hash(key) % 30
    
    def add(self, key, value):
        position = self._hash(key)
        bucket   = self.map[position]
        for pair in bucket:
            if pair[0] == position:
                pair[1] = value
                return
        bucket.append(key)
        bucket.append(value)

    def get(self, key):
        position = self._hash(key)
        bucket = self.map[position]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None
    
    def remove(self, key, value):
        position = self._hash(key)
        bucket   = self.map(position)
        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)
                return
        print("Key not found")

if __name__ == "__main__":
    Hmap = Hashmap()
    Hmap.add("a", 2)
    Hmap.add("b", 3)
    Hmap.get("c")
    print(Hmap.map)
    
    
