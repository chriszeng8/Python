# list can store variables of different types.
# Extract 


ListA=['a','b',3]
print 'Mixed Type List: ',ListA

# Nested List is also allowed
ListB=[1,[2,3],4]
print 'length of list B: ',len(ListB)
for i in ListB:
	print (i)
print '\n'

# NO NO NO NO
# Strings are immutable
# When we are applying lower function to a string, we are getting a copy of the string.
# That's because strings are not mutable.
Fruit='Banana'
print Fruit[0],'\n'
#Fruit[0]='b'
# There will be an error here.

# YES YES YES YES
# List is mutable.
lotto=[1,2,4,'chris',8]
print len(lotto)

print range(4)

# Concatenating lists
ListC=[1,2,3]
ListD=['a','b','c']
ListE=ListC+ListD
print ListE

# Slicing: Up to but not including the last index
# List[a:b]
# start at element a and finish at b-1 (excluding b)
# starting at a upto but not including b th element

# List[:b]
# starting from 0, going upto but excluding element b
Num=['a','b','c']

# Create an empty list
x=list()
# what can we do with it?
print type(x)
# what can we do with this data type?
print dir(x)

# Build a list from scratch
# Append

x.append('a')
x.append(1)
print x


# ask if an item is in the list?
# is 'a' in list x
print 'a' in x
print 2 in x
print 2 not in x
print 1 in x

# sorting in list: (SORT YOURSELF!!)
# NOTE: .sort function does not make a copy of ordered list, it actually alter the original list!
friends=['Chris','Adam','Brent','Dwane']
friends.sort()
print friends

# functions in list
num=[1,2,3,0,6]
print len(num)
print max(num)
print sum(num)

################################# SPLIT #################################
# split function in python 
Str='hello I am really happy to be here.'
ListStr=Str.split()
print 'sentence length: ',len(ListStr)
print ListStr

####### SPLIT treats lots of spaces the same as a single space  #########
HelloStr='hello world          life is     good'
hellosplit=HelloStr.split()
print 'Sentence length: ',len(hellosplit)
print hellosplit

# specifying other parameters
HelloStr2='hello;world;life;is;good;'
hellosplit2=HelloStr2.split(';')
print 'Sentence length: ',len(hellosplit2)
print hellosplit2

# import regular expression
print '\nSplitting using multiple delimiters:'
import re
a='Beautiful, is; better*than\nugly'
print a
print 'Split string list:',re.split(';|,|\*|\n',a)


# Compare to using string function, this is a lot easier
# Extracting information easily
# continue in a for loop
print '\nEmail:' 
ReadFile=open('madeupdata.txt')
for line in ReadFile:
	if line.lower().startswith('from '):
		words=line.split()
		print words[1]
ReadFile.close()

# double spliting
print '\nDomain:' 
ReadFile=open('madeupdata.txt')
for line in ReadFile:
	if line.lower().startswith('from '):
		words=line.split()
		email=words[1]
		domain=email.split('@')
		print domain[1] 
ReadFile.close()


# Extract unique words
#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list 
#of words using the split() function. The program should build a list of words. For each word on 
#each line check to see if the word is already in the list and if not append it to the list. When
#the program completes, sort and print the resulting words in alphabetical order.
fh = open('romeo.txt')
lst = list()
for line in fh:
	words=line.split()
	for word in words:
		if not word in lst:
			lst.append(word)
lst.sort()
print lst


# You will parse the From line using split() and print out the second word in the line (i.e. the 
# entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if line.lower().startswith('from '):
        Str=line.split()
        print Str[1]
        count=count+1
print "There were", count, "lines in the file with From as the first word"
