'''
This python script is the "model" file that deals with the data (words.txt). It is imported by Game.py to implement features of the ScrabbleHelper.
'''

'''Class ScrabbleDictionary:
Variables: wordDict, wordList and wordGroup
Methods: 
1. __init__()
2. getWordList()
3. isWordInDict()
4. isWordInWordGroup()
5. __str__()
'''

class ScrabbleDictionary(object):
    def __init__(self, fileName):
        openFile = open(fileName, "r")
        
        #Create a wordDict dictionary which contains words grouped by their lengths. For eg. wordDict["3"] = ["awe","wea" .. ] (contains all the words of length 3)
        self._wordDict = {}
        self._wordDict["1"] = []
        self._wordDict["2"] = []
        self._wordDict["3"] = []
        self._wordDict["4"] = []        
        self._wordDict["5"] = []        
        self._wordDict["6"] = []        
        self._wordDict["7"] = []        
        self._wordDict["8"] = []        
        self._wordDict["9"] = []        
        self._wordDict["10"] = []        
        self._wordDict["11"] = []        
        self._wordDict["12"] = []        
        self._wordDict["13"] = []        
        self._wordDict["14"] = []        
        self._wordDict["15"] = []        
        self._wordDict["16"] = []        
        self._wordDict["17"] = []        
        self._wordDict["18"] = []        
        self._wordDict["19"] = []        
        self._wordDict["20"] = [] 
        
        #Create a wordGroup dictionary which groups words by their letter occurences. For eg. wordGroup["3"] = ["aew" .. ] ("awe", "wea" etc are considered equivalent)       
        self._wordGroup = {}
        self._wordGroup["1"] = set()
        self._wordGroup["2"] = set()
        self._wordGroup["3"] = set()
        self._wordGroup["4"] = set()        
        self._wordGroup["5"] = set()        
        self._wordGroup["6"] = set()        
        self._wordGroup["7"] = set()        
        self._wordGroup["8"] = set()        
        self._wordGroup["9"] = set()        
        self._wordGroup["10"] = set()        
        self._wordGroup["11"] = set()        
        self._wordGroup["12"] = set()        
        self._wordGroup["13"] = set()        
        self._wordGroup["14"] = set()        
        self._wordGroup["15"] = set()        
        self._wordGroup["16"] = set()        
        self._wordGroup["17"] = set()        
        self._wordGroup["18"] = set()        
        self._wordGroup["19"] = set()        
        self._wordGroup["20"] = set()
        self._wordList = []

        wordList = openFile.readlines()
        for word in wordList:
            self._wordList.append(word.strip("\n"))
        
        for word in self._wordList:
            if len(word) == 1:
                self._wordDict["1"].append(word)
                self._wordGroup["1"].add("".join(sorted(word)))        
            elif len(word) == 2:
                self._wordDict["2"].append(word)
                self._wordGroup["2"].add("".join(sorted(word)))
            elif len(word) == 3:
                self._wordDict["3"].append(word)        
                self._wordGroup["3"].add("".join(sorted(word)))
            elif len(word) == 4:
                self._wordDict["4"].append(word)        
                self._wordGroup["4"].add("".join(sorted(word)))
            elif len(word) == 5:
                self._wordDict["5"].append(word)        
                self._wordGroup["5"].add("".join(sorted(word)))
            elif len(word) == 6:
                self._wordDict["6"].append(word)        
                self._wordGroup["6"].add("".join(sorted(word)))
            elif len(word) == 7:
                self._wordDict["7"].append(word)        
                self._wordGroup["7"].add("".join(sorted(word)))
            elif len(word) == 8:
                self._wordDict["8"].append(word)        
                self._wordGroup["8"].add("".join(sorted(word)))
            elif len(word) == 9:
                self._wordDict["9"].append(word)        
                self._wordGroup["9"].add("".join(sorted(word)))
            elif len(word) == 10:
                self._wordDict["10"].append(word)        
                self._wordGroup["10"].add("".join(sorted(word)))
            elif len(word) == 11:
                self._wordDict["11"].append(word)        
                self._wordGroup["11"].add("".join(sorted(word)))
            elif len(word) == 12:
                self._wordDict["12"].append(word)        
                self._wordGroup["12"].add("".join(sorted(word)))
            elif len(word) == 13:
                self._wordDict["13"].append(word)        
                self._wordGroup["13"].add("".join(sorted(word)))
            elif len(word) == 14:
                self._wordDict["14"].append(word)        
                self._wordGroup["14"].add("".join(sorted(word)))
            elif len(word) == 15:
                self._wordDict["15"].append(word)        
                self._wordGroup["15"].add("".join(sorted(word)))
            elif len(word) == 16:
                self._wordDict["16"].append(word)        
                self._wordGroup["16"].add("".join(sorted(word)))
            elif len(word) == 17:
                self._wordDict["17"].append(word)        
                self._wordGroup["17"].add("".join(sorted(word)))
            elif len(word) == 18:
                self._wordDict["18"].append(word)        
                self._wordGroup["18"].add("".join(sorted(word)))
            elif len(word) == 19:
                self._wordDict["19"].append(word)        
                self._wordGroup["19"].add("".join(sorted(word)))
            elif len(word) == 20:
                self._wordDict["20"].append(word)        
                self._wordGroup["20"].add("".join(sorted(word)))
            
    #Getter function which returns the wordList    
    def getWordList(self):
        return self._wordList
    
    #Checks if a given word is in the dictionary
    def isWordInDict(self, word):
  
        if word in self._wordDict[str(len(word))]:
            return True
        else:
            return False
    
    #Checks if a given word is in a wordGroup 
    def isWordInWordGroup(self, word):
  
        if word in self._wordGroup[str(len(word))]:
            return True
        else:
            return False
    
    #str function to print the wordList        
    def __str__(self):
        return str(self._wordList)
