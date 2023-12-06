#  Change the value of a specific item in the dicitonary:

myDict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# lets change model name from Mustang to Audi
print("ORIGINAL Dict : {}".format(myDict)) # ORIGINAL Dict : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
myDict["model"] = "Audi"

print(f"UPDATED Dict : {myDict}") # UPDATED Dict : {'brand': 'Ford', 'model': 'Audi', 'year': 1964}