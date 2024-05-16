""" Hash tables can be considered either linear or non-linear data structure. """

# Create a Hash table as a nested list
Hash_Table = [[] for _ in range(10)]


def display_hash(hash_table):
    for index in range(len(hash_table)):
        print(index, end=" ")

        for j in hash_table[index]:
            print("-->", end=" ")
            print(j, end=" ")

        print()


def hashing(key):
    return key % len(Hash_Table)


def insert(hash_table, key, value):
    hash_key = hashing(key)
    hash_table[hash_key].append(value)


insert(Hash_Table, 1, "Andalusia")
insert(Hash_Table, 10, "Fes Jdid")
insert(Hash_Table, 6, "Ouejda")
insert(Hash_Table, 10, "Fes Qdim")
insert(Hash_Table, 9, "Dakhla")
insert(Hash_Table, 4, "Titouane")

display_hash(Hash_Table)
