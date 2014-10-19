#!/usr/bin/env python

## Bacon Game Jam 08
## Harry Beadle
## Solo Entry

#### Theme: "Millions of them."
#### Interpritation: "Google Searches"

# Requires Random and Urllib2
from random import shuffle
from urllib2 import urlopen

# Requires Pygame
import pygame as p
p.init()

X = 1280
Y = 720
Origin = (0, 0)
scr = p.display.set_mode((X, Y))

BLACK = 000,000,000
WHITE = 255,255,255
GREY  = 215,215,215
DGRAY = 241,241,241
CKEY  = 000,255,000
RED   = 187,66,40
GREEN = 83,151,88
BLUE  = 90,131,253

ARIAL = p.font.Font("Arial.ttf", 50)
TITLE = p.font.Font("Arial.ttf", 130)

surfaceForeground = p.Surface((X, Y))
surfaceForeground.set_colorkey(CKEY)
surfaceForeground.fill(surfaceForeground.get_colorkey())
p.draw.line(surfaceForeground, BLACK, (0, Y/2), (X, Y/2), 10)
p.draw.rect(surfaceForeground, WHITE, (555,325,180,70))
p.draw.rect(surfaceForeground, BLACK, (555,325,180,70), 5)
surfaceForeground.blit(ARIAL.render("OR", 1, BLACK), (((X-75)/2),((Y-57)/2)))
p.draw.rect(surfaceForeground, WHITE, (140,490,1000,100))
p.draw.rect(surfaceForeground, WHITE, (140,130,1000,100))

surfacePrimary = p.Surface((X, Y))
surfacePrimary.set_colorkey(CKEY)
surfacePrimary.fill(surfacePrimary.get_colorkey())
p.draw.rect(surfaceForeground, GREY, (140,490,1000,100), 3)
p.draw.rect(surfaceForeground, BLUE, (140,130,1000,100), 3)

surfaceSecondary = p.Surface((X, Y))
surfaceSecondary.set_colorkey(CKEY)
surfaceSecondary.fill(surfaceSecondary.get_colorkey())
p.draw.rect(surfaceSecondary, BLUE, (140,490,1000,100), 3)
p.draw.rect(surfaceSecondary, GREY, (140,130,1000,100), 3)

imgGoogle = p.image.load("google.bmp").convert()
imgGoogle.set_colorkey(WHITE)

imgBacon = p.image.load("bacon.png")
imgBacon.set_colorkey(WHITE)

## Top Searches of 2013 by Catagory
Searches_By_Catagory = {
    "All"            : ["Paul Walker", "iPhone 5S", "Royal Baby", "Cory Monteith", "Oscar Pistorious", "Nelson Mandela", "Grand National 2013", "Universal Jobmatch", "Margret Thatcher", "Xbox One"],
    "People"         : ["Paul Walker", "Cory Monteith", "Oscar Pistorious", "Nelson Mandela", "Margret Thathcher", "Peter Capaldi", "Nigella Lawson", "Tom Daley", "Lou Reed", "Joey Essex"],
    "Events"         : ["Grand National", "Wimbolden", "Eurovision", "Confederations Cup", "The Oscars", "Red Nose Day", "Glastonbury", "Lovebox", "Brit Awards", "The Ashes"],
    "Football Stars" : ["Gareth Bale", "Willian Borges da Silva", "Mesut Ozil", "David Moyes", "Christian Bentiez", "Thiago Alcantara", "Paul Gascoigne", "Gonzalo, Higuain", "Adnan Januzaj", "Razor Ruddock"],
    "How To"         : ["How to make pancakes", "How to wrtite a CV", "How to loose weight", "How to draw manga", "How to play poker", "How to play guitar", "How to get a flat stomach", "How to dip dye hair", "How to reset iPod", "How to find IP address"],
    "Movies"         : ["Man of Steel", "World War Z", "Iron Man 3", "The Conjuring", "Dispicable Me 2", "The Impossible", "The Life of Pi", "Insidious", "Elysium", "Skyfall"],
    "Songs"          : ["Harlem Shake", "Gangnam Style", "Blured Lines", "Thrift Shop", "Wreckig Ball", "Roar", "Impossible", "Holy Grail", "Get Lucky", "Mirrors"],
    "Places"         : ["Rome", "New York", "Amsterdam", "Palma", "Magaluf", "Bangkok", "Sydney", "Bruges", "Venice", "Mauritius"],
    "TV"             : ["Eastenders", "Breaking Bad", "Coronation Street", "Big Brother 2013", "Strictly Come Dancing", "Emmerdale", "Holyoaks", "Daybreak", "Top Gear", "The Voice"],
    "What Is"        : ["What is twerking?", "What is my IP?", "What is yolo?", "What is a prime number?", "What is illuminati?", "What is my car worth?", "What is spooning?", "What is global warming?", "What is Zumba?", "What is the meaning of life?"]
}
Catagory = [
    "All",
    "People",
    "Events",
    "Football Stars",
    "How To",
    "Movies",
    "Songs",
    "Places",
    "TV",
    "What Is"
]

