'''
This is the main script (the "view" file) which implements the GUI for the users. It interacts with Game.py to get the results.
'''

from tkinter import *
import Game

'''Class ScrabbleWindow:
Variables: master, gameObject, photo, heading, photoLabel, menuGroup
Methods: 
1. __init__()
2. table()
3. twoLetters()
4. threeLetters()
5. QnotU()
6. ifInDict()
7. XandZ()
8. endsWith()
9. startsWith()
10. anagrams()
11. acrossDown()
'''
class ScrabbleWindow(object):
    
    '''Creating widgets in the window
    #1. The widget to be created using the base window
    #2. pack method which resizes the widget to fit itself to the given text and make itself visible'''
     
    def __init__(self, master):
        #master is the root which is used to create child widgets        
        self.master = master
        self.gameObject = Game.Game()
        self.photo = PhotoImage(file='scrabble.gif')
        
        #Create a frame object which has a heading, photolabel and one group of menu buttons
        frame = Frame(master, bg="olive drab")
        frame.pack()
        
        self.heading = Label(frame, text="Scrabble Helper", font=("MS Fixedsys", 40, "bold italic"), bg="LemonChiffon3")
        self.heading.pack()
        
        self.photoLabel = Label(frame,image=self.photo)
        self.photoLabel.pack()
        
        self.menuGroup = LabelFrame(frame, text="Menu", padx=5, pady=5, bg="LemonChiffon3")
        self.menuGroup.pack(padx=10, pady=10)
        
        #Create buttons in the menuGroup  
        one = Button(self.menuGroup, text="Display a table with point values and frequencies", height=1, width=75, bg="LemonChiffon2", command=self.table)
        two = Button(self.menuGroup, text="Display all two letter words", height=1, width=75, bg="LemonChiffon2", command=self.twoLetters)
        three = Button(self.menuGroup, text="Display all three letter words with your tile", height=1, width=75, bg="LemonChiffon2", command=self.threeLetters)
        four = Button(self.menuGroup, text="Display all words starting with a \"Q\" but not followed by \"U\"", height=1, width=75, bg="LemonChiffon2",  command=self.QnotU)
        five = Button(self.menuGroup, text="Enter a word to see if it's in the Scrabble dictionary", height=1, width=75, bg="LemonChiffon2",  command=self.ifInDict)
        six = Button(self.menuGroup, text="Enter your letter to see all words containing your letter and \"X\" or \"Z\"", height=1, width=75, bg="LemonChiffon2", command=self.XandZ)
        seven = Button(self.menuGroup, text="Enter as many letters as you would like to see if there are any words that end with those letters", height=1, width=75, bg="LemonChiffon2", command=self.endsWith)
        eight = Button(self.menuGroup, text="Enter as many letters as you would like to see if there are any words that begin with those letters", height=1, width=75, bg="LemonChiffon2", command=self.startsWith)
        nine = Button(self.menuGroup, text="Display all the anagrams for a set of tiles", height=1, width=75, bg="LemonChiffon2", command=self.anagrams)
        ten = Button(self.menuGroup, text="Display across and down words", height=1, width=75, bg="LemonChiffon2", command=self.acrossDown)
        quit = Button(self.menuGroup, text="Quit", fg="red", bg="LemonChiffon2", command=self.master.destroy)
        one.pack()
        two.pack()
        three.pack()
        four.pack()
        five.pack()
        six.pack()
        seven.pack()
        eight.pack()
        nine.pack()
        ten.pack()
        quit.pack()
        
    #Functions which create respective child windows on top of master
    def table(self):
        childWindow = table(self.master, self.gameObject)
        self.master.wait_window(childWindow.top)       
        
    def twoLetters(self):
        childWindow = twoLetters(self.master, self.gameObject)
        self.master.wait_window(childWindow.top)
        
    def threeLetters(self):
        childWindow = threeLetters(self.master, self.gameObject)
        self.master.wait_window(childWindow.top)
        
    def QnotU(self):
        childWindow = QnotU(self.master, self.gameObject)
        self.master.wait_window(childWindow.top)
                                
    def ifInDict(self):
        childWindow = ifInDict(self.master, self.gameObject)
        self.master.wait_window(childWindow.top)
                                
    def XandZ(self):
        childWindow = XandZ(self.master, self.gameObject)
        self.master.wait_window(childWindow.top)
                        
    def endsWith(self):
        childWindow = endsWith(self.master, self.gameObject)
        self.master.wait_window(childWindow.top)
                        
    def startsWith(self):
        childWindow = startsWith(self.master, self.gameObject)
        self.master.wait_window(childWindow.top)
    
    def anagrams(self):
        childWindow = anagrams(self.master, self.gameObject)
        self.master.wait_window(childWindow.top)
        
    def acrossDown(self):
        childWindow = acrossDown(self.master, self.gameObject)
        self.master.wait_window(childWindow.top)

