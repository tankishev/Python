# Create a class Storage. The __init__ method should accept one parameter - the capacity of the storage. 
# The Storage class should also have an attribute called storage - empty list, where all the items will be stored. 
# The class should have two additional methods:
# •	add_product(product: str) - adds the product in the storage if there is enough space for it
# •	get_products() - returns the storage list

class Storage:
    def __init__(self, capacity) -> None:
        self.storage = []
        self.capacity = int(capacity)
    
    def add_product(self, product: str):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self) -> list:
        return self.storage

#Test class
storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())
