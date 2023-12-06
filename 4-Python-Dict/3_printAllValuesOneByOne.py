

def printAllvaluesOfDict(dct):

    # lstOfVals = dct.values()
    # for val in lstOfVals:
    #     print("value  -> {}".format(val))
    # OR
    for key in dct :
       print(f"{key}  -> {dct[key]}")


myDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
printAllvaluesOfDict(myDict)

'''
brand  -> Ford
model  -> Mustang
year  -> 1964

'''