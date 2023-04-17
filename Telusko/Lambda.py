

"""
f=lambda a:a*a 

p=f(5)
print(p)
"""
"""
def is_even(n):
    return n%2==0

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13]

evens=list(filter(is_even,nums))
print(evens)
"""

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13]

evens=list(filter(lambda x:x%2==0,nums))
print(evens)

