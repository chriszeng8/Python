# Crash Course in Python
############# LIST #############
# 1. hetergenous list is allowed in python (like R)
hetergeneous_list=["A",1,True]
print hetergeneous_list

# 2. list within list is allowed in python (like R)
list_of_lists=[hetergeneous_list,[]]
list_of_lists2=[hetergeneous_list,["A",4]]
print list_of_lists
print list_of_lists2
print list_of_lists2[1][0]

# 3. concatenate strings
x = [1,2,3]
x.extend([4,5,6])
# note the difference between append and extend:
# append is for a single element
y = [1,2,3]
y.append([4,5,6])
print x
print y

# 4. upack
x,y=[1,2]
_,v=[1,2] # underscore if do not want to return that variable

print x,y,v

############# TUPLE #############
# 5. tuple (immutable cousins of list)
my_list=[1,2]
my_tuple=(1,2)
my_tuple2=1,2 #parathesis or without parathesis are both tuples.
print 'tuple: '+str(my_tuple)
print 'tuple: '+str(my_tuple2)
# return multiple values
# tuple is convinent to return multiple values
def sum_and_product(x,y):
	return (x+y),(x*y)
print "\nsum and product are: "+str(sum_and_product(2,3))
# way to swap element of tuple/list, this is considered an assignment process.
x,y=1,2
x,y=y,x
print '\n'+''+str((x,y))

########### DICTIONARY ###########
# 6. dict
empty_dict={}
empty_dict2=dict()
grades={"Paul":98,"Chris":99}

# unlike list/tuple, you use keys to extract element
print grades["Chris"]

try:
	print grades["NoOne"]
except:
	print 'Cannot find NoOne'

# returns a default value when such element cannot be found
print grades.get("NoOne")
print grades.get("NoOne",0)

# ways to add element that did not exist in the dictionary
grades["NoOne"]=grades.get("NoOne",1)
print grades


########### DEFAULTDICT ###########
# default dict
from collections import defaultdict
WordFile= open('romeo.txt')
WordCount= defaultdict(int) #int() produces 0
Words = WordFile.read().split()
for word in Words:
	WordCount[word]+=1
	# either create or update
WordFile.close()
print WordCount
print WordCount

dd_list=defaultdict(list)
dd_list[2].append(1)
print dd_list

########### COUNTER ###########
# COUNTER counts the frequency of elements in a list (similar to table in R)

from collections import Counter
WordFile= open('romeo.txt')
words=WordFile.read().split()
#  ONE LINER FOR WORD COUNT !!!!!
word_counts = Counter(words)
WordFile.close()
print word_counts
#  MOST_COMMON FUNCTIONS !!!!!!
print '\n5 Most Common Words:'
for word,_ in word_counts.most_common(5):
	print word

############ SET ############
# 1. first reason
# "in" is a fast operation on set (much much faster on large dataset)
print "bb" in words      # False, but have to check every elements
print "bb" in set(words) # False, much faster to check
# 2. second reason
# find distinct items
print set(words)

# Python uses None to indicate a nonexistent value
# It is similar to other language's null (e.g., null in R)
m=None
print m==None
print m is None


############ FALSE ############

# The following value are all "Falsy" when converted to/treated as boolean
# None/0 value, empty string, empty collection (i.e., list/dict/set)

# scalar 0, or None value
print '\nDifferent Falses:'
print bool(False)
print bool(0)
print bool(0.0)
print bool(None)
# empty string
print bool("")
# empty collection
print bool([])
print bool({})
print bool(set())

# All and Any function
print '\nall and any:'
print all([1,False,"a"])
print all([1,True,"a"])
print all([1,False,"a"])
print all([1,True,"a"])