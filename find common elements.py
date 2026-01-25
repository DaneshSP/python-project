list1=[1,2,3,4]
list2=[3,4,5,6]
for i in (list1):
    for j in (list2):
        if i==j:
            print(i, end=" ")
print()
            
#or

list1=[1,2,3,4]
list2=[3,4,5,6]
common=set(list1) & set(list2)
print(common)
