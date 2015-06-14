# Regular Expression
# Notes taken from Programming for Everyone Lec 11.
# Chris Zeng
# June, 2014

#re.search: smarter version of find

#re.findall: a combination of find() and slicing: var[5:10]
# Starts From
import re
hand=open('mbox-short.txt')
for line in hand:
	line=line.rstrip()
	# if a line contains string "From"
#	if re.search('From',line):

	# if a line starts with string "From"
	if re.search('^From.*[A-Z].*\s',line):
		print (line)


# Patterns
# ^ start with 
# . (dot) matches ANY characters.
# * (asterisk) repeat the immediate previous character MANY times (>=0).
# + having the immediate previous character at least one or more times (>=1) (e.g., [a-z]+ means having a lowercase character at least once)
# /s space
# /S non-whitespace character

# For example: ^M.*:
# match any word STARTING with M followed some number of characters many times, then followed by :
# Results for ^M.*:
# X-Seive: asdfa
# XHellosadfs: asdfasf

# To find if something is there or not?
# re.search ()

# To extract information by combining the searching and parsing
# re.findall ()

# [abcd]
# OR operator:
# a single character that is either a, b, c or d.

# - dash is the range
# [0-9]+
# find any number that is between 0-9, and repeat more than one times


x='My favorite 3 numbers are 19, 24 and 333'
y=re.findall('[0-9]+',x)
print (y)

# if cannot find, return an empty string


## GREEDY matching (that push far as you can)
# The repeat characters (* and +) push outward in both directions
# to match the largest possible string
# note that x2 here has two possible strings that satistifes the pattern '^F.+:'
# that is
# 1. From:
# 2. From: Using the :
# .+ will greedily find the largest string.

x2='From: Using the :character'
y2=re.findall('^F.+:',x2)
print (y2)


## NON-GREEDY matching (that stops at the first find)
# ? Non-Greedy match
# stop as soon as you find the first/shortest matched string
x3='From: Using the :character'
y3=re.findall('^F.+?:',x3)
print (y3)

#\S+: think it as a stop mechanism to extract information before or after the immediate space
x4='From stephen.marquare@uct.ac.za Sat Jan'
y4=re.findall('\S+@\S+',x4)
print (y4)



# ( start of string extraction
# ) end of string extraction
# () only extract information within the parathesis.
# Parenthesis as a way to specify match the whole pattern, but only extract the part of information withint the ().
x5='From stephen.marquare@uct.ac.za Sat Jan'
y5a=re.findall('From (\S+@\S+)',x5)
# Match the whole string 'From stephen.marquare@uct.ac.za', but only extract the email part
domain=re.findall('\S+@(\S+)',x5)
user=re.findall('(\S+)@\S+',x5)
print (y5a)
print (domain)
print (user)

# ^ within [] means NOT
# [^ ] means non-blank characters
# '@[^ ]+' means all the immediate non-blank characters after the @
domain2=re.findall('@([^ ]+)',x5)
print (domain2)

#[0-9.]
# any character that is . or number 0-9



# How to match the signs in the string
# $ means matching the end of string with character ...
# what if we want to match "The price is $10.00" with dollar sign in it?
# '\' (backslash) is the soluation
xx='The prices is $10.00'
yy=re.findall('\$([0-9.]+)',xx)
print (yy)
