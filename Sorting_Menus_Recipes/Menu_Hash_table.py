class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)

    def remove(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError(key)


# Create a hash table for menus and recipes
menu_hash_table = HashTable(10)

# Insert menus and recipes
menu_hash_table.insert("Breakfast", "Scrambled eggs")
menu_hash_table.insert("Lunch", "Chicken sandwich")
menu_hash_table.insert("Dinner", "Grilled salmon")

# Get recipes for menus
print(menu_hash_table.get("Breakfast"))  # Output: Scrambled eggs
print(menu_hash_table.get("Lunch"))  # Output: Chicken sandwich
print(menu_hash_table.get("Dinner"))  # Output: Grilled salmon

# Remove a menu and its recipe
menu_hash_table.remove("Lunch")

# Try to get the removed menu (raises KeyError)
print(menu_hash_table.get("Lunch"))  # Raises KeyError
