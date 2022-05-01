#here are 4 ways to swap numbers in python

#1 using an extra variable
a = 10
b = 5
temp = a
a = b
b = temp
print(a)
print(b)

#2 using addition and subtraction
c = 12
d = 6
c = c+d
d = c-d
c = c-d
print(c)
print(d)

#3 using the circumflex
e = 14
f = 7
e = e^f
f = e^f
e = e^f
print(e)
print(f)

#using commas
g = 16
h = 8
g,h=h,g
print(g)
print(h)