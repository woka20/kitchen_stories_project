#Ini pencetak hello world

#print("hello world")


#Integer
myint=7
print(myint)
print(type(myint))

#Float
# myfloat=7.0
# print(myfloat)
# print(type(myfloat))

myfloat=float(7)
print(myfloat)
print(type(myfloat))

#Strings
print(type('hello'))
print(type("hello"))


print("=============================================================")
one=1
two=int(2.0)

print(one+two)
print(type(one+two))

print("========================================================")
#string

hello="hello"
world="world"
hello_world=hello+" "+world
print(hello_world, type(hello_world))

print("==========================================================")
w=str(1)
x=str(int(2.0))
hello="hello"

print(w+x+hello)

print("==========================================================")

ast="*"*10
print(ast)

print("==========================================================")

a,b=7,9
print(a,b)

print("==========================================================")
a,b,c=7,9,"halo"

print(a,b,c)

print("=========================================================")

mylist=[]
mylist.append(1)
mylist.append('2')
mylist.append(3)

print(mylist)
print(mylist[2])
print(len(mylist))
print("=========================================================")

for element in mylist:
    print(element)
print("=========================================================")
for i in range(0,len(mylist)):
    print(i)
print("==========================================================")

#Arithmetic

a=5
t=2
L=(a*t)/2
print(L)

print("==================================================")

#Boolean

x=True
y=True
print(x)
print(y)


t=6>7
u=6<7
print(t,u)

print("======================================================")
#Condition

hour=5
if hour>=10:
    print("masih pagi")
elif hour>=8:
    print("sudah siang")
else:
    print("subuh")
print("=======================================================")
#Loops

primes=[2,3,5,7]
for i in primes:
    print(i)

print("=======================================================")

#while
count=5
while count>0:
    print(count)
    count=count-1
print("======================================================")

#Break=KeluarLoop&Continue=SkipPutraranIterasiSaatItu
x=3
for i in range(5,0,-1):
    if i==x:
        continue
    print(i)
count=5
# while count>0:
#     print(count)
#     if count==3:
#         continue
#     count=count-1
print('=====================================================')

