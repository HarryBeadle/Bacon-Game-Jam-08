# Harry Beadle's Bacon Game Jam 08 Entry
# http://www.harrybeadle.co.uk

## Theme: THEME
## Game: GAME
## 17/10/14 to 18/10/14

from os import system as command
import pygame as p
p.init()

X = 800
Y = 600

def update_highscore(score):
    highscore_file = open('highscore.txt', 'r')
    highscore = int(highscore_file.read())
    if highscore < score:
        highscore_file.close()
        highscore_file = open('highscore.txt', 'w')
        highscore_file.write(str(score))
        highscore_file.close()
        return True
    else:
        return False

def load():
    # Setup Highscore Document
    try:
        open('highscore.txt')
    except:
        command("touch highscore.txt; echo '0' > highscore.txt")

def opening():
    # Opening Credits
    return

def menu():
    

def main():
    # Play the game here
    return

def end():
    # Finish cleanly
    return

load()
opening()
while True:
    menu()
    main()