def getLiveList():
    List = []
    Atom = urlopen("http://www.google.com/trends/hottrends/atom/feed")
    for Line in Atom.read().split("\n"):
        if ("<title>" in Line) and ("</title>" in Line) and not ("Hot Trends" in Line):
            List.append(Line[15:-8])
    if len(List) % 2 != 0:
        del List[-1]
    return List

def Input():
    Output = []
    for Event in p.event.get(p.KEYDOWN):
        if Event.key == p.K_UP: Output.append("Up")
        if Event.key == p.K_DOWN: Output.append("Down")
        if Event.key == p.K_LEFT: Output.append("Left")
        if Event.key == p.K_RIGHT: Output.append("Right")
        if Event.key == p.K_RETURN: Output.append("Enter")
        if Event.key == p.K_ESCAPE: p.quit();quit()
    if p.event.get(p.MOUSEBUTTONUP): Output.append("Mouse")
    if p.event.get(p.QUIT): p.quit();quit()
    return Output

def splash():
    # Splash Screen
    scr.fill((190,70,46))
    scr.blit(
        imgBacon,
        (
            (X-imgBacon.get_size()[0])/2,
            (Y-imgBacon.get_size()[1])/2
        )
    )
    p.display.flip()
    p.time.wait(1000)

def mainMenu():
    scr.fill(DGRAY)
    p.draw.rect(scr, WHITE, (106,360,480,180))
    p.draw.rect(scr, WHITE, (694,360,480,180))
    p.draw.rect(scr, BLUE, (106,360,480,180), 3)
    p.draw.rect(scr, GREY, (694,360,480,180), 3)
    scr.blit(
        ARIAL.render("Trending Now", 1, BLACK),
        (180, 420)
    )
    scr.blit(
        ARIAL.render("Top of 2013", 1, BLACK),
        (810, 420)
    )
    scr.blit(
        TITLE.render("Trends", 1, BLACK),
        (720, 105)
    )
    scr.blit(imgGoogle, (150, 90))
    Selection = 0
    p.display.flip()
    while True:
        INPUT = Input()
        if "Enter" in INPUT or "Mouse" in INPUT:
            return Selection
        if ("Right" in INPUT or p.mouse.get_pos()[0]>(X/2)) and Selection == 0:
            Selection = 1
            p.draw.rect(scr, GREY, (106,360,480,180), 3)
            p.draw.rect(scr, BLUE, (694,360,480,180), 3)
        if ("Left" in INPUT or p.mouse.get_pos()[0]<(X/2)) and Selection == 1:
            Selection = 0
            p.draw.rect(scr, BLUE, (106,360,480,180), 3)
            p.draw.rect(scr, GREY, (694,360,480,180), 3)
        p.display.flip()

