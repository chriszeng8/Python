# Tuples are very much like list
x=('Glen','Chris','Max')
print x[2]

# However, Tuples are IMMUTABLE.
# Like Strings.

# List mutable
y1=['A','B','C']
print y1[2]
y1[2]='D'

# string immutable
y2='ABC'
print y2[2]
try:
	y2[2]='D'
except:
	print "string is immutable" 

# TUPLEs:

# cannot overwrite
# cannot sort
# cannot reverse
# cannot append

# In summary, you cannot change it at all
print 'List:',dir(list())
t=tuple()
print 'Tuple:',dir(t)

# WHY???
# Good things about tuple:
# 1. Python will process it faster.
# When creating temporary variables (temporary list), we prefer to use Tuple instead.


# 2. double assignment 
(x,y)= (4,'fred')
# or without the parathesis
a,b= (4,'fred')
print x
print a

# Dict item return Tuples (key-value pair)
# e.g., [('a',2),('b',3)]
# d.items() returns a vector of Tuples

# 3. Comparable
# Lazy evaluation (not comparing all records)
# as soon as one of element in the tuple is less than the counterpart from the other tuple
print (0,1,2)<(5,1,2)
print (0,1,2000)<(0,2,2)


# Dict: sort by keys
# Note that dictionary are not displayed in sequence.
d={'a':10,'b':1,'c':22}
t=d.items()
print 'unsorted:',t
t.sort()
print 'sorted:  ',t

x , y = 3, 4
# Sorted in Python.
print y

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print days[2]

data=[1,3,2]
data.sort(reverse=True)
print data


d={'a':10,'b':1,'c':22}
t=sorted(d.items())
print 'sorted:  ',t

# Run in key sorted order.
for k,v in sorted(d.items()):
	print k,v

c={'a':10,'b':1,'c':1,'d':3}
tmp=list()
for k,v in c.items():
	#tmp.append(v,k) does not work somehow
	tmp.append((v,k))
print tmp

tmp.sort(reverse=True)
print tmp