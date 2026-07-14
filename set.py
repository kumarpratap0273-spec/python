# A set in Python is a built-in data type that stores an unordered collection of unique, immutable elements, meaning duplicates are automatically removed and the order of items is not preserved.

myset = {"apple",1,2, "banana", "cherry"}
print(myset)
print(type(myset))
print(len(myset))

#set method
print("adding new element of a set")

#adding new elemnt
myset.add("orange")
print(myset)

#update
myset.update(["grapes","kiwi"])
print(myset)

#remove
myset.remove("banana")
print(myset)

#discard
myset.discard("kiwi")
print(myset)



