# Chris Zeng, Feb 15, 2015
# Try ... Except
# operations within the TRY block is to say that, as a programmer,
# I know that things could go wrong in this block. If it goes wrong,
# jump straight to except block.

print 'This program will multiply your input integer by 10.'
test = raw_input("Enter an integer number:")  
try: 
   test = int(test)
   print 'Good, it\'s a Valid Entry' # Note that this helloworld will not be printed if the input is invalid.
except:  
   print "Invalid entry. Please enter an integer"
   quit()
result = test * 10  
print result  