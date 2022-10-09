n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
n4 = int(input("Enter fourth number: "))
n5 = int(input("Enter fifth number: "))
additionN = n1 + n2 + n3 + n4 + n5
averageN = additionN/5
quotient1_5 = n1 // n5
productN2N4_N3 = (n2 * n4) / n3
reqN = 42
print("sum of the numbers =", additionN)
print("Average of the numbers:", averageN)
print ("Quotient of the first number divided by the fifth number", quotient1_5)
#printing greater than 5
list_number = [ n1, n2, n3, n4, n5]
if any((match := item) > 5 for item in list_number):
            print("One or more numbers are greater than 5")
else:
            print('No items in the list are greater than 5')
#printing equal to 42
if reqN - n1 == False:
    print ("The input is equal to 42")
elif reqN - n1 != True:
    print (n1, "is not equal to 42")
if reqN - n2 == False:
    print ("The input is equal to 42")
elif reqN - n2 != True:
    print (n2, "is not equal to 42")
if reqN - n3 == False:
    print ("The input is equal to 42")
elif reqN - n3 != True:
    print (n3, "is not equal to 42")
if reqN - n4 == False:
    print ("The input is equal to 42")
elif reqN - n4 != True:
    print (n4, "is not equal to 42")
if reqN - n5 == False:
    print ("The input is equal to 42")
elif reqN - n5 != True:
    print (n5, "is not equal to 42")
#printing divisible by 13
if n1 % 13 == 0:
    print(n1 , "is divisible by 13")
elif n1 % 13 != 0:
    print( n1 , "is not divisible by 13")
if n2 % 13 == 0:
    print(n2 , "is divisible by 13")
elif n2 % 13 != 0:
    print( n2 , "is not divisible by 13")
if n3 % 13 == 0:
    print(n3 , "is divisible by 13")
elif n3 % 13 != 0:
    print( n3 , "is not divisible by 13")
if n4 % 13 == 0:
    print(n4 , "is divisible by 13")
elif n4 % 13 != 0:
    print( n4 , "is not divisible by 13")
if n5 % 13 == 0:
    print(n5 , "is divisible by 13")
elif n5 % 13 != 0:
    print( n5 , "is not divisible by 13")