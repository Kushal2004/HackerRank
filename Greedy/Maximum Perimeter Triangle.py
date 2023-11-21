'''Given an array of stick lengths, use 3 of them to
construct a non-degenerate triangle with the maximum
possible perimeter. Return an array of the lengths of its
sides as 3 integers in non-decreasing order.
If there are several valid triangles having the maximum
perimeter:'''

def maximumPerimeterTriangle(sticks):
    sticks.sort()
    Max_perimeter_sticks=[]
    Max_perimeter_sum=0
    for i in range(0,len(sticks)-2):
        side_length =sticks[i]+sticks[i+1]
        if(side_length > sticks[i+2]):
            perimeter = sticks[i]+sticks[i+1]+sticks[i+2]
            if(perimeter > Max_perimeter_sum):
                Max_perimeter_sum= perimeter
                Max_perimeter_sticks=[sticks[i],sticks[i+1],sticks[i+2]]
    if((Max_perimeter_sum)==0):
        return [-1]
    else:
        return Max_perimeter_sticks
