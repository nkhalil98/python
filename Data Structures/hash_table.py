# lookup by key is O(1) in the average case scenario but O(n) in the worst case scenario if the hash table uses a bad hash function that leads to a lot of collisions
# we can handle collisions using techniques such as open addressing, linear probing, and separate chaining
# below is a basic hashmap implementaion that takes a string, an integer, or a float as valid keys and stores key-value pairs in a python list

class HashTable():
    def __init__(self, n):
        self.max_size = n
        self.arr = [None for i in range(n)]

    def get_hash(self, key):
        if type(key) == float or type(key) == int:
            return int(key) % self.max_size

        h = 0
        for char in key:
            h += ord(char)
        return h % self.max_size

    def __setitem__(self, key, val):
        hash_value = self.get_hash(key)
        self.arr[hash_value] = val
    
    def __getitem__(self, key):
        hash_value = self.get_hash(key)
        return self.arr[hash_value]
    
    def __delitem__(self, key):
        hash_value = self.get_hash(key)
        self.arr[hash_value] = None

    def print(self):
        print(self.arr)