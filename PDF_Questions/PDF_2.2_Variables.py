"""
#
# File            : PDF_2.2_Variables.py
# Created          : 18/01/2023 7:24 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     :
#
"""
# Question 1
print("\t" * 2 + "Title")
print("Hello")
print('hello world')
a = 5
b = 12.3456789
c = a + b
d = "A number ", +b
e = a + \
    b + \
    c
f = 2
g = a / f

print(a), print(b), print(c), print(d), print(e), print(f), print(g)

# Question 2
a = "^"
b = a * 47
print(b)
c = "<{0:45}>".format("")
print(c), print(c), print(c)
d = "<{0:10}Title{1:30}>".format("", "")
e = "<{0:5}A   Option a{0:28}>".format("", "")
f = "<{0:5}B   Option b{0:28}>".format("", "")
g = "<{0:5}C   Option c{0:28}>".format("", "")
h = "˅"
i = h * 47
print(d), print(c), print(c)

print(e), print(f), print(g), print(c), print(c), print(i)

# Question 3
# Question 3
# Consider the type of information and it’s structure for the following items.
# You are not asked to code anything here. Just consider the information:
# • ppsn                                • temperature in degrees
# • cao number                          • Miles travelled per day
# • Average collection of exam grades   • File path

# Question 4
# Carry out the following calculations. Why are these examples important?
# Answer: To learn the sequence the mathematical action ar done by the computer.
# Sequence: P – Parentheses.
# E – Exponentiation.
# M – Multiplication.
# D – Division.
# A – Addition.
# S – Subtraction.
print(6+8/2-1)
print(1+1-1+2/2)
print(1.1+5/2)
print(9.2/3)
print(1*2+3*5%4)
print(1+8%3*2-9)
print(6+(24%(16-11)))