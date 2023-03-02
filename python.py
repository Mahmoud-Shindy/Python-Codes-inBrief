
"""# average of N numbers 
Num = int(input("how many numbers do u want ?"))
total_sum= 0
for n in range(Num):
    numbers=float(input("enter any number"))
    total_sum += numbers
avr = total_sum/Num
print("the average of the numbers u entered is : ",avr)"""

"""# how to get the current username 
import getpass
print(getpass.getuser())"""

"""# how to access environment variable in python 
import os
print(os.environ)"""

"""# how to do a profile in python script
import cProfile
def sum():
    print(1,3)
cProfile.run('sum()')"""

"""# how to find the virsion of python 
import sys
print(sys.version)
print(sys.version_info)"""

"""#how to find the area of a circle
#constant = 3.14
from math import pi
r = float(input("please enter the \"R\" "))
Area = pi * r**2
print(Area)"""

"""#list
li=[]
for n in range(5):
    l= int(input("enter a number"))
    li.append(l)
print(li)"""

"""#how to extract an extension of a file name
file_name = input("enter any file name")
file_extension = file_name.split('.')
print(repr(file_extension[-1]))"""

"""#how to print first & last of list
colors =["red","blue","yellow","green"]
print(" %s %s "%(colors[0] , colors[-1]))"""

"""#how to sample an exam
exam_date=(2,3,2023)
print("the exam date is: %i / %i / %i "  %exam_date)"""

"""#how to in a number n and compute it in n+nn+nnn
number=int(input("enter a number"))
n1=int("%s"%number)
n2=int("%s%s"%(number,number))
n3=int("%s%s%s"%(number,number,number))
print(n1,"+",n2,"+",n3)
print(n1+n2+n3)"""

"""#how to print the decument of any built_in function
print(float.__doc__)
print(int.__doc__)"""

"""#how to print the calendar of a year month
import calendar
year=int(input("please enter the year"))
month=int(input("please enter the month u need in this year"))
print(calendar.month(year,month))"""

# how to print a string without escaping in python
print("""hi 
            this is
                    mahmoud
                            shindy
                            
bye""")

"""#how to calculate the numbers of days between two dates
from datetime import date
first_date=date(2015,9,1)
second_date=date(2021,6,1)
delta=second_date - first_date
print(delta.days)"""

"""#how to find the area and volume of a sphere
from math import pi
radios=float(input("please enter the radios of the sphere: "))
volume=float(4/3)*pi* radios**3
area=4*pi*radios**2
print("the volume is : ",volume , "\n the area is : ",area)"""

"""#sum of 3 numbers , if the 3 numbers is equal then sum thrice of their sum
def sum_thrice(x,y,z):
    sum=x+y+z
    if x == y == z:
        sum= sum*3
    return sum
print(sum_thrice(3,3,3))"""

"""#how to find if number given is odd or even
def even_odd(n):
    print("the number u entered is : ",n)
    if n%2 ==0 :
        print(n," is even")
    else:
        print(n," is odd")
    
even_odd(1088)"""
"""**************************************************************************************************************************"""
"""************************DataTypes******************************"""
"""str                       
int,float,complex         
list,tuple,range          
dict                      
set,frozenset    
bool
bytes,bytearray,memoryview"""

"""***************************Slicing a string*********************************"""
"""name='mahmoud'
print(name[2:5])
"""
"""***********************************loops*************************************"""

"""for item in range(6):
    if item == 3: 
        break
    print(item)"""
"""**************************************file handling*****************************"""
"""with open("../python/child.py")as file:
    for line in file:
        print(line)"""
