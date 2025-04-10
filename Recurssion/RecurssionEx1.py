#Division of Two Numbers Using Recurssion
#RecurssionEx1.py
def recurssive_div(a,b):
    if b==0: #if Denominator is Zero
        raise ValueError("Division by Zero is Not-Allowed.")
    if a==0: #if Numerator is Zero
        return 0
    if a<b: #if Numerator is less than Denominator
        return 0
    if a==b: #For Same Numerator and Denominator
        return 1
    else:
        return 1+recurssive_div(a-b,b)
#Main Program
print(recurssive_div(15,5))
