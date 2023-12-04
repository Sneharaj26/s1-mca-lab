asquare = lambda x: x*x
atriangle = lambda a,b: 0.5*a*b
arectangle = lambda l,d: l*d

while True:
 print("1.area of square")
 print("2.area of triangle")
 print("3.area of rectangle")
 print("4.exit")
 ch= int(input("Enter your choice(1,2,3)"))

 if(ch== 1):
    x= int(input("Enter the side of a square:"))
    print("area of square is :",asquare(x))
 if(ch==2):
    a= int(input("Enter the height of the triangle:"))
    b= int(input("Enter the base of the triangle:"))
    print("area of the triangle is:",atriangle(a,b))
 if(ch==3):
     l= int(input("Enter the height of the rectangle:"))
     d= int(input("Enter the breadth of the triangle:"))
     print("area of the triangle is:",arectangle(l,d))
 if(ch==4):
     break

    
  
  