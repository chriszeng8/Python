# Difference between list

# 1. List: 
# A linear collection of values indexed by integers. 
# like Pringles (stacked nicely on top of each other)

# 2. Dictionary:
# A bag of values (unordered) with its label
# Dict needs a label
# Label in the context of dictionary is called key.

# Dictionary:
# Python's most powerful data collection.
# Dictionary allows us to do fast database-like operations in Python.

# In other languages, dictionary is also called as:
# Keys =:
# Associative array - PHP/Perl
# Property Map or Hashmap - Java
# Property/attribute bag - C#


# Create a dict (key:value pairs)
# 'candy', 'coke', 'Pringle' are keys
# 1.2, 2.5, 2.9 are values
PriceList=dict()
PriceList['candy']=1.2
PriceList['coke']=2.5
PriceList['Pringles']=2.9

print PriceList

PriceList['Pringles']=PriceList['Pringles']+0.5
print PriceList

# Listing do not have orders
# it is using hashing to decide the label orders

# Rather than using dict().
EmptyDict={}
EmptyDict['a']=1
EmptyDict['b']=2
print EmptyDict


# Think dictionary as a frequency counter!!
# count most common names/words


# Python does not allow us to reference a key before it exists.
# Solution is the " in " operator
aaa=dict()
# is the string 'a' a key in the current 
print 'a' in aaa
aaa['a']=1
print 'a' in aaa


###  
print 'What does y in x iterator throught?'
x=dict()
x['a']='aaa'
x['b']='bbb'
# ...
# question: for y in x, what does the for loop iterate through
for y in x:
	print y
# answer: it iterates through keys.

# Word count program in Python
WordFile=open('romeo.txt')
WordCount=dict()
for line in WordFile:
	words=line.split()
	for word in words:
		if word not in WordCount:
			WordCount[word]=1
		else:
			WordCount[word]=WordCount[word]+1
WordFile.close()
print WordCount


# This procedure above is very common that there is defined method.
# get method in dictionary
# what get does
dict_name=dict()
key_name='a'
#
value_if_key_not_existent=0
# either create using default value or pull out value corresponds to this key
print dict_name.get(key_name,value_if_key_not_existent)

# get is the same as:
name='a'
if name in dict_name:
	print dict_name[name]
else:
	print 0


dict_name['a']=1
if name in dict_name:
	print dict_name[name]
else:
	print 0

# the 4 line above is equal to the single line below:

print dict_name.get(key_name,value_if_key_not_existent)

#simplified 
WordFile=open('romeo.txt')
WordCount=dict()
for line in WordFile:
	words=line.split()
	for word in words:
		WordCount[word]=WordCount.get(word,0)+1
		# either create or update
WordFile.close()
print WordCount


# looping through dictionary:
# take the label successively.
for key in WordCount:
	print key, WordCount[key]


# Convert dictionary into a list
# keys and values are corresponding
key_list=list(WordCount)
key_list2=WordCount.keys()
Val_list=WordCount.values()

# tuple: key value map
tuple_list=WordCount.items()

print key_list
print key_list2
print Val_list
print tuple_list

# Two iteration variables:
for aaa,bbb in WordCount.items():
	print aaa,bbb

