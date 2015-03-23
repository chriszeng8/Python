# Python is very succint in reading txt file.
fileName=('None_Smallest.py')
NewFile=open(fileName)
# Takeaway 1. NOTE: /n (newline symbol) is counted as 1 character!!!!

# Takeaway 2. File handle in python:
# when a file is stored in a file handle for read (i.e., NewFile in this case), 
# it can be treated as a sequence/vector of strings which are separated by \n.

# With Python's file handle, we can read lines of a file easily.
for cheese in NewFile:
	print cheese
print '\n'
NewFile.close()


################################################################################################
######################   PROPER WAY: use .rstrip() to remove /n  ###############################
# \n or blank are countered a white spaced, and can be stripped by using strip functions.
# !!!!!! Problem here, the new lines will cause a gap/blank line.
NewFile=open(fileName)
for cheese in NewFile:
	print cheese.rstrip()
print '\n'
NewFile.close()
################################################################################################

NewFile=open(fileName)
counter=0
# line counter
for cheese in NewFile:
	counter=counter+1
print 'Line Counter: ',counter,'\n'
NewFile.close()



# Condition on read string
NewFile=open(fileName)
# Takeaway 3. set if conditions within loop to print out useful information
for cheese in NewFile:
	if cheese.startswith('for'):
		print (cheese.rstrip())
NewFile.close()
	