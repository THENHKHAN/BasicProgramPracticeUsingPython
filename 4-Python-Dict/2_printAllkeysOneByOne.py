# Print all keys one by one of dictionary

def printKeys(dct):
    lstOfkeys = dct.keys()
    print(lstOfkeys)
    print(type(lstOfkeys))
    for k in lstOfkeys :
        print("key  -> {}".format(k))
    
    # for k in dct : # by default it return keys
    #     print("key  -> {}".format(k))
    
'''
dict_keys(['brand', 'model', 'year'])
<class 'dict_keys'>
key  -> brand
key  -> model
key  -> year
'''


myDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

printKeys(myDict)