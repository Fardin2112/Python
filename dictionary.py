thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#for find by specfic key
print(thisdict["model"])

#update
thisdict["CEO"]="Fardin"
thisdict["year"]=2023
thisdict.update({"country": "America"})
print(thisdict)

#remove item
thisdict.pop("country")
#del thisdict["model"]
#The popitem() method removes the last inserted item 
#thisdict.popitem()

#The clear() method empties the dictionary:
thisdict.clear()

#type
print(type(thisdict))
print(type("CEO"))

#length of dict
print(len(thisdict))

#You can use the keys() method to return the keys of a dictionary
for x in thisdict.keys():
  print(x)

#You can also use the values() method to return values of a dictionar
for x in thisdict.values():
  print(x)

# for copy dict
mydict = thisdict.copy()
print(mydict)  