# Count Chacter Occurances In Python
"""
def day2(n):
    count={}
    for i in n:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    print(count) 
A=input("Enter A String :")
print(day2(A))               

"""




def day2(n):
    count={}
    for i in n:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    print(count) 
A=input("Enter A String :")
print(day2(A))    