def factorial(a):
    if a==1:
        return a
    else:
        return a*factorial(a-1)

a=int(input("Enter a number : "))

if a<0:
    print("There is no factorial for 0.")
elif a == 0:
    print("The factorial of 0 is 1.")
else:
    print("The factorial of",a,"is",str(factorial(a))+".")

print("This is a factorial program")
    
#added a new comment to test
