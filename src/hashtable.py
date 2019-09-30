# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        h_key = self._hash_mod(key)
        c_pair = self.storage[h_key]

        while c_pair is not None and c_pair.key != key:
            c_pair = c_pair.next

        if c_pair is None:
            n_pair = LinkedPair(key, value)
            n_pair.next = self.storage[h_key]
            self.storage[h_key] = n_pair
        else:
            c_pair.value = value



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        h_key = self._hash_mod(key)
        c_pair = self.storage[h_key]

        if c_pair is not None:
            # basically taking whatever was there and replacing 
            self.storage[h_key] = None
        elif c_pair is not None and c_pair.next is not None:
            n_pair = c_pair.next
            self.storage[h_key] = n_pair
        else:
            print('THIS IS A WARNING: KEY IS NOT FOUND!')


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        h_key = self._hash_mod(key)
        c_pair = self.storage[h_key]

        while c_pair is not None and c_pair.key != key:
            c_pair = c_pair.next

        if c_pair is None:
            return None
        else:
            return c_pair.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        n_cap = self.capacity * 2
        n_table = HashTable(n_cap)
        for n_pair in self.storage:
            self.insert(n_pair.key, n_pair.value)
            if n_pair.next:
                c_pair = n_pair.next
                while c_pair:
                    self.insert(c_pair.key, c_pair.value)
                    c_pair = c_pair.next
        return n_table



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
