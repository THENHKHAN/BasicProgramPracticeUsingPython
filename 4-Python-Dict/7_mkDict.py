

#way-3
def mkDictByKeyword(**dct) :
                print(dct)
                print(type(dct))
        

# way-2
def mkDict(dct):
        print(dct)
        print(type(dct))


print("*********************   WAY - 1 : Constuctor    ***********************")
thisdict = dict(brand="Ford", model="Mustang", year=1964) # 1 - WAyyyyyyyY - using constructor
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)


print("*********************   WAY - 2 : tuple with Constuctor    ***********************")
tpl = ( (1,"Ford"), (2,"Mustang"),(3,1964) )
mkDict(dict(tpl)) # 2 - WAYyyyyyyy - using constructor from tuple


print("*********************   WAY - 3 : Paking: key-value pair ***********************")
# 3 - WAYyyyyyyy - using key value pair
mkDictByKeyword(brand="Ford", model="Mustang", year=1964) 

'''
*********************   WAY - 1 : Constuctor    ***********************
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
*********************   WAY - 2 : tuple with Constuctor    ***********************
{1: 'Ford', 2: 'Mustang', 3: 1964}
<class 'dict'>
*********************   WAY - 3 : Paking: key-value pair ***********************
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
<class 'dict'>

'''