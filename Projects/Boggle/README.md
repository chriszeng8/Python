#Boggle
##Background

Boggle is a word game played on a 4x4 grid of letters in which the aim is to create words from the 16 letters. The letters are arranged in a random order, and players must form as many words as possible. 

Restrictions on the words are that character length must be greater than, or equal to, 3 and each letter 
can be used only once.

##Problem Description

The task is to write a program that produces an output of all possible words when given a dictionary 
and a set of Boggle boards. You will need to identify all the words that can be constructed from the  available letters. If a letter occurs twice in the board, you can use that letter twice in a word. If a word contains more than one ‘e’ (for example ‘meet’), you’ll need one ‘m’, one ‘e’, another ‘e’ and a ‘t’ in your input string – therefore the input string of ‘atamabebcdrremjh’ would satisfy this match. 

Note, it is not required that the letters be sequential on the board. You can also assume that matches  are not sensitive to case. 
A dictionary file is provided here, and 100 Boggle boards were also provided in a file.
(Note that all files have UNIX line endings)

* The dictionary file is one word per line -- word_dictionary
* The Boggle boards are in the file -- input.txt
* An example output file is supplied -- output.txt
* Each Boggle board will be a random string of 16 characters, e.g. ‘abcdefghwxyzijkl’. 
* The distribution of characters in this string will be in line with the distribution of characters in  the dictionary. 

##Constraints

The program must accept 2 positional arguments:
1. The path to an input file -- use the supplied input.txt as an example. 
2. The path to the word dictionary – use the supplied word_dictionary for testing.

The program must output a file in the exact format specified in output.txt.

Language specific constraints:

* Python Python 2.7.3 or later, 3.x is acceptable 
* If using 2.7, print statements should be in python 3 style: print (a). NOT print a 
* Nothing is available to you except the python standard library