"""***************************************arthemetic********************************************"""
"""result = 10 + 30 # => 40
result = 40 - 10 # => 30
result = 50 * 5  # => 250
result = 16 / 4  # => 4.0 (Float Division)
result = 16 // 4 # => 4 (Integer Division)
result = 25 % 2  # => 1
result = 5 ** 3  # => 125
"""
"""***********************************  f -  Strings  (there is alot in f string to search  *****************************"""
"""name="mahmoud"
print(f'{name} shindy')

num=15
print(f'15+{num}={num+15}')

f'{200:b}'           #binary type
f'{200:o}'           # octal type
f'{200:X}'           #hexadecimal type 

"""
"""*****************************************numbers***************************************"""
"""x=20
y=20.5
z=5j
print(type(x))
print(type(y))
print(type(z))

"""
"""****************************************lists & tuples &sets************************************************"""
"""list1=["cat","dog","mouse"]
list2=[1,2,3,4,5,6]
list3=[True,False,False,True]
list4=list((1,2,3,4,5,6))
list5=list(range(1:11))
del li[0]    #to delete special index value
print(lis)

tuple=(1,2,3,4)
tuple0=tuple((5,4,8,7))

set1={"a","c","f"}
set2=set(("a","d","f"))
"""
"""*******************************************dictionary********************************************"""
"""a={
    "one":1,
    "two":2,                               #here dictionary is ( keys & values)
    "three":3
}
print(a.keys())
print(a.values())
a.update({"four":4})
print(a.keys())"""
"""*******************************************   HEAP   ***********************************************"""
"""import heapq
list=list((5,7,4,3,1,9,2,14,26,21))
#list=[-val for val in list]  # this to make max value printed 
heapq.heapify(list)
print(list)

heapq.heappush(list,18)                            #heap is a binary tree
heapq.heapify(list)                                #usful in finding the max / min value fast and easy
print(list)
x=heapq.heappop(list)
print(x)
print(-x)"""
"""************************************************   Queue And Stacks   ***********************************"""
"""from collections import deque
que=deque([1,2,3])
que.appendleft(0)
que.append(4)
print(que)

x=que.pop()
y=que.popleft()
print(x)
print(y)
print(que)"""
"""**************************************************  for **********************************************"""
"""for c in "foo":
    print(c)
    """
"""*************************************************   Multiple copies ************************************"""
"""s = '===+' 
n = 8
print(s * n)"""
"""************************************************    check string ****************************************"""
"""name="mahmoud"
result=name in "mahmoud ahmed bassam"
result1=name not in "mahmoud ahmed bassam"
print(result)
print(result1)"""
"""**************************************************** Format() method ************************************************ """

"""print("my name is {name} , i am {age}".format(name="mahmoud",age=26))
print("i am {} my age is {}".format("mahmoud",26))"""

"""*********************************************** join (just strings) ********************************************************"""
"""j="#".join(["1","2","3"])
print(j)"""

"""************************************************** end with ********************************************************"""
"""r="!"
q= r in "mahmoud!"
print(q)

b = "hello !".endswith("!")
print(b)"""

"""*************************************************** lists (extend , sort() , reverse() , count()) ************************************************** """
"""list=[1,2,3,4,5,6]
list.extend([7,8,9])
print(list)
list11=[2,8,6,4,7,9,3,2,5]

list11.sort()
print(list11)
list11.reverse()
print(list11)

x=list11.count(2)
y=list11*3
print(x)
print(y)
"""
"""***************************************************   one line if condition *************************************************"""
"""a=200
b=300
x= "b is begger" if b>a else "a is begger"
print(x)"""
"""*********************************************************  loop enumerate  *****************************************************"""
"""list=[55,44,88,66,22]
for i,v in enumerate(list):
    print(i,v)"""
"""***********************************************************  Break  ********************************************************"""
"""x=0
for n in range(10):
    x=n*10
    if n==5:
        break   # or type (continue) 
    print(x)"""
""" ******************************************************** %s %d ************************************************* """

"""n=20
b=50
print("%s numbers is  that is it %d"%(n,n)) """
"""**********************************************************  Positional arguments ***************************************"""
"""def varargs(*args):
    return args

varargs(1, 2, 3)"""
""" ***************************************************  Keyword arguments ************************************************"""
"""def keyword_args(**kwargs):
    return kwargs
keyword_args(big="foot", loch="ness")
"""
"""************************************************************** Swap() ****************************************************"""
"""def swap(x,y):
    return (y,x)
    
x=2
y=5
x,y = swap(x,y)
print(x,y)"""
"""*************************************************************** function with default value ***********************************"""

"""def val(x,y=4,z=4): #elements which will take a default value must be in the right (last items)
    return x+y+z
z=val(4)
print(z)"""
"""********************************************************************  short module name ***********************************"""
"""import math as m
"""
"""******************************************************************  classes *********************************************************"""
class Animall:
    def __init__(self,name,leg):
        self.name=name
        self.leg=leg
    def run():
        print("escap if u can")    

class wild(Animall):
    def deserrt():
        print("lets hide")
        super().run()
obj_1=wild.deserrt()
obj_2=wild("lion",4)
obj_2=wild()

print(obj_2.name,obj_2.leg,obj_2.deserrt())




