total1 =0
total2 =0
list1= [1,3,2,4,5]
list2= [1,2,3,4,6]
for ele in range(0,len(list1)):
    total1= total1 + list1[ele]

for ele in range(0,len(list2)):
    total2= total2 + list2[ele]

if total1==total2:
 print("the sums are equal")
else:
  print("not equal")