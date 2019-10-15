#words = ["Lol", "Kek", "Cheburek"]
#print(sum(words)) 


#how work sum
# a=[1,2,3]
# temp = 0
# temp+=a[0]
# temp+=a[1]
# temp+=a[2]

x1= int(input())
y1= int(input())
x2= int(input())
y2= int(input())


if (x1+2 == x2 and y1+1==y2) or (x1+2 == x2 and y1-1==y2) or (x1-2 == x2 and y1+1==y2) or (x1-2 == x2 and y1-1==y2) or (x1+1 == x2 and y1+2==y2) or (x1+1 == x2 and y1-2==y2) or (x1-1 == x2 and y1+2==y2) or (x1-1 == x2 and y1-2==y2):
    print("YES")
else: 
    print("NO")