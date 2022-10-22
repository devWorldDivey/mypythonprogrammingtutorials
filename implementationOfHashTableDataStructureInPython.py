"""This program is implementation of hash table in Python"""


# Step 1. Create a hash table (empty list) in constructor
class HashTable:
    def __init__(self):
        self.data_map = []

    # whenever an object of Hashtable will be created it will initialize empty list
    # Step 2. Create a Hash Function, to get an integer value of array index
    def _hash_value(self, key):
        hash_key = 0
        for letters in key:
            hash_key = (hash_key + ord(key) * 23) % len(self.data_map)
        return hash_key

    # Step 3. Print the list
    def print_table(self):
        for i, value in enumerate(self.data_map):
            print(i, " ", value)
