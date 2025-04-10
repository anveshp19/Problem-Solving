#RecursionEx7.py
def find_min_max(lst,low,high):
    #If There is One Element
    if low==high:
        return lst[low],lst[high]
    #If There is Two Element
    if high==low+1:
        if lst[low]<lst[high]:
            return lst[low],lst[high]
        else:
            return lst[high],lst[low]
    #If More Than Two Elements
    mid=(low+high)//2
    min1,max1=find_min_max(lst,low,mid)
    min2,max2=find_min_max(lst,mid+1,high)

    return min(min1,min2),max(max1,max2)
#Main Program
lst=[20,30,-50,70,80,-55,0,7,1]
minimum,maximum=find_min_max(lst,0,len(lst)-1)
print(f"Minimum Element:{minimum}")
print(f"Maximum Element:{maximum}")