def catagorySelection():
    scr.fill(DGRAY)
    p.draw.rect(scr, WHITE, (140,310,1000,100))
    p.draw.rect(scr, BLUE, (140,310,1000,100), 3)
    scr.blit(
        ARIAL.render("Choose your catagory... (use arrow keys)", 1, BLACK),
        (
            (140,250)
        )
    )
    Element = 0
    preElement = -1
    while True:
        INPUT = Input()
        if "Right" in INPUT and Element != (len(Catagory)-1):
            Element += 1
        if "Left" in INPUT and Element != 0:
            Element -= 1
        if "Enter" in INPUT:
            return Searches_By_Catagory[Catagory[Element]]
        if Element != preElement:
            p.draw.rect(scr, WHITE, (140,310,1000,100))
            p.draw.rect(scr, BLUE, (140,310,1000,100), 3)
            String = Catagory[Element] + " " + "(%i/%i)" % (Element + 1, len(Catagory))
            scr.blit(
                ARIAL.render(String, 1, BLACK),
                (
                    (X-ARIAL.size(String)[0])/2,
                    (Y-ARIAL.size(String)[1])/2
                )
            )
            preElement = Element
        p.display.flip()

def play(String1, String2):
    scr.fill(DGRAY)
    scr.blit(surfacePrimary, Origin)
    surfaceForegroundTemp = p.Surface((X, Y))
    surfaceForegroundTemp.set_colorkey(CKEY)
    surfaceForegroundTemp.fill(surfaceForegroundTemp.get_colorkey())
    surfaceForegroundTemp.blit(surfaceForeground, Origin)
    surfaceForegroundTemp.blit(
        ARIAL.render(String1, 1, BLACK),
        (
            (X-ARIAL.size(String1)[0])/2,
            152
        )
    )
    surfaceForegroundTemp.blit(
        ARIAL.render(String2, 1, BLACK),
        (
            (X-ARIAL.size(String2)[0])/2,
            512
        )
    )
    State = 0
    scr.blit(surfaceForegroundTemp, Origin)
    p.display.flip()
    while True:
        INPUT = Input()
        if "Enter" in INPUT or "Mouse" in INPUT:
            return State
        if ("Up" in INPUT or p.mouse.get_pos()[1] < (Y/2)) and State == 1:
            scr.blit(surfaceForegroundTemp, Origin)
            scr.blit(surfacePrimary, Origin)
            State = 0
        if ("Down" in INPUT or p.mouse.get_pos()[1] > (Y/2)) and State == 0:
            scr.blit(surfaceForegroundTemp, Origin)
            scr.blit(surfaceSecondary, Origin)
            State = 1
        p.display.flip()

def finishPage(Score, List):
    scr.fill(DGRAY)
    Percentage = (float(Score)*100)/(float(len(List))/float(2))
    Percentage = str(int(Percentage)) + "% - Press enter to continue to Main Menu."
    scr.blit(
        ARIAL.render(Percentage, 1, BLACK),
        (
            (X-ARIAL.size(Percentage)[0])/2,
            (Y-ARIAL.size(Percentage)[1])/2
        )
    )
    while True:
        INPUT = Input()
        if "Enter" in INPUT or "Mouse" in INPUT:
            return
        p.display.flip()

def main():
    Selection = mainMenu()
    if Selection == 0:
        scr.fill(DGRAY)
        scr.blit(
            ARIAL.render("Loading...", 1, BLACK),
            (
                (X-ARIAL.size("Loading...")[0])/2,
                (Y-ARIAL.size("Loading...")[1])/2
            )
        )
        p.display.flip()
        List = getLiveList()
    if Selection == 1:
        List = catagorySelection()
    originalPosition = {}
    count = 0
    for e in List:
        originalPosition.update({e : count})
        count += 1
    shuffle(List)
    Score = 0
    for x in range(0,len(List),2):
        Win = 1
        if originalPosition[List[x]] > originalPosition[List[x+1]]: Win = 0
        if play(List[x], List[x+1]) != Win:
            Score += 1
    finishPage(Score, List)
    
if __name__ == '__main__':
    splash()
    while True: main()