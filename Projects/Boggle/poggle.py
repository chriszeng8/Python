# Boggle 
# Jan 23 2015, Chris Zhuo Zeng

def Boggle(input_path="input.txt",dict_path="word_dictionary"):
    from collections import Counter #collections is part of the standard library in python
    import os
    Input_file = open(os.path.expanduser(input_path)) # read in a input.txt file
    Dic_file=open(os.path.expanduser(dict_path)) # read in the dictionary file
    Output_file=open("output.txt","w") # output.txt file to be written
    
    Input_Words=Input_file.readlines() # read all lines from input.txt file
    All_Words=Dic_file.readlines() # read all words from the dictionary
    Dic_file.close() 
    Input_file.close()
    
    # Processing and filtering the imported dictionary:
    # Step 1. lowercase   
    # Step 2. remove replicates 
    # Step 3. remove words with less than 3 characters 
    
    # 1. lower-case all elements within the dictionary
    All_Words = [item.lower() for item in All_Words] 
    # 2a. a function that remove replicated items in a list
    def FindUnique(seq):
        seen = set()
        seen_add = seen.add
        return [ x for x in seq if not (x in seen or seen_add(x))]
    # 2b. find vocabulary list with repeated items removed (using FindUniqu function)
    All_Words=list(FindUnique(All_Words))
    # 3. Remove all words with length less than 3 letters
    All_Words=[i for i in All_Words if len(i) >= 4] 
    #len(i)>=4 because each word contains a space already
    
    Num_words=len(All_Words) # The number of filtered vocabularies
    Num_Inputs=len(Input_Words) # The number of input strings
    
    # Pre-process the dictionary file to construct a (row=number of words) x (col=26) matrix
    #Char_Matrix=np.zeros((Num_words,26))
    Char_Matrix=[[ 0 for i in range(26)] for j in range(Num_words)]
    print ('Initializing ...')
    for i in range(Num_words):
        # match the letter frequencies within a word against the 26 letters
        Char_Matrix[i]=map(Counter(All_Words[i]).__getitem__, map(chr, range(ord('a'), ord('z')+1)))
    Made_Word_Count=[]
    
    for i in range(Num_Inputs):
        CountW=0 # count number of vocabularies that can be found in the list
        Input_Char_Freq=map(Counter(Input_Words[i]).__getitem__, map(chr, range(ord('a'), ord('z')+1)))
        # check if all elements in temp list are greater than 
        for j in range(Num_words):
            if all(x >= y for x,y in zip(Input_Char_Freq,Char_Matrix[j])): CountW=CountW+1    
        Made_Word_Count.append(CountW)
        print ('Progress: '+str(float(i+1)/(Num_Inputs)*100)+'%')
    
    for i in range(Num_Inputs):
        Output_file.write("%s %s\n" %(Input_Words[i].strip(),Made_Word_Count[i]))
    print ('Complete!')
 
# Please add arguments to the function if would like to specify input.txt and word_dictionary under difference names and direcotry
Boggle()
# e.g.
# Boggle('~/Desktop/input2.txt','~/Desktop/word_dictionary2')
