#Find out x power n.
def recursive_fun(x,n):
    if n==0:
        return 1
    else:
        return x*recursive_fun(x,(n-1))
#Main Program
num=int(input("Enter the Value of n:"))
pow=int(input("Enter the Value of pow:"))
print(recursive_fun(num,pow))
