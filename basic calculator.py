a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
o=input("enter the symbol of the basic operation (+,-,*,/,%,**) you would like to perform:")
if o=='+':
    res= a+b
elif o=='-':
    res= a-b
elif o=='*':
    res= a*b
elif o=='/':
    res= a/b
elif o=='%':
    res= a%b
elif o=='**':
    res= a**b
else:
    res="The operation choice is invalid"
print("The result is", res)