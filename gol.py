#!/usr/bin/env python
import os
import random
import time
import argparse
# this is how one may think of the 2d arrays used in this program
#         j-1 j   j+1
# i-1     0   0   0
# i       0   0   0
# i+1     0   0   0

def color(color_name, string):
    color_codes = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }

    if color_name not in color_codes or color_name is color_codes['reset']:
        return string

    return f"{color_codes[color_name]}{string}{color_codes['reset']}"


def iterateGameState(gol1, gol2, ruleSet):
    # copying over to arr 2 for every iteration for comparison purposes
    for i in range(len(gol1)):
        for j in range(len(gol1[0])):
            gol2[i][j] = gol1[i][j]
    # stats
    births = 0
    deaths = 0
    survivals = 0
    sterile = 0
    living = 0
    dead = 0
    population = len(gol1) * len(gol1[0])
    
    # boolean to prevent redrawing/recalculating a stagnant game
    same = True

    # calculating game logic
    for i in range(len(gol1)):
        for j in range(len(gol1[0])):
            neighbourCount = 0

            top = i == 0
            bottom = i == len(gol1)-1
            left = j == 0
            right = j == len(gol1[0])-1

            if (not top):
                neighbourCount += gol2[i-1][j]
            if (not left and not top):
                    neighbourCount += gol2[i-1][j-1]
            if (not right and not top):
                    neighbourCount += gol2[i-1][j+1]
            if (not bottom):
                neighbourCount += gol2[i+1][j]
            if (not left and not bottom):
                    neighbourCount += gol2[i+1][j-1]
            if (not right and not bottom):
                    neighbourCount += gol2[i+1][j+1]
            if (not left):
                neighbourCount += gol2[i][j-1]
            if (not right):
                neighbourCount += gol2[i][j+1]
            
            # apply rules
            gol1[i][j] = ruleCheck(gol2[i][j], ruleSet, neighbourCount)

            if (gol2[i][j] == 0 and gol1[i][j] == 1):
                births += 1
                living += 1
            elif (gol2[i][j]==1 and gol1[i][j] == 1):
                survivals += 1
                living += 1
            elif (gol2[i][j] == 0 and gol1[i][j] == 0):
                sterile += 1
                dead += 1
            else: # a cell dies
                deaths += 1
                dead += 1
            
            if (gol1[i][j] != gol2[i][j]): same = False

    # printing stats
    statline = "Ruleset: {} | G: {:>3} | Pop: {:>5} | L: {:>5} | %: {:.2f} | D: {:>5} | B: {:>5} | S: {:>5} |".format(ruleSet, generation, population, living, living/population*100, deaths, births, survivals)
    print(statline)
    return same

def ruleCheck(initial, ruleSet, n):
    if (ruleSet == "" or ruleSet == "default"):
        b = [3]
        s = [2, 3]
    elif (ruleSet=="replicator"):
        b = [1, 3, 5, 7]
        s = [1, 3, 5, 7]
    elif (ruleSet == "seeds"):
        b = [2]
        s = []
    elif (ruleSet == "blank" or ruleSet == "kuhaku"):
        b = [2, 5]
        s = [4]
    elif (ruleSet == "life-without-death" or ruleSet == "LWD" or ruleSet == "inkspots" or ruleSet == "flakes"):
        b = [3]
        s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    elif (ruleSet == "34" or ruleSet == "34-life" or ruleSet == "34L"):
        b = [3, 4]
        s = [3, 4]
    elif (ruleSet == "diameoba"):
        b = [3, 5, 6, 7, 8]
        s = [5, 6, 7, 8]
    elif (ruleSet == "block" or ruleSet == "2x2"):
        b = [3, 6]
        s = [1, 2, 5]
    elif (ruleSet == "morley" or ruleSet == "move"):
        b = [3, 6, 8]
        s = [2, 4, 5]
    elif (ruleSet == "anneal" or ruleSet == "twisted-majority-rule" or ruleSet == "TMR"):
        b = [4, 6, 7, 8]
        s = [3, 5, 6, 7, 8]
    elif (ruleSet == "majority" or ruleSet == "vote"):
        b = [5, 6, 7, 8]
        s = [4, 5, 6, 7, 8]
    
    return 1 if (n in b and initial == 0) or (n in s and initial == 1) else 0

def drawGame(golArr, deadCell, liveCell):
     for i in range(len(golArr)):
        for j in range(len(golArr[0])):
            if (golArr[i][j]): print(liveCell,end="")
            else: print(deadCell,end="")
        print()

def initGols():
    size = os.get_terminal_size()
    rowSize = (int)(size.columns) - 1
    colSize = (int)(size.lines) - 2
    gol1 = [[0]* rowSize for i in range(colSize)]
    gol2 = [[0]* rowSize for i in range(colSize)]

    for i in range(colSize):
        for j in range(rowSize):
            gol1[i][j] = random.randint(0,1)
    
    gols = [gol1, gol2]

    return gols

if __name__ == "__main__":
    agp = argparse.ArgumentParser(description="CLI game of life simulator written in python. Fills out the size of your terminal window")
    agp.add_argument(
        "-rs",
        "--rule-set",
        default="default",
        choices=["default", "replicator", "seeds", "blank", "kuhaku", "life-without-death", "LWD", "inkspots", "flakes", "34", "34-life", "34L", "ameoba", "diamond", "diameoba", "block", "2x2", "morley", "move", "anneal", "twisted-majority-rule", "TMR", "vote", "majority"],
        metavar="RULESET",
        type=str,
        help="Defining game of life ruleset. Default: 'default' (original b3s23 game)"
    )
    # agp.add_argument(
    #     "-l",
    #     "--loop",
    #     default="y",
    #     choices=["y","n"],
    #     type=str,
    #     help="whether or not the game loops infinitely"
    # )
    agp.add_argument(
        "-g",
        "--generations",
        default=500,
        choices=range(-1,1000),
        metavar="GENERATIONS",
        type=int,
        help="Maximum number of generations before ending a game of life. -1 for an infinite game. Default: 500"
    )
    agp.add_argument(
        "-d",
        "--delay",
        default=0.1125,
        type=float,
        help="Number of seconds between iterations. Default: 0.1125"
    )
    agp.add_argument(
        "-c",
        "--color",
        default="white",
        type=str,
        help="Change the color of the game text. Choices are black, red, green, yellow, blue, magenta, cyan, white"
    )
    args = agp.parse_args()
    
    ruleSet = args.rule_set
    colorchoice = str(args.color).lower()
    try:
        # make program perpetual
        while (True):
            # initialize arrays with appropriate size
            gols = initGols()
            gol1 = gols[0]
            gol2 = gols[1]

            # init gen
            generation = 0
            while (True):
                same = iterateGameState(gol1, gol2, ruleSet)

                # printing out game state
                drawGame(gol1, color(colorchoice, "."), color(colorchoice, "■"))

                # reinit game after 500 generations or once it turns stagnant
                # TODO stagnancy may also come in the form of a game of oscilators so let's try to detect that in the future by keeping a small history of arrays
                if (same or generation == args.generations): break

                # sleep to make it appear animated to the user
                # time.sleep(0.1125)
                time.sleep(args.delay)

                #increment generation
                generation+=1
    except KeyboardInterrupt:
        # Handle KeyboardInterrupt
        pass
