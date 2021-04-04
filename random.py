# Memory locations in python are integer and can be gotten using the id() function
# E.g;
tuple1 = (1, 2, 3, 4, 5)
tuple1_id = id(tuple1)
print("Tuple1:", tuple1, "\nTuple1 id:", tuple1_id)

tuple2 = (1, 2, 3, 4, 5)
tuple2_id = id(tuple2)
print("Tuple2:", tuple2, "\nTuple2 id:", tuple2_id)

print(hash(tuple1), hash(tuple2))

# UNDERSTAND MEMORY LOCATIONS
# HASHING AND HASH VALUES
# id() FUNTION IN PYTHON