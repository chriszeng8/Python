FileName=raw_input('Enter text file name: ')
WordFile=open(FileName)
WordCount=dict()
wordText=WordFile.read()
words=wordText.split()
for word in words:
	WordCount[word]=WordCount.get(word,0)+1
# either create or update
WordFile.close()
print WordCount


bigCount=None
bigWord=None
for word,count in WordCount.items():
	if bigCount is None or count>bigCount:
		bigCount=count
		bigWord=word
print 'The most common word in this text file is \"',bigWord,'\" which appears',  bigCount, 'times.'