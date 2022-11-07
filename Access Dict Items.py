car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(car["year"])
x = car.get("year")
print(x)
keys = car.keys()           #The keys() method will return a list of all the keys in the dictionary.
print(keys)
values = car.values()       #The keys() method will return a list of all the values in the dictionary.
print(values)


#Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()

car["color"] = "white"
print(car)

y = car.values()

car["year"] = "2017"
print(car)

#The items() method will return each item in a dictionary, as tuples in a list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x)
if "model" in car:
    print("Yes")
else:
    print("No") 