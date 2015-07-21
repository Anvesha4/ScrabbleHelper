'''
This is the middle script which implements the features using Dictionary.py and sends the results to Scrabble.py to display them on the GUI.
'''

import Dictionary
import itertools
import json

'''Class Game:
This class contains all the functions that implements features of the application
Variables: wordPoints, wordFreq
Static Variables: dictionaryObject and wordList
Methods:
1. __int__()
2. __str__()
3. getTwoLetterWords()
3. threeLetterWordsUsingInput()
4. xOrZWordsUsingInput()
5. getWordPoints()
6. qWords()
7. wordVerifier()
8. endTiles()
9. beginTiles()
10. getAnagrams()
11. acrossDown()
12. acrossDownFewerTiles()
'''
class Game(object):
    dictionaryObject = Dictionary.ScrabbleDictionary("words.txt")
    wordList = dictionaryObject.getWordList()

    def __init__(self):
        self._wordPoints = {"A": 1, "B": 3, "C": 3, "D":2, "E":1, "F": 4, "G": 2, "H": 4, "I": 1, "J":8, "K": 5,
                             "L": 1, "M":3, "N":1, "O": 1, "P":3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V":4,
                             "W": 4, "X": 8, "Y": 4, "Z": 10, "Blank": 0}
        self._wordFreq = {"A": 9, "B": 2, "C": 2, "D":4, "E":12, "F": 2, "G": 3, "H": 2, "I": 9, "J":1, "K": 1,
                             "L": 4, "M":2, "N":6, "O": 8, "P":2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V":2,
                             "W": 2, "X": 1, "Y": 2, "Z": 1, "Blank": 2}

    def __str__(self):
        msg = "\tx1\t\tx2\t\t\tx3\t\tx4\t\tx6\t\tx8\t\tx9\t\tx12\n" \
              "0\t \t\t(Blank)\t\t\t \t\t \t\t \t\t \t\t \t\t\n" \
              "1\t \t\t \t\t\t \t\tL,S,U \tN,R,T \tO \t\tA,I \tE\n" \
              "2\t \t\t \t\t\tG \t\tD \t\t \t\t \t\t \t\t\n" \
              "3\t \t\tB,C,M,P \t\t\t \t\t \t\t \t\t \t\t \t\t\n" \
              "4\t \t\tF,H,V,W,Y\t\t\t \t\t \t\t \t\t \t\t \t\t\n" \
              "5\tK \t\t\t\t \t\t \t\t \t\t \t\t \t\t\n" \
              "8\tJ,X \t\t\t\t \t\t \t\t \t\t \t\t \t\t\n" \
              "10\tQ,Z \t\t\t\t \t\t \t\t \t\t \t\t \t\t\n"

        return msg
        
    
    #Function that returns all two letter words from the dictionary 
    def getTwoLetterWords(self):
        words = {}
        for word in Game.wordList:
            if len(word) == 2:
                words[word] = self.getWordPoints(word)
        
        return words

    #Function that returns all three letter words from the dictionary using an input tile     
    def threeLetterWordsUsingInput(self, tile):
        #Error checking
        if tile.isalpha():
                pass
        else:
            return "Make sure your input contains letters only."
        
        if len(tile) == 1:
            pass
        else:
            return "Make sure your input contains only one letter."

        
        words = {}
        flag = 0
        for word in Game.wordList:
            if len(word) == 3 and tile in word:
                words[word]= self.getWordPoints(word)
                flag = 1
                    
        if flag == 0:
            return "There are no words that contain your input. "
        else:
            return words

    #Function that returns all words from the dictionary using an input tile and (X or Z)     
    def xOrZWordsUsingInput(self, tile):
        #Error checking
        if tile.isalpha():
            pass
        else:
            return "Make sure your input contains letters only."
        
        if len(tile) == 1:
            pass
        else:
            return "Make sure your input contains only one letter."
            
        words = {}
        flag = 0
        
        for word in Game.wordList:
            if ("x" in word or "X" in word) or ("z" in word or "Z" in word):
                if tile in word:
                    words[word] = self.getWordPoints(word)
                    flag = 1
                    
        if flag == 0:
            return "There are no words that contain your input. "
        else:
            return words
    
    #Function that returns points for a given word
    def getWordPoints(self, word):
        point = 0
        for letter in word:
            point += self._wordPoints[letter.upper()]
        return point

    #Function that returns all words the start with a Q but not followed by a U, from the dictionary 
    def qWords(self):
        words = {}
        for word in Game.wordList:
            if word[0].upper() == "Q" and word[1].upper() != "U":
               words[word] = self.getWordPoints(word)
        
        return words

    #Function that checks if a given word is in the dictionary
    def wordVerifier(self, inputWord):
        #Error checking
        if inputWord.isalpha():
            pass
        else:
            return "Make sure your input contains a valid word."   
             
        if Game.dictionaryObject.isWordInDict(inputWord) == True:
            return "The word is in the dictionary."
        else:
            return "The word is not in the dictionary."
    
    #Function that returns all the words that end with tiles entered by the user
    def endTiles(self, inputTiles):
        lettersList = inputTiles.split(",")
        flag = 0
        
        #Error checking
        for letter in lettersList:
            if letter.isalpha():
                pass
            else:
                return "Make sure your input contains letters separated by commas, with no comma in the beginning or end."
            
            if len(letter) == 1:
                pass
            else:
                return "Make sure one tile is one letter."
                
        words = {}
        for word in Game.wordList:
            for letter in lettersList:
                if word.endswith(letter):
                    words[word] = self.getWordPoints(word)
                    flag = 1

        if flag == 0:
            return "There are no words that contain your input. "
        else:
            return words

    #Function that returns all the words that begin with tiles entered by the user              
    def beginTiles(self, inputTiles):
        lettersList = inputTiles.split(",")
        flag = 0

        #Error checking
        for letter in lettersList:
            if letter.isalpha():
                pass
            else:
                return "Make sure your input contains letters separated by commas, with no comma in the beginning or end."
            
            if len(letter) == 1:
                pass
            else:
                return "Make sure one tile is one letter."
        
        words = {}
        for word in Game.wordList:
            for letter in lettersList:
                if word.startswith(letter):
                    words[word] = self.getWordPoints(word)
                    flag = 1

        if flag == 0:
            return "There are no words that contain your input. "
        else:
            return words
    
    #Function to get anagrams. It finds out the permutation of input tiles and then checks in the dictionary
    def getAnagrams(self, inputTiles):
        lettersList = inputTiles.split(",")
        
        #Error checking        
        for letter in lettersList:
            if letter.isalpha():
                pass
            else:
                return "Make sure your input contains letters separated by commas, with no comma in the beginning or end."
            
            if len(letter) == 1:
                pass
            else:
                return "Make sure one tile is one letter."
                
        inputString = inputTiles.replace(",","")
        listOfAnagrams = ["".join(p) for p in itertools.permutations(inputString)]
        newList = set()
        for anagram in listOfAnagrams:
            if Game.dictionaryObject.isWordInDict(anagram):
                newList.add(anagram)
        
        return list(newList)
    
    #Function to get input tiles one by one for across/down feature   
    def acrossDown(self, inputTiles, word):
        lettersList = inputTiles.split(",")

        #Error checking
        for letter in lettersList:
            if letter.isalpha():
                pass
            else:
                return "Make sure your input tiles are letters separated by commas, with no comma in the beginning or end."
            
            if len(letter) == 1:
                pass
            else:
                return "Make sure one tile is one letter."
                
        if word.isalpha():
            pass
        else:
            return "Make sure the word on board contains one word with all letters."
        
        if len(lettersList) < 8:
            pass
        else:
            return "Scrabble Helper can handle only seven or fewer tiles!"

        self.results = {}
        self.results["Down"] = {}        
        self.results["Across"] = {}
        
        for letter in list(word):
            self.results["Down"][letter] = {}
        
        #calls acrossdown for each combination of input tiles    
        for L in range(1, len(lettersList)+1):
            for comb in itertools.combinations(lettersList, L):
                self.acrossDownFewerTiles(",".join(list(comb)), word)
                
        return json.dumps(self.results, indent=4)        
    
    #Function to search for words that extend or cross    
    def acrossDownFewerTiles(self, inputTiles, word):    
        wordOnBoard = list(word)
        
        #Error Checking
        lettersList = inputTiles.split(",")
        for letter in lettersList:
            if letter.isalpha():
                pass
            else:
                return "Make sure your input contains all letters."
        
        inputString = inputTiles.replace(",","")
        
        #Down
        for letter in wordOnBoard:
            
            if Game.dictionaryObject.isWordInWordGroup("".join(sorted(inputString+letter))):
                for possibleWord in ["".join(p) for p in itertools.permutations(inputString+letter)]:
                    if Game.dictionaryObject.isWordInDict(possibleWord):
                        self.results["Down"][letter][possibleWord] = self.getWordPoints(possibleWord)
                    
        #Extends
        lettersList.append(word)
        
        if Game.dictionaryObject.isWordInWordGroup("".join(sorted("".join(sorted(lettersList))))):
            for possibleWord in ["".join(p) for p in itertools.permutations(lettersList)]:
                if Game.dictionaryObject.isWordInDict(possibleWord):
                    self.results["Across"][possibleWord] = self.getWordPoints(possibleWord)
                            

def main():
    gameObject = Game()
    menu(gameObject)

#To enable import by other scripts
if __name__ == "__main()__":
    main()
