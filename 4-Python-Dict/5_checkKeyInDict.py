

def checkKeyInDict(key,dct) :
    if key in dct :
         print(f"Yes, key - {key} is one of the keys in the above dictionary")

    else:
         print(f"NO, key - {key} is not in the above dictionary")


def byGetMethod(key, dct) : # The get() method returns the value of the item with the specified key.
     # dictionary.get(keyname, fallbackValue) - fallbackValue: Optional. A value to return if the specified key does not exist. Default value None

    check = dct.get(key, False)   
    if not check : # means if check is false then only this will execute
         print(f"NO, key - {key} is not in the above dictionary")
    else :
         print(f"Yes, key - {key} is one of the keys in the above dictionary")


myDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("ORIGINAL Dict : {}".format(myDict)) 
checkKeyInDict("model",myDict)
checkKeyInDict("name",myDict)
print("***** By get() dict method  *******")
byGetMethod("model",myDict)
byGetMethod("name",myDict)

'''
ORIGINAL Dict : {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
Yes, key - model is one of the keys in the above dictionary
NO, key - name is not in the above dictionary
***** By get() dict method  *******
Yes, key - model is one of the keys in the above dictionary
NO, key - name is not in the above dictionary

'''