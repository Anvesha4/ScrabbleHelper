# ScrabbleHelper
![MainMenu] (https://github.com/Anvesha4/ScrabbleHelper/blob/master/MainMenu.png)

##About:
This is a word-game helper application which has the following features (not in the same order):

1. List all the anagrams for a set of tiles entered by the user.
2. List all words that start with a “Q” but are not followed by a “u”.
3. Display all 2-letter words.
4. List the 3-letter words containing a given input tile (letter).
5. Word verifier: Given an input word, verify that it exists within the Scrabble dictionary (words.txt).
6. Find all words that end with one or more tiles (letters) entered by the user.
7. Find all words that begin with one or more input tiles (letters.
8. Find all words containing the letters “X” or “Z” and an input tile.
9. Display point values alongside all result words.
10. Display a simple table showing Scrabble point values and frequencies for all 26 letters of the English alphabet plus blanks.
11. Find all ways to play a given set of seven or fewer input tiles (the player’s rack) that extend or cross an existing word on the board (disregarding the positioning of the word on the board). List the results by category (extends the word, crosses the first letter of the word, crosses the second letter, and so on). Sort each play by its total point value within each category, and display the point value next to each play.

![Across/Down Option] (https://github.com/Anvesha4/ScrabbleHelper/blob/master/Across_Down.png)

##Contents:
The project contains the following:

1. Dictionary.py: This python script is the "model" file that deals with the data (words.txt).
2. Scrabble.py: This is the main script (the "view" file) which implements the GUI for the users.
3. Game.py: This is the middle script which implements the features using Dictionary.py and sends the results to Scrabble.py to display them on the GUI. 
4. words.txt: This is the dictionary of words used as reference in the application. It should be in the same directory as the scripts.
5. scrabble.gif: This should be present in the same directory as the scripts.

To run this project, you will need python3. Python libraries required are tkinter, itertools and json.

Usage:
````
        python3 Scrabble.py 
````
