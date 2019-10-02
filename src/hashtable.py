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
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


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
        '''
        h_key = self._hash_mod(key)
        c_pair = self.storage[h_key]

        if c_pair is not None:
            # basically taking whatever was there and replacing it with none
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
        '''
        new_storage = [None] * self.capacity
        self.storage.extend(new_storage)
        
        #for pair in new_storage:
        #    if pair is not None and pair.next is None:
        #        self.storage[self._hash_mod(pair.key)] = pair
        #    elif pair is not None and pair.next is not None:
        #        pair = pair.next
        #        self.storage[self._hash_mod(pair.key)] = pair
        #    else:
        #        pass



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
