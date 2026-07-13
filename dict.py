#A dictionary in Python is a built‑in data type that stores data as key–value pairs, where each key is unique and maps to a specific value. It’s written inside curly braces {} with the format key: value.

dict={
    "name": "pratap",
    "cgpa":7.00,
    "marks":65,
}
print(dict)
print(type(dict))

#changing values
dict["name"] = "pratap kumar"
print(dict)

#updating values
dict.update({"cgpa":8.00})
print(dict)

#adding new value
dict["marks"] = 77
print(dict)

dict.update({"age": 20}) #updating dictionary with new key value pair
print(dict)

#removing item
dict.pop("marks") #removes item with specified key
print(dict)

dict.popitem() #removes last item
print(dict)

del dict["cgpa"] #removes item with specified key
print(dict)

dict.clear() #removes all items
print(dict)

