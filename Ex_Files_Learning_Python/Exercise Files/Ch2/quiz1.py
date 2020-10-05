# Question 1 of 12
# What code should come instead of the ??? placeholders to have a function that
# takes the amount of local currency and a varying number of exchange rates,
# and prints the value of the currency at each provided exchange rate?
# def Calc(???):
#     for i in rates:
#         print(???)
# answer: currency,*rates; currency*i

# my practice:
# rates = [0.2, 0.6, 0.3]
# def Calc(currency,rates):
#     for i in rates:
#         print(currency * i)
# Calc(1,rates)

# Question 2 of 12
# You have an existing class Simple() that returns the sum of two numbers
# using its Add(x,y) method. How can you leverage it to build another class that
# calculates the inverse of the sum of two numbers?
# answer
# class Advanced(Simple):
#   def Inverse(self,x,y):
#     return (1/Simple.Add(self,x,y))


# Question 3 of 12
# What code will you need to place instead of the ??? placeholder for the script to print '3'?
# a=1
# b=2
# def func():
#         ???
# func()
# print(b)

# answer:
# global b
# b=a+b

# Question 4 of 12
# This code has three critical issues. Which is not actually an issue?
# def main:
# print(hello!)
# The function must be defined with the keyword 'func', not 'def'.

# Question 5 of 12
# In Python, what is the correct way to develop a class called Person that has parameters in the initialize function called name, age, and sex?
# answer:
# class Person:
#   def __initialize__(self, name, age, sex):
#     self.name = name
#     self.age = age
#     self.sex = sex


# Question 6 of 12
# What will the following script print?
# def inc(a, b=1):
#     return (a + b)
# a = inc(1)
# a = inc(a, a)
# print(a)
# answer:
4

# Question 7 of 12
# You need to set the annual payment in one function and print the respective monthly payment in a separate function. How would you fix the suggested code to work properly?
# def SetAnnual():
#   annual=10000
# def PrintMonthly():
#   print("Your monthly payment is "+annual/12+" USD.")
# SetAnnual()
# PrintMonthly()

#anwer:

# def SetAnnual():
#   global annual
#   annual=10000
# def PrintMonthly():
#   print("Your monthly payment is "+str(annual/12)+" USD.")
# SetAnnual()
# PrintMonthly()

# Question 8 of 12
# Which code snippet can you use to print the number of digits in the number variable? You can assume this number is always positive and always less than 10,000.
# number = 66
# if (number>=1000):
#     print(4)
# elif (number>=100):
#     print(3)
# elif (number>=10):
#     print(2)
# else:
#     print(1)

# Q9:Which alternative code is logically equivalent to the code below?
# max=x if (x>y) else y
# answer:
# max=y
# if (x>y):
#     max=x

# Question 10 of 12
# Which function will return the sum of the first item in the data list and every tenth item after?
# anwer：
# data = range(100)
# def Sum10th(data):
#     sum = 0
#     for i,d in enumerate(data):
#         if (i%10==0): sum = sum+d
#     # return sum
#     print(sum)
# Sum10th(data)

# Question 11 of 12
# Why is the code below often added to a Python program file?
# answer:
# It executes the main() function only if this file is executed as the main program.
# The __main__ variable will not be set based on the executing entity,
# but based on whether this is the main program.
# if __name__ == "__main__":
#     main()

# Question 12 of 12
# Which real-world scenario is best described as a standard while loop?
# answer: Start reading a book, and stop after reading a certain number of pages.