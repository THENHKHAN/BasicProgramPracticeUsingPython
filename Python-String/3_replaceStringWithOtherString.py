
# Replace a string with another string using replace method.It return a new string

def replaceAllOccurences (myStr) :
    

    strNew = myStr.replace("one", "three")
    print(strNew)

def replaceASpecifiedCount( myStr) :
        replStr = myStr.replace("one" , "three" , 2 )
        print(f" After repacing two * one * with two * three *  : {replStr}")


myStr = "Hello, World "
print(f"Original before replacing: {myStr}")

# replacing last two He with PK

repStr = myStr.replace("ld" , "PK") 
print(f"NEW STRING  After replacing: {repStr}")

txt = "one one was a race horse, two two was one too."
print(f"Original string: {txt}")


print(f" ************ AFTER Replacing ALL character **********")


# Replace all occurrence of the word "one":
replaceAllOccurences(txt)

print(f" ************ AFTER Replacing only TWO word **********")

# Replace the two first occurrence of the word "one":
replaceASpecifiedCount ( txt )


# INFO :

'''
The replace() method replaces a specified phrase with another specified phrase.


We can replace many character or string of character with other. But only in serialwise

EX: 1 - s1=Hello -> s1.replace("He" , "KLL") OUTPU = print s1 -> KLLllo

'''
# Syntax and info :
'''
string.replace(oldvalue, newvalue, count)
The replace() method replaces a specified phrase with another specified phrase.
** : Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.
count: Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences.

'''