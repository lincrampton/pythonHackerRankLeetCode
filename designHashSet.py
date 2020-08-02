'''Design a HashSet without using any built-in hash table libraries.
To be specific, your design should include these functions:
	add(value): Insert a value into the HashSet. 
	contains(value) : Return whether the value exists in the HashSet or not.
	remove(value): Remove value in the HashSet, if it exists'''



class MyHashSet:

    def __init__(self):
        self.hashset = set()
       

    def add(self, key: int) -> None:
        self.hashset.add(key)
       

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)

           
    def contains(self, key: int) -> bool:
        return True if (key in self.hashset) else False
