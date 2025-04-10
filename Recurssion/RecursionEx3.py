#Factorial Series
def factorial(n):
    if(n<0):
        raise ValueError("Enter Natural Numbers Only.")
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

#Main Program
try:
    n=int(input("Enter any Number:"))
    print(f"Factorial of a Number {n}:{factorial(n)}")
except ValueError as ve:
    print("ValueError:",ve)
except RecursionError:
    print("The Maximum Limit is 999 You Have Exceding that Limit.")