def birthday_Cake_Candles(height):
    i=0
    max=height[i]
    while i<len(height):
        if height[i]>max:
            max=height[i]
        i+=1
    j=0
    count=0
    while j<len(height):
        if height[j]==max:
            count+=1
        j+=1    
    print(max, count)

num=int(input("enter the child's Age: "))
height=list(map(int,input("enter the candles height: ").split()))[:num] #use spacebar after entering one number
# print(height)
birthday_Cake_Candles(height)

