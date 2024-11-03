class HashTable():
    def __init__(self, n):
        self.max_size = n
        self.arr = [[] for i in range(n)]

    def get_hash(self, key):
        if type(key) == float or type(key) == int:
            return int(key) % self.max_size

        h = 0
        for char in key:
            h += ord(char)
        return h % self.max_size

    def __setitem__(self, key, val):
        hash_value = self.get_hash(key)

        if not self.arr[hash_value]:
            self.arr[hash_value].append((key, val))
            return

        for index, element in enumerate(self.arr[hash_value]):
            if element[0] == key:
                self.arr[hash_value][index] = (key, val)
                return
        self.arr[hash_value].append((key, val))

    
    def __getitem__(self, key):
        hash_value = self.get_hash(key)

        if not self.arr[hash_value]:
            return

        for e in self.arr[hash_value]:
            if e[0] == key:
                return e[1]
    
    def __delitem__(self, key):
        hash_value = self.get_hash(key)
        
        if not self.arr[hash_value]:
            return

        for e in self.arr[hash_value]:
            if e[0] == key:
                self.arr[hash_value].remove(e)

    def print(self):
        print(self.arr)