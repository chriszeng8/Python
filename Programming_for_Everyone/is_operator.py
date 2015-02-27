# This is to illustrate the difference between "is" and "==" operator
# "is" checks whether two objects are the same objects
x = [1, 2, 3]
y = [1, 2, 3]
print 'x=',(x)
print 'y=',(y)
print id(x)
print id(y)
# Conceptually, it is equivalent to memory address. id(x) returns an unique id for that object
# during the lifetime of the 
print 'x is y? -->',(x is y)
print 'x == y? -->',(x == y)
x=y
print id(x)
print id(y)
print 'After x=y'
print 'x is y? -->',(x is y)