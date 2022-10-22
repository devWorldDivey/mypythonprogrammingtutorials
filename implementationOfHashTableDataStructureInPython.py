"""This program is implementation of hash table in Python"""


# Step 1. Create a hash table (empty list) in constructor
class HashTable:
    def __init__(self, size=10):
        self.data_map = [None] * size

    # whenever an object of Hashtable will be created it will initialize empty list
    # Step 2. Create a Hash Function, to get an integer value of array index
    def _hash_value(self, key):
        hash_key = 0
        for letters in key:
            hash_key = (hash_key + ord(letters) * 23) % len(self.data_map)
        return hash_key

    # Step 3. Print the list
    def print_table(self):
        for i, value in enumerate(self.data_map):
            print(i, " ", value)

    # Step 4. Below function will set the value in the list
    def set_item(self, key, value):
        index = self._hash_value(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


# Test the methods

myHashTable = HashTable()
myHashTable.set_item("Divey", "Male")
myHashTable.set_item("Divey", "C11/12A-3rd Floor")
myHashTable.print_table()
