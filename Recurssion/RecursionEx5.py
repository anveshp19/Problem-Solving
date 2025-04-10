#RecursionEx5.py
def natural(n):
    if n<=0:
        raise ValueError("Enter Positive Numbers Only.")
    if n==1:
        return 1
    else:
        return n+natural(n-1)

#Main Program
try:
    n=int(input("Enter a Number:"))
    print(f"Sum of {n} Natural Numbers is {natural(n)}")
except ValueError:
    print("Enter Natural Numbers Only.")
except RecursionError:
    print("You Have Exceding Maximum Recursion Limit.")