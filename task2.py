def nonDivisibleSubset(list_of_elements,k):
    i=0
    c=0
    while i<len(list_of_elements):
        j=i+1
        while j<len(list_of_elements):
            sum=list_of_elements[i]+list_of_elements[j]
            if sum%k!=0:
                c+=1
            j+=1
        i+=1
    print(c)
num=int(input("enter the limit: "))
list_of_elements=list(map(int,input("enter the list elements: ").split()))[:num]
nonDivisibleSubset(list_of_elements,3)


