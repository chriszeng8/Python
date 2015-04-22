WordFile=open('mbox-short.txt')
WordCount=dict()

#wordText=WordFile.read()
for line in WordFile:
	words=line.split()
	for word in words:
		WordCount[word]=WordCount.get(word,0)+1
# either create or update
WordFile.close()
#print WordCount

lst=list()
for key,val in WordCount.items():
	lst.append((val,key))

lst.sort(reverse=True)

for val,key in lst[:10]:
	print key, val


#
print sorted([(v,k) for k,v in WordCount.items()])
# list comprehension: construct dynamically a value-key reversed list
# [(v,k) for k,v in c.items()]