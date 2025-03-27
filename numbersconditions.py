#check positive or negative
num1=int(input("Enter a number"))


if num1 > 0:
    print("The number is positive")
else:
    print("The number is negative")

 # profit or loss
cp=int(input("Enter the cost price"))
sp=int(input("Enter the selling price"))

if (sp>cp):
    print("profit")
    profit_amount=sp-cp
    print (profit_amount)
else:
    print("Loss")

# check a number is greater or smaller
i=int(input("Enter a number"))
if i < 15:
    print("i is smaller that 15")
else:
    print("i is greater that 15")

print("I am outside if else")

 # check even or odd

n=int(input("Enter a number"))
if (n%2==0) :
    print("The number is even")
else :
    print("The number is odd")