
#  how to add and remove item to a dictionary

def addItemtoDict(key, value , dct) :
    if key in dct :
        print("this key -{0} is already exist in the dict: {1}".format(key, list(dct.keys())))
    else:
        dct[key] = value
    

def rmvItemtoDict(key, dct) :
        if key not in dct :
           print("this key -{0} is NOT exist in the dict: {1}".format(key, list(dct.keys())))

        else:
            a= dct.pop(key) # it removed value with key w.r.t provided key and return value of the provided key
            print(a)

myDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
key = "color"
value = "red"
print("ORIGINAL Dict : {}".format(myDict)) 
addItemtoDict(key, value, myDict)
print("Updated Dict : {}".format(myDict)) 

rmvItemtoDict(key, myDict)
print("Updated Dict after removing {} key : {}".format(key, myDict)) 

'''
ORIGINAL Dict : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
Updated Dict : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
red
Updated Dict after removing color key : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
'''