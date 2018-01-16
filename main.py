'''
Created on Dec 5, 2015

@author: Matthias
'''

import json

def PrintResults(player,opponent,matches):
    for match in matches:
        if match["DCI"] == player and match["OpponentDCI"] == opponent and match["Result"] != "Intentional Draw":
            print match["Result"] + " at " + match["TournamentName"] + " (" + match["Format"] + ") " + match["Date"]
    return True


def GetResults(player,opponent,matches):
    playerWins,opponentWins,draws = 0,0,0
    #locationList = []
    for match in matches:
        if match["DCI"] == player and match["OpponentDCI"] == opponent and match["Result"] != "Intentional Draw":
            if match["Result"] == "Win":
                playerWins += 1
                #print "WON at " + match["TournamentName"] + " (" + match["Format"] + ")"
            elif match["Result"] == "Loss":
                opponentWins += 1
                #print "LOST at " + match["TournamentName"] + " (" + match["Format"] + ")"
            else:
                draws +=1
    return playerWins,opponentWins,draws

def OverallRecord(player,matches):
    wins,losses,draws = 0,0,0
    for match in matches:
        if match["DCI"]==player:
            if match["OpponentDCI"] in dciNumbers and match["Result"] != "Intentional Draw":
                if match["Result"] == "Win":
                    wins += 1
                elif match["Result"] == "Loss":
                    losses += 1
                else:
                    draws += 1
    return wins,losses,draws
                

#Set of Players in the Player's Championship
dciNumbers = {"3043101865":"Caleb Scherer","5049942652":"Brad Nelson","2210126823":"Todd Stevens","7223920643":"Max McVety","2019780255":"Todd Anderson","1022501662":"Tom Ross","3208256023":"Jeff Hoogland","1051786619":"Gerry Thompson","7083142562":"Jim Davis","1201269006":"Andrew Tenjum","7012682632":"Kevin Jones","1102090686":"Liam Lonergan","8019027343":"Andrew Jessup","1206870763":"Jacob Baugh","1202011091":"Brad Carpenter","6073195379":"Joe Lossett"}

with open("Matches.json") as json_file:
    rawmatches = json.load(json_file)
    matches = []
    for match in rawmatches:
        if match["TournamentType"][:8]=="StarCity": #and match["Date"][:4]=="2015":
            matches.append(match)
    for player in dciNumbers:
        wins,losses,draws = OverallRecord(player, matches)
        print "\n"+dciNumbers[player],": "+str(wins)+"-"+str(losses)+"-"+str(draws)+"\n--------------------\n"
        for opponent in dciNumbers:
            if player != opponent:
                wins,losses,draws = GetResults(player,opponent,matches)
                if wins == 0 and losses == 0 and draws == 0:
                    print "Has never played " + dciNumbers[opponent]
                elif draws == 0:
                    print str(wins) + "-" + str(losses) + " against "+ dciNumbers[opponent]
                else:
                    print str(wins) + "-" + str(losses) + "-" +str(draws) + " against "+ dciNumbers[opponent]
                PrintResults(player,opponent,matches)
    for player in dciNumbers:
        print dciNumbers[player]
        wins,losses,draws= 0,0,0
        for match in matches:
                ##match["TournamentType"][:8]=="StarCity" and
                if match["DCI"] == player and match["Date"][:4]=="2016":
                    if match["Result"]=="Win":
                        wins += 1
                    elif match["Result"]=="Loss":
                        losses += 1
                    elif match["Result"]=="Draw":
                        draws += 1
        print str(wins)+"-"+str(losses)+"-"+str(draws)
        print float(2*wins+draws)/(2*(wins+losses+draws))

    