# Useful String Functions

# 1. lower()/upper()
# 2. replace('old','new')
# 3. lstrip(): strip whitespaces at the beginning
# 4. rstrip(): strip whitespaces at the end
# 5. strip(): strip all whitespaces
# 6a. find('char'): return the position of the found character (starting from 0)
# 6b. find('char',start pos): return the position of the found character (starting from 1)
# find() function is useful for parsing strings

s='Monty Python'
print 'whole expression:';
print s[:]
print 'truncated 6 to 12: ';
print s[6:12]
print 'Mighty Python is forgiving! Truncated 6 to 100 (even max is 12): ';
print s[6:100]
# beginning to 5
print s[:5]
# 6 to the end 
print s[6:]

# lower case/upper case
print s.lower()
print 'Random String LOLOLOL'.lower()
print 'Random String LOLOLOL'.upper()

# search a string
fruit='banana'
pos=fruit.find('na')
print pos

# replace function
fruit='banana'
newfruit=fruit.replace('b','c')
print newfruit

# strip white space
# similar to 
Astring='    Hello Bob       ' 
newlStr=Astring.lstrip()+'.' #remove white space to the left
print newlStr
newrStr=Astring.rstrip()+'.' #remove white space to the right
print newrStr
newStr=Astring.strip()+'.'  #remove white space at both ends
print newStr

# check prefix
Afruit='Hello banana'
print Afruit.startswith('H')
print Afruit.startswith('Hello')
print Afruit.startswith('hello')

# Working example 
data1=['From helloworld1@aucklanduni.ac.nz Sat Jan 1', 'From helloworld2@cornell.edu Sat Jan 1', 'From helloworld3@gatech.edu Sat Jan 1' ]
print data1
username=[]
# we would like to exactract the user name
for i in range(len(data1)):
	start_pos=data1[i].find(' ')
	end_pos=data1[i].find('@',start_pos)
	extractUser=data1[i][start_pos+1:end_pos]
	username.append(extractUser)
print 'User name: '
print username

domainname=[]
# we would like to exactract the user name
for i in range(len(data1)):
	start_pos=data1[i].find('@')
	end_pos=data1[i].find(' ',start_pos)
	extractDomain=data1[i][start_pos+1:end_pos]
	domainname.append(extractDomain)
print 'Domain name: '
print domainname