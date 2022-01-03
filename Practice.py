# type function

# name = "dhruv"
# age = 19
# complexNumber = 2 + 3j
# print(type(name))
# print(type(age))
# print(type(complexNumber))

# Operators

# a = 3
# b = 5
# #  ** -> power
# # print(a**b)
# #  // gives quotient
# print(a//b)
# print(b//a) 

# input from user

# a = input('Enter your age')  # The input function takes string only so entered age is a string.
# print(type(a))
# b = int(input('Enter your age'))  # The input function takes string only so entered age is a string.
# print(type(b))


# conditional statements

# age = 16
# if age>=18:
#     print("you are an adult")
# elif age>13 & age<18:
#     print("teenager")
# else:
#     print("you are a kid")
# print("kjntsk")

# Range function

# a = range(10)
# print(a)
# b = range(3,10)
# print(b)
# c = list(range(2,8))
# print(c)

# Loops

# n = range(7)
# for i in n:
#     print(i , end= " ")

# n = 5
# while n>0:
#     print(n)
#     n-=1


# Strings
# for multi lines string we use triple inverted comas
# address = ''' gsg
# fdgdf
# fdg '''
# print(address)

# name = "dhruv"
# print(name[0])
# print(name[4])
# print(name[-1])

# slicing(substrings)
# print(name[0:2]) #first index is inclusive and 2nd index is exclusive
# print(name[0:5:2]) #last index is the jump between elements, dafault value is 1.
# print(name[::-1]) 
# print(name[-1:0:-1]) 

# concatenation
# a = "abc"
# b = "def"
# # c = a+b
# # d=2*a //abcabc
# # print(c)
# print(d)

# a = "abc"
# for i in a:
#     print(2*i)

# Functions in String
# s = "abcde"
# print('s.isalpha', s.isalpha())
# print('s.isdigit', s.isdigit())
# print('s.islower', s.islower())
# print('s.isupper', s.isupper())

# print(s.lower())
# print(s.upper())

# x="    fdgd     "
# print(x.lstrip()) #removes left side spaces
# print(x.rstrip()) #removes right spaces


# list -> they are mutable unlike strings.

# name = [1,2,3,'dhruv']
# print(name)
# print(name[-1])

# # sublist
# number = [1,2,3,4,5]
# # print(number[2:5])
# del number[0]
# print(number)

# list comprehension

# a = [x for x in range(10)]
# print(a)

# a = [x for x in range(10) if x%2==0]
# print(a)

# list methods

# a = [1,2,3]
# a.append(4)
# print(a)
# a.insert(1, 1.2)
# print(a)
# a.pop(0)
# print(a)

# a = [2,3,1]
# a.sort()
# print(a)

# list functions
# a=[2,5,3,6]
# # print(len(a))
# # print(max(a))
# # print(min(a))
# # print(sum(a))

# for i in a:
#     print(2*i)

# x = "dhruv"
# print(list(x))

# tuples-> they are immutable

# a= ('A', 'B', 'C')
# print(a)
# # We have same functions in tuple as in lists.

# Sets -> duplicate elements are not there and there is no indexing.

# a={1,2,3,4,3,4}
# print(a)

#Dictionary -> key-value pair is stored

# marks = {"Chintu":34, "Pintu":45, "Mintu":99, 23:58}
# print(marks)
# #we use key instead of index
# marks["Rohit"]=67
# marks["Chintu"]=54
# print(marks["Mintu"])
# print(marks)

# squares= {1:1, 3:9, 5:25, 7:49}
# for i in squares:
#     print(squares[i])

# Modules

# import math
#from math import *
# print(math.pi)

# import math as m
# print(m.pi)

#import only one module
# from math import cos, sin
# print(cos(0)) 
# print(sin(1.57))

# User Defined Functions

# def greet():
#     print("Hello")
# greet()
# greet()

# def greet(name):
#     print("Good Morning", name)

# greet("Dhruv")

# def sumoflist(a):
#     print("Calculating...")
#     return sum(a)

# marks = [34,54,12,65]
# total = sumoflist(marks)
# print(total)


