# Loop through both keys and values using items() method of dictionary

# there is method of dictinary called listObj.items() - it return list of tuple with key and value pair - it helps to gte and value at the same time

def getkeyAndvalues(dct) :

        print(dct.items()) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

        for key, value in dct.items():
                print(f"{key}->{value}")



myDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
getkeyAndvalues(myDict)

'''
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
brand->Ford
model->Mustang
year->1964
'''