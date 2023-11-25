start = int(input("Enter start year:"))
end= int(input("Enter end year:"))

while start < end:
  if start% 4==0 and start%100!=0:
    print(start)
  if start%100==0 and start%400==0:
    print(start)
  start+=1

