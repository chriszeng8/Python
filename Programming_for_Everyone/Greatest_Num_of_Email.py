name = "mbox-short.txt"
handle = open(name)
EmailFreq=dict()
for line in handle:
    if line.startswith('From '):
        LineList=line.split()
        Email=LineList[1]
        EmailFreq[Email]=EmailFreq.get(Email,0)+1


GreatestEmail=None
GreatestFreq=None
for email in EmailFreq:
	if (not GreatestEmail) or EmailFreq[email]>GreatestFreq:
		GreatestEmail=email
		GreatestFreq=EmailFreq[email]
print GreatestEmail,GreatestFreq