'''Class table:
Variables: top, tableGroup
Mathods: ok() - to destroy the window
'''
                        
class table():
    def __init__(self, parent, gameObject):
        top = self.top = Toplevel(bg="LemonChiffon3")
        self.top.title("Letter distribution")
        
        #Create a frame to hold the table
        frame = Frame(self.top, bg="maroon")
        frame.pack()
        
        #Create a group inside the frame
        self.tableGroup = LabelFrame(frame, text="Table", padx=5, pady=5)
        self.tableGroup.pack(padx=10, pady=10)
        
        #Table to display Letter distribution and point values
        Message(self.tableGroup, text="").grid(row=0, column=0)
        Message(self.tableGroup, text="x1").grid(row=0, column=1)
        Message(self.tableGroup, text="x2").grid(row=0, column=2)
        Message(self.tableGroup, text="x3").grid(row=0, column=3)
        Message(self.tableGroup, text="x4").grid(row=0, column=4)
        Message(self.tableGroup, text="x6").grid(row=0, column=5)
        Message(self.tableGroup, text="x8").grid(row=0, column=6)
        Message(self.tableGroup, text="x9").grid(row=0, column=7)
        Message(self.tableGroup, text="x12").grid(row=0, column=8)
        Message(self.tableGroup, text="0").grid(row=1, column=0)
        Message(self.tableGroup, text="").grid(row=1, column=1)
        Message(self.tableGroup, text="Blank").grid(row=1, column=2)
        Message(self.tableGroup, text="").grid(row=1, column=3)
        Message(self.tableGroup, text="").grid(row=1, column=4)
        Message(self.tableGroup, text="").grid(row=1, column=5)
        Message(self.tableGroup, text="").grid(row=1, column=6)
        Message(self.tableGroup, text="").grid(row=1, column=7)
        Message(self.tableGroup, text="").grid(row=1, column=8)
        Message(self.tableGroup, text="1").grid(row=2, column=0)
        Message(self.tableGroup, text="").grid(row=2, column=1)
        Message(self.tableGroup, text="").grid(row=2, column=2)
        Message(self.tableGroup, text="").grid(row=2, column=3)
        Message(self.tableGroup, text="LSU").grid(row=2, column=4)
        Message(self.tableGroup, text="NRT").grid(row=2, column=5)
        Message(self.tableGroup, text="O").grid(row=2, column=6)
        Message(self.tableGroup, text="AI").grid(row=2, column=7)        
        Message(self.tableGroup, text="E").grid(row=2, column=8)
        Message(self.tableGroup, text="2").grid(row=3, column=0)
        Message(self.tableGroup, text="").grid(row=3, column=1)
        Message(self.tableGroup, text="").grid(row=3, column=2)
        Message(self.tableGroup, text="G").grid(row=3, column=3)
        Message(self.tableGroup, text="D").grid(row=3, column=4)
        Message(self.tableGroup, text="").grid(row=3, column=5)
        Message(self.tableGroup, text="").grid(row=3, column=6)
        Message(self.tableGroup, text="").grid(row=3, column=7)
        Message(self.tableGroup, text="").grid(row=3, column=8)
        Message(self.tableGroup, text="3").grid(row=4, column=0)
        Message(self.tableGroup, text="").grid(row=4, column=1)
        Message(self.tableGroup, text="BCMP").grid(row=4, column=2)
        Message(self.tableGroup, text="").grid(row=4, column=3)
        Message(self.tableGroup, text="").grid(row=4, column=4)
        Message(self.tableGroup, text="").grid(row=4, column=5)
        Message(self.tableGroup, text="").grid(row=4, column=6)
        Message(self.tableGroup, text="").grid(row=4, column=7)
        Message(self.tableGroup, text="").grid(row=4, column=8)
        Message(self.tableGroup, text="4").grid(row=5, column=0)
        Message(self.tableGroup, text="").grid(row=5, column=1)
        Message(self.tableGroup, text="FHVWY").grid(row=5, column=2)
        Message(self.tableGroup, text="").grid(row=5, column=3)
        Message(self.tableGroup, text="").grid(row=5, column=4)
        Message(self.tableGroup, text="").grid(row=5, column=5)
        Message(self.tableGroup, text="").grid(row=5, column=6)
        Message(self.tableGroup, text="").grid(row=5, column=7)
        Message(self.tableGroup, text="").grid(row=5, column=8)
        Message(self.tableGroup, text="5").grid(row=6, column=0)
        Message(self.tableGroup, text="K").grid(row=6, column=1)
        Message(self.tableGroup, text="").grid(row=6, column=2)
        Message(self.tableGroup, text="").grid(row=6, column=3)
        Message(self.tableGroup, text="").grid(row=6, column=4)
        Message(self.tableGroup, text="").grid(row=6, column=5)
        Message(self.tableGroup, text="").grid(row=6, column=6)
        Message(self.tableGroup, text="").grid(row=6, column=7)
        Message(self.tableGroup, text="").grid(row=6, column=8)
        Message(self.tableGroup, text="8").grid(row=7, column=0)
        Message(self.tableGroup, text="JX").grid(row=7, column=1)
        Message(self.tableGroup, text="").grid(row=7, column=2)
        Message(self.tableGroup, text="").grid(row=7, column=3)
        Message(self.tableGroup, text="").grid(row=7, column=4)
        Message(self.tableGroup, text="").grid(row=7, column=5)
        Message(self.tableGroup, text="").grid(row=7, column=6)
        Message(self.tableGroup, text="").grid(row=7, column=7)
        Message(self.tableGroup, text="").grid(row=7, column=8)
        Message(self.tableGroup, text="10").grid(row=8, column=0)
        Message(self.tableGroup, text="QZ").grid(row=8, column=1)
        Message(self.tableGroup, text="").grid(row=8, column=2)
        Message(self.tableGroup, text="").grid(row=8, column=3)
        Message(self.tableGroup, text="").grid(row=8, column=4)
        Message(self.tableGroup, text="").grid(row=8, column=5)
        Message(self.tableGroup, text="").grid(row=8, column=6)
        Message(self.tableGroup, text="").grid(row=8, column=7)
        Message(self.tableGroup, text="").grid(row=8, column=8)
        
        #Create a button to go back to the main menu
        b = Button(self.top, text="Main Menu", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        #Destroy the child window when Main Menu button is pressed
        self.top.destroy()

'''Class twoLetters:
Variables: top, parent, gameObject, label, text
Methods: ok() - to destroy the window
'''        
class twoLetters():
    def __init__(self, parent, gameObject):
        top = self.top = Toplevel(bg="LemonChiffon3")
        self.parent = parent
        self.gameObject = gameObject
        self.top.title("Two Letters")
        
        #Create a frame
        frame = Frame(self.top, bg="maroon")
        frame.pack()
        
        #Add a label to the frame
        self.label = Label(frame, text="All words from the dictionary that contain two letters: ", bg="LemonChiffon2")
        self.label.pack()
        
        #Text widget to display results
        self.text = Text(frame, wrap=WORD, width=90, height=10)
        self.text.insert("1.0", self.gameObject.getTwoLetterWords())
        self.text.pack()
        
        #Create a button to go back to the main menu
        b = Button(self.top, text="Main Menu", command=self.ok, bg="LemonChiffon2")
        b.pack(pady=5)

    def ok(self):
        #Destroy the child window when Main Menu button is pressed
        self.top.destroy()

'''Class threeLetters:
Variables: top, parent, gameObject, label, entry, text
Methods: 
1. getTile()
2. ok() - to destroy the window
'''
class threeLetters():
    def __init__(self, parent, gameObject):
        top = self.top = Toplevel(bg="LemonChiffon3")
        self.parent = parent
        self.gameObject = gameObject
        self.top.title("Three Letters including your tile")
        
        #Create a frame
        frame = Frame(self.top, bg="maroon")
        frame.pack()
        
        #Create another entry frame
        frameEntry = Frame(frame)
        frameEntry.pack()
        
        #Add a scrollbar to the frame
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        #Create a label and bind it to the entry frame
        self.label = Label(frameEntry, text="Please enter your tile to get all the three letter words using your tile:", bg="LemonChiffon2")
        self.label.pack(side = LEFT)
        
        #Create an entry and bind it to the entry frame
        self.entry = Entry(frameEntry, width=50)
        self.entry.pack()
        
        #Create a button to get words
        Button(frame, text="Get words", command=self.getTile, bg="LemonChiffon2").pack()
        
        #Create a button to go back to the main menu
        b = Button(self.top, text="Main Menu", command=self.ok, bg="LemonChiffon2")
        b.pack(pady=5)
        
        #Text widget to display results
        self.text = Text(frame, wrap=WORD, width=90, height=40, yscrollcommand=scrollbar.set)
        self.text.pack()
        scrollbar.config(command=self.text.yview)
  
    
    def getTile(self):
        #Clear text area
        self.text.delete("1.0",END)
        
        #Insert results by calling respective function from game.py using gameObject
        self.text.insert("1.0", self.gameObject.threeLetterWordsUsingInput(self.entry.get()))
        self.text.pack()

    def ok(self):
        #Destroy the child window when Main Menu button is pressed
        self.top.destroy()                    

'''Class QnotU:
Variables: top, parent, gameObject, label, text
Methods: ok() - to destroy the window
'''
class QnotU():
    def __init__(self, parent, gameObject):
        top = self.top = Toplevel(bg="LemonChiffon3")
        self.parent = parent
        self.gameObject = gameObject
        self.top.title("QnotU")
        
        #Create a frame
        frame = Frame(self.top, bg="maroon")
        frame.pack()
        self.label = Label(frame, text="All words from the dictionary that start with a Q but not followed by U: ", bg="LemonChiffon2")
        self.label.pack()
        
        #Text widget to display results
        self.text = Text(frame, wrap=WORD, width=90, height=5)
        self.text.insert("1.0", self.gameObject.qWords())
        self.text.pack()
        
        #Create a button to go back to the main menu
        b = Button(self.top, text="Main Menu", command=self.ok, bg="LemonChiffon2")
        b.pack(pady=5)

    def ok(self):
        #Destroy the child window when Main Menu button is pressed
        self.top.destroy() 

'''Class XandZ:
Variables: top, parent, gameObject, label, entry, text
Methods: 
1. getTile()
2. ok() - to destroy the window
'''
class XandZ():
    def __init__(self, parent, gameObject):
        top = self.top = Toplevel(bg="LemonChiffon3")
        self.parent = parent
        self.gameObject = gameObject
        self.top.title("(X or Z) and your tile")
        
        #Create a frame
        frame = Frame(self.top, bg="maroon")
        frame.pack()
        
        #Create another entry frame
        frameEntry = Frame(frame)
        frameEntry.pack()
        
        #Add a scrollbar to the frame
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        #Create a label and bind it to the entry frame
        self.label = Label(frameEntry, text="Enter your letter to see all words containing your letter and \"X\" or \"Z\":", bg="LemonChiffon2")
        self.label.pack(side = LEFT)
        
        #Create an entry and bind it to the entry frame
        self.entry = Entry(frameEntry, width=50)
        self.entry.pack()
        
        #Create a button to get words
        Button(frame, text="Get words", command=self.getTile, bg="LemonChiffon2").pack()
        
        #Create a button to go back to the main menu
        b = Button(self.top, text="Main Menu", command=self.ok, bg="LemonChiffon2")
        b.pack(pady=5)
        
        #Text widget to display results
        self.text = Text(frame, wrap=WORD, width=2000, height=50, yscrollcommand=scrollbar.set)
        self.text.pack()
        scrollbar.config(command=self.text.yview)
        
  
    def getTile(self):
        #Clear text area
        self.text.delete("1.0",END)
        
        #Insert results by calling respective function from game.py using gameObject
        self.text.insert("1.0", self.gameObject.xOrZWordsUsingInput(self.entry.get()))
        self.text.pack()

    def ok(self):
        #Destroy the child window when Main Menu button is pressed
        self.top.destroy()  

'''Class ifInDict:
Variables: top, parent, gameObject, label, entry, text
Methods: 
1. checkWord()
2. ok() - to destroy the window
'''         
class ifInDict():
    def __init__(self, parent, gameObject):
        top = self.top = Toplevel(bg="LemonChiffon3")
        self.parent = parent
        self.gameObject = gameObject
        self.top.title("Word Verifier")
        
        #Create a frame
        frame = Frame(self.top, bg="maroon")
        frame.pack()
        
        #Create another entry frame
        frameEntry = Frame(frame)
        frameEntry.pack()
        
        #Create a label and bind it to the entry frame
        self.label = Label(frameEntry, text="Enter a word to see if it's in the Scrabble Dictionary: ", bg="LemonChiffon2")
        self.label.pack(side = LEFT)
        
        #Create an entry and bind it to the entry frame
        self.entry = Entry(frameEntry, width=50)
        self.entry.pack()
        
        #Create a button to check the word
        Button(frame, text="Check Word", command=self.checkWord, bg="LemonChiffon2").pack()
        
        #Create a button to go back to the main menu
        b = Button(self.top, text="Main Menu", command=self.ok, bg="LemonChiffon2")
        b.pack(pady=5)
        
        #Text widget to display results
        self.text = Text(frame, wrap=WORD, width=90, height=3)
        self.text.pack()
        
    def checkWord(self):
        #Clear text area
        self.text.delete("1.0",END)
        
        #Insert results by calling respective function from game.py using gameObject
        self.text.insert("1.0", self.gameObject.wordVerifier(self.entry.get()))
        self.text.pack()

    def ok(self):
        #Destroy the child window when Main Menu button is pressed
        self.top.destroy()                    

'''Class endsWith:
Variables: top, parent, gameObject, label, entry, text
Methods: 
1. getWords()
2. ok() - to destroy the window
'''
class endsWith():
    def __init__(self, parent, gameObject):
        top = self.top = Toplevel(bg="LemonChiffon3")
        self.parent = parent
        self.gameObject = gameObject
        self.top.title("Ends with letters")
        
        #Create a frame
        frame = Frame(self.top, bg="maroon")
        frame.pack()
        
        #Create another entry frame
        frameEntry = Frame(frame)
        frameEntry.pack()
        
        #Add a scrollbar to the frame
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        #Create a label and bind it to the entry frame
        self.label = Label(frameEntry, text="Enter tiles to see words that end with those tiles, separated by a comma: ", bg="LemonChiffon2")
        self.label.pack(side = LEFT)
        
        #Create an entry and bind it to the entry frame
        self.entry = Entry(frameEntry, width=50)
        self.entry.pack()
        
        #Create a button to get words
        Button(frame, text="Get words", command=self.getWords, bg="LemonChiffon2").pack()
        
        #Create a button to go back to the main menu
        b = Button(self.top, text="Main Menu", command=self.ok, bg="LemonChiffon2")
        b.pack(pady=5)
        
        #Text widget to display results
        self.text = Text(frame, wrap=WORD, width=2000, height=50, yscrollcommand=scrollbar.set)
        self.text.pack()
        scrollbar.config(command=self.text.yview)
        
    def getWords(self):
        #Clear text area
        self.text.delete("1.0",END)
        
        #Insert results by calling respective function from game.py using gameObject
        self.text.insert("1.0", self.gameObject.endTiles(self.entry.get()))
        self.text.pack()

    def ok(self):
        #Destroy the child window when Main Menu button is pressed
        self.top.destroy()  
 
'''Class startsWith:
Variables: top, parent, gameObject, label, entry, text
Methods: 
1. getWords()
2. ok() - to destroy the window
'''        
class startsWith():
    def __init__(self, parent, gameObject):
        top = self.top = Toplevel(bg="LemonChiffon3")
        self.parent = parent
        self.gameObject = gameObject
        self.top.title("Starts with letters")
        
        #Create a frame
        frame = Frame(self.top, bg="maroon")
        frame.pack()
        
        #Create another entry frame
        frameEntry = Frame(frame)
        frameEntry.pack()
        
        #Add a scrollbar to the frame
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        #Create a label and bind it to the entry frame
        self.label = Label(frameEntry, text="Enter tiles to see words that begin with those tiles, separated by a comma: ", bg="LemonChiffon2")
        self.label.pack(side = LEFT)
        
        #Create an entry and bind it to the entry frame
        self.entry = Entry(frameEntry, width=50)
        self.entry.pack()
        
        #Create a button to get words
        Button(frame, text="Get words", command=self.getWords, bg="LemonChiffon2").pack()
        
        #Create a button to go back to the main menu
        b = Button(self.top, text="Main Menu", command=self.ok, bg="LemonChiffon2")
        b.pack(pady=5)
        
        #Text widget to display results
        self.text = Text(frame, wrap=WORD, width=2000, height=50, yscrollcommand=scrollbar.set)
        self.text.pack()
        scrollbar.config(command=self.text.yview)
        
    def getWords(self):
        #Clear text area
        self.text.delete("1.0",END)
        
        #Insert results by calling respective function from game.py using gameObject
        self.text.insert("1.0", self.gameObject.beginTiles(self.entry.get()))
        self.text.pack()

    def ok(self):
        #Destroy the child window when Main Menu button is pressed
        self.top.destroy()         

'''Class anagrams:
Variables: top, parent, gameObject, label, entry, text
Methods: 
1. getWords()
2. ok() - to destroy the window
'''
class anagrams():
    def __init__(self, parent, gameObject):
        top = self.top = Toplevel(bg="LemonChiffon3")
        self.parent = parent
        self.gameObject = gameObject
        self.top.title("Anagrams")

        #Create a frame
        frame = Frame(self.top, bg="maroon")
        frame.pack()
        
        #Create another entry frame
        frameEntry = Frame(frame)
        frameEntry.pack()
        
        #Add a scrollbar to the frame
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        #Create a label and bind it to the entry frame
        self.label = Label(frameEntry, text="Enter letters whose anagrams you want to find, separated by commas: ", bg="LemonChiffon2")
        self.label.pack(side = LEFT)
        
        #Create an entry and bind it to the entry frame
        self.entry = Entry(frameEntry, width=50)
        self.entry.pack()
        
        #Create a button to get words
        Button(frame, text="Get words", command=self.getWords, bg="LemonChiffon2").pack()
        
        #Create a button to go back to the main menu
        b = Button(self.top, text="Main Menu", command=self.ok, bg="LemonChiffon2")
        b.pack(pady=5)
        
        #Text widget to display results
        self.text = Text(frame, wrap=WORD, width=90, height=40, yscrollcommand=scrollbar.set)
        self.text.pack()
        scrollbar.config(command=self.text.yview)
        
    def getWords(self):
        #Clear text area
        self.text.delete("1.0",END)
        
        #Insert results by calling respective function from game.py using gameObject
        self.text.insert("1.0", self.gameObject.getAnagrams(self.entry.get()))
        self.text.pack()

    def ok(self):
        #Destroy the child window when Main Menu button is pressed
        self.top.destroy()  

'''Class acrossDown:
Variables: top, parent, gameObject, label1, entry1, label2, entry2, text
Methods: 
1. getWords()
2. ok() - to destroy the window
'''
class acrossDown():
    def __init__(self, parent, gameObject):
        top = self.top = Toplevel(bg="LemonChiffon3")
        self.parent = parent
        self.gameObject = gameObject
        self.top.title("Across/Down")
        
        #Create a frame
        frame = Frame(self.top, bg="maroon")
        frame.pack()
        
        #Create entry frames
        frameEntry1 = Frame(frame)
        frameEntry1.pack()
        frameEntry2 = Frame(frame)
        frameEntry2.pack()
        
        #Add a scrollbar to the frame
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        #Create a label and bind it to the entry frame1
        self.label = Label(frameEntry1, text="Enter the tiles separated by commas: ", bg="LemonChiffon2")
        self.label.pack(side = LEFT)
        
        #Create an entry and bind it to the entry frame1
        self.entry = Entry(frameEntry1, width=50)
        self.entry.pack()
        
        #Create a label and bind it to the entry frame2
        self.label2 = Label(frameEntry2, text="Enter the word on board: ", bg="LemonChiffon2")
        self.label2.pack(side = LEFT)
        
        #Create an entry and bind it to the entry frame2
        self.wordEntry = Entry(frameEntry2, width=50)
        self.wordEntry.pack()
        
        #Create a button to get words
        Button(frame, text="Get words", command=self.getWords, bg="LemonChiffon2").pack()
        
        #Create a button to go back to the main menu
        b = Button(self.top, text="Main Menu", command=self.ok, bg="LemonChiffon2")
        b.pack(pady=5)
        
        #Text widget to display results
        self.text = Text(frame, wrap=WORD, width=50, height=50, yscrollcommand=scrollbar.set)
        self.text.pack()
        scrollbar.config(command=self.text.yview)
        
    def getWords(self):
        #Clear text area
        self.text.delete("1.0",END)
        
        #Insert results by calling respective function from game.py using gameObject
        self.text.insert("1.0", self.gameObject.acrossDown(self.entry.get(), self.wordEntry.get()))
        self.text.pack()

    def ok(self):
        #Destroy the child window when Main Menu button is pressed
        self.top.destroy()   
                                
def main():
    #Initialize Tkinter using a Tk root widget. Only one root is created for each program, and before all widgets
    root = Tk()
    root.title("Welcome")
    window = ScrabbleWindow(root)
    
    #Loop which runs until main window is closed
    root.mainloop()
    
main()
