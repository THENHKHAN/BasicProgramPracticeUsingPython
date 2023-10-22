
# In python there multiple function to do such thing so let's leverage it.

decimalNum = int (input ("\n\nPlease enter any decimal(or normal number) : ") )
binaryNum = bin(decimalNum)
octalNum = oct(decimalNum)
hexDecimalNum = hex(decimalNum)
print ("Decimal {} To Binary : {}".format(decimalNum , binaryNum))
print ("Decimal {} To Octal : {}".format(decimalNum , octalNum))
print ("Decimal {} To Hexadecimal : {}".format(decimalNum , hexDecimalNum))


# OUTPUT
'''

Please enter any decimal(or normal number) : 12
Decimal 12 To Binary : 0b1100
Decimal 12 To Octal : 0o14
Decimal 12 To Hexadecimal : 0xc

'''