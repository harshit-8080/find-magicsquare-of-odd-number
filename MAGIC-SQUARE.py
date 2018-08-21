def magicsquare(n):
 square=[]
 for i in range(n):
        l=[]
        for v in range(n):
            l.append(0)
        square.append(l)
 count=1
 i=n//2
 j=n-1
 while count<=n*n:
     if i==-1 and j==n:
         j=n-2
         i=0
     else:
          if i<0:
              i=n-1
          if j==n:
              j=0
     if square[i][j]!=0:
           j=j-2
           i=i+1
           continue
     else:
        square[i][j]=count
        count+=1
     i=i-1
     j=j+1
 for i in range(n):
         for j in range(n):
             print(square[i][j],end=" ")
         print()
 print("the magic number for this magic-square is=",n*(n**2+1)/2)            
             
def play():
 l=int(input("ENTER A ODD NUMBER TO FIND MAGIC SQUARE"))
 if l%2!=0:
    print("THE MAGIC-SQUARE OF",l)
    magicsquare(l)
 else:
    print("YOU HAVE ENTER",l,"WHICH IS EVEN NUMBER PLEASE TRY TO ENTER ODD NUMBER")
    print("for ex:- if you enter 3 which is odd number then its MAGIC-SQUARE IS")
    magicsquare(3)         
print("*-*-*-*-*-*WELCOME HERE*-*-*-*-*-*-*")
print("ENTER YOUR---",end=" ")
name=input()
print()
print("hey! how are you--",name)
print("------------------------------------------------")
print("DO YOU WANT TO ABOUT MAGIC SQUARE?")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
r=int(input("PRESS 1 FOR KNOW ABOUT SQUARE MAGIc*-*-*-*-*-*-* OR*-*-*-*-*-*-*-*PRESS 0 NOT INTERESTED"))
while(r):
    print('1.It is a matrix of n*n "WHERE N IS ODD NUMBER".')
    print('2.In this matrix when you add its element either horizontally or vertically and even diagonally----"THE VALUE IS SAME"')
    print("DO YOU WANT TO FIND A SQUARE MATRIX------------")
    l=int(input("press 1 to FIND MAGIC-SQUARE or press 0 to EXIT----"))
    if l==1:
        play()
        break
    else:
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-THANKU YOUR VISITING*-*-*-*-*-*-*-*-**-*-*-**-*-*-*-*-")
        break
else:
    play()

