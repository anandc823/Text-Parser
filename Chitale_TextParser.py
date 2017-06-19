#Anand Chitale
import string
import datetime
def hasNum(string):
    numbers = ('1','2','3','4','5','6','7','8','9','0')
    for i in string:
        if i in numbers:
            return True
    return False
fName = input('Enter the filename to process ')
valid = dict()
with open('wordlist.txt', 'r', encoding = 'utf-8') as wlist:
    for line in wlist:
        line = line.strip()
        valid[line] = 1
startTime = datetime.datetime.now()

with open(fName, 'r', encoding='utf-8') as myFile:
    z = 0
    i = 0
    start = True
    fake = dict()
    used = dict()
    frequentPrint = ""
    start = False
    stop = False
    for line in myFile:
        if(line[0:41] == "*** START OF THIS PROJECT GUTENBERG EBOOK"):
            start = True
            continue
        if(line[0:39] == "*** END OF THIS PROJECT GUTENBERG EBOOK"):
            stop = True
        if(start == True and stop == False):
            line = line.replace("-", " ")
            for word in line.split():
                if hasNum(word) == True:
                    continue
                word = word.strip(string.punctuation)
                word = word.lower()
                for element in word:
                    if (element in string.punctuation and element != "'"):
                        word = word.replace(element, "")
                    if(element == "'" and word[word.index("'")+ 1] == "s"):
                        word = word[0:word.index("'")]
                if word == "":
                    continue
                if word not in used:
                    used[word] = 1
                    z = z + 1
                else:
                    used[word] = used[word] + 1
                i= i + 1
    numwordsprint = str(i) + " words in the file." + '\n' + str(z) + " unique words in the file."
    print(numwordsprint)     
    sortedByWordList = sorted(used)
    betterSortedByValueList = sorted(sortedByWordList,key=used.get,reverse=True)
    commonCount=0
    for element in betterSortedByValueList:
        if(commonCount < 20):
            frequentPrint += "Most Frequent Word " + "#" + str(commonCount+1)+ ": " + element + " - " + str(used[element]) + "\n"
            commonCount = commonCount + 1
    print(frequentPrint)
    for key in used:
        if((key not in valid) and (hasNum(key) == False)):
            fake[key] = 1
    showFake = input("Do you wish to see a list of words not in the dictionary(Yes/No)?")
    if (showFake[0] == "Y" or showFake[0] == "y"):
        toPrint = ""
        fake = sorted(fake)
        for nonword in fake:
            toPrint += nonword + "\n"
        print(toPrint)
endtime = datetime.datetime.now()
print("runtime: " + str(endtime - startTime))
