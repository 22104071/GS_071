#Ans1
A='Python is a case sensitive language'
print(len(A))
print(A[::-1])
b=A[9:26]
print(A[9:26])
print('Python is a %s language'%('object oriented'))
print(A.index('a'))
print(A.replace(' ',''))
#Ans 2
ABC=str(input("Enter your name:"))
SID=int(input("Enter your SID:"))
XYZ=str(input("Enter your Department:"))
Cg=9.9
print('Hey', ABC, "here","\nMy SID is",SID, "\nI am from",XYZ ,"Department and my CGPA is",Cg)
#Ans 3
a=56
b=10
print(a&b)
print(a|b)
print(a*b)
print(a<<2)
print(b<<2)
print(a>>2)
print(b>>4)
#Ans4
n1=int(input('Enter the First no. :'))
n2=int(input('Enter the Second no. :'))
n3=int(input('Enter the Third no. :'))
if (n1>n2) and (n2>n3):
    print('Greatest:',n1)
elif(n2>n1) and (n2>n3):
    print('Greatest:',n2)
else :
    print('Greatest:',n3)
#Ans 5
A=str(input('Enter the statement:'))
if ('name' in A):
    print('Yes')
else:
        print('No')
#Ans 6
s1=int(input('Enter the First length of ∆. :'))
s2=int(input('Enter the Second length of ∆. :'))
s3=int(input('Enter the Third length of ∆. :'))
if (s1<(s2+s3)):
    print('Yes')
elif(s2<(s1+s3)):
    print('Yes')
elif(s3<(s1+s2)):
    print('Yes')
else:
    print('No')    
