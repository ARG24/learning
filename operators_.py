#operators
#1> ARITHMATIC OPERATORS

a=int(input("enter the value of a "))
b=int(input("enter the value of b "))
print("a+b= ",a+b)
print("a-b= ",a-b)
print("a*b= ",a*b)
print("a/b= ",a/b)
print("a**b= ",a**b)
print("a%b= ",a%b)


#2>relational operators
a=int(input("enter the value of a "))
b=int(input("enter the value of b "))
print("a<b= ",a<b)
print("a>=b= ",a>=b)
print("a==b= ",a==b)
print("a!=b= ",a!=b)


#3>asssignment operators
a=int(input("enter the value of a = "))
a+=5
a-=5
a/=5
a*=5
#a=a+5
print("a+=5",a)
print("a-=5",a)
print("a/=5",a)
print("a*=5",a)

#4>logical operators
true=1
false=0

print("true and false",true and false)#1*0
print("true or false",true or false)#1+0

#5>bitwise operators
print("5&3",6&3)
print("5|3",5|3)

#6>A identity operator
   #B membersjip operator

#A> identity :check wheteher data present in same memory location or not
a=int(input(" value of a= "))
b=int(input(" value of b ="))
print("a is b=",a is b )
print("a is not b =", a is not b )

#B>membership:check whether given term is present in string or not
s="welcome"
print("w in welcome =","w"in "welcome")
print("w in s = ","w"in s)
print("e i not in s =","e" not in s)
