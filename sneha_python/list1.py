list1= [1,3,2,4,5]
list2= [1,2,3,4,5]
print("the first list is :"+ str(list1))
print("the second list is :"+ str(list2))
list1.sort()
list2.sort()
if list1 == list2:
    print("The list are equal")
else: 
    print("the lists are not same ")
