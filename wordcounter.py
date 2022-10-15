import re
import os
answer=[]
WordCount={}
userchoice=input('(1)To process a text file\n(2)To process pasted text\nWhat is your choice\n')
if userchoice=="1":
    file= open('wordcountfile.txt')
    lines= file.readlines()
    for i in lines:
        print(i)
        answer=answer+(re.findall('\w+',i))
else:
    answer=answer+(re.findall('\w+',input('Paste your text here:\n')))
count=0
for a in answer:
    count+=1
    if a in WordCount:
        WordCount[a]+=1
    else:
        WordCount[a]=1
WordCount=(dict(sorted(WordCount.items(), key= lambda item: item[1])))
unique=0
for key in WordCount:
    unique+=1
os.system('clear')
print(f'There are {count} unique words in this text.')
print(f'There are {unique} unique words in this text.')


    