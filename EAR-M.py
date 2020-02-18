# ETossed's Algorithmic Ranking of Melee
# This is a MAJOR work in progress, and I'm getting a foundation down for
# a more advanced ranking at some point

# Tournament is to be implemented in more complicated ELO system later
# Non-Local tournamnets are the only one that counts. Superlocals (i.e. Nimbus 70) do count.

import math

class Tournament(object):
    def __init__(self, name, size, winner):
        self.name = name;
        self.size = size;
        self.winner = winner;

    def __repr__(self):
        return "Tournament: " + self.name + " | Winner: " + self.winner

class Player(object):
    def __init__(self, tag, rank):
        self.tag = tag
        self.rank = rank
        self.sets_played = 0
        self.tournaments = []
        self.wins = []
        self.losses = []
        self.melee_lvl = 0

    def __lt__(self, other):
        return self.melee_lvl < other.melee_lvl

    def __repr__(self):
        return self.tag + " EAR-M: " + str(self.melee_lvl)

    def lvl_calculator(self, tournament, placement, opponents, history):
        # Tournament is the tournament that was attended
        # Placement is the player's placement at that tournament
        # Opponents is a player array
        # History is the list correlated with opponents with w or l
        if len(opponents) != len(history):
            print("ERROR: Amount of matches does not match amount of opponents for " + self.tag + " - " + tournament.name)
            return
        
        self.tournaments.append(tournament)

        # Result loop
        for i in range(len(opponents)):
            self.sets_played += 1

            # For Wins
            if history[i] == "w":
                if opponents[i] in self.wins:
                    self.melee_lvl += (5 * (((101 - opponents[i].rank) * (math.log((101-opponents[i].rank)))) / 100))
                else:
                    self.wins.append(opponents[i])
                    self.melee_lvl += (10 * (((101 - opponents[i].rank) * (math.log((101-opponents[i].rank)))) / 100))

            # For Losses
            elif history[i] == "l":
                if opponents[i] in self.losses:
                    self.melee_lvl -= (3.5 * ((opponents[i].rank * (math.log(opponents[i].rank)))/ 100))
                else:
                    self.losses.append(opponents[i])
                    self.melee_lvl -= (7 * ((opponents[i].rank * (math.log(opponents[i].rank)))/ 100))

            # For neither
            else:
                raise ValueError('NotWOrL')

        # Placement Integration?
        if placement == 1:
            placement = 10
        elif placement == 2:
            placement = 9
        elif placement == 3:
            placement = 8
        elif placement == 4:
            placement = 6
        elif placement == 5:
            placement = 4
        elif placement == 7:
            placemeent = 3
        elif placement == 9:
            placement = 2
        elif placement == 13:
            placement = 1
        elif placement == 17:
            placement = 0
        elif placement == 25:
            placement = -1
        elif placement == 33:
            placement = -2
        elif placement == 49:
            placement = -3
        elif placement == 65:
            placement = -4
        elif placement == 97:
            placement = -5
        elif placement == 129:
            placement = -6
        else:
            placement = 0
            print("Placement error with " + self.tag + " at " + tournament.name)

        neg = False
        if (placement - (10 - (tournament.size * 2))) < 0:
            neg = True

        p_s = ((placement - (10 - (tournament.size * 2)))**2) * tournament.size
        if neg == True:
            p_s *= -1

        self.melee_lvl += p_s

def sortAndPrintPlayers(players):
    players.sort(reverse=True)
    for i in range(len(players)):
        if players[i].sets_played != 0:
            print(players[i].tag + " - EAR-M: " + (str("{:.2f}".format(players[i].melee_lvl))))

def printPlayers(players):
    for i in range(len(players)):
        if players[i].sets_played != 0:
            print(players[i].tag + " | 2019 Rank: " + (str(players[i].rank)) + " | EAR-M: " + (str("{:.2f}".format(players[i].melee_lvl))))

def printTournaments(player):
    tournamentString = player.tag + ": "
    for i in range(len(player.tournaments)):
        tournamentString += (player.tournaments[i].name + ", ")
    print(tournamentString)

# GIANT LIST OF PLAYERS BELOW

Hungrybox = Player("Hungrybox", 1)
Leffen = Player("Leffen", 2)
Mango = Player("Mango", 3)
Axe = Player("Axe", 4)
Wizzrobe = Player("Wizzrobe", 5)
Zain = Player("Zain", 6)
aMSa = Player("aMSa", 7)
Plup = Player("Plup", 8)
iBDW = Player("iBDW", 9)
Mew2King = Player("Mew2King", 10)
S2J = Player("S2J", 11)
Fiction = Player("Fiction", 12)
SFAT = Player("SFAT", 13)
Moky = Player("moky", 14)
n0ne = Player("n0ne", 15)
Trif = Player("Trif", 16)
Captain_Faceroll = Player("Captain Faceroll", 17)
Swedish_Delight = Player("Swedish Delight", 18)
Hax = Player("Hax$", 19)
Lucky = Player("Lucky", 20)
Ginger = Player("Ginger", 21)
Spark = Player("Spark", 22)
ChuDat = Player("ChuDat", 23)
PewPewU = Player("PewPewU", 24)
ARMY = Player("ARMY", 25)
lloD = Player("lloD", 26)
AbsentPage = Player("AbsentPage", 27)
Bananas = Player("Bananas", 28)
KJH = Player("KJH", 29)
Shroomed = Player("Shroomed", 30)
Westballz = Player("Westballz", 31)
Medz = Player("Medz", 32)
MikeHaze = Player("MikeHaze", 33)
Professor_Pro = Player("Professor Pro", 34)
TwoSaint = Player("2Saint", 35)
Gahtzu = Player("Gahtzu", 36)
Albert = Player("Albert", 37)
Spud = Player("Spud", 38)
FatGoku = Player("FatGoku", 39)
Rishi = Player("Rishi", 40)
Bimbo = Player("Bimbo", 41)
Setchi = Player("Setchi", 42)
Magi = Player("Magi", 43)
Morsecode = Player("Morecode762", 44)
JakenShaken = Player("JakenShaken", 45)
HugS = Player("HugS86", 46)
Stango = Player("Stango", 47)
Zamu = Player("Zamu", 48)
Drephen = Player("Drephen", 49)
Michael = Player("Michael", 50)
Ice = Player("Ice", 51)
billybopeep = Player("billybopeep", 52)
La_Luna = Player("La Luna", 53)
Colbol = Player("Colbol", 54)
OverTriforce = Player("OverTriforce", 55)
Slox = Player("Slox", 56)
Kalamazhu = Player("Kalamazhu", 57)
Nickemwit = Player("Nickemwit", 58)
Jerry = Player("Jerry", 59)
Aura = Player("Aura", 60)
Nut = Player("Nut", 61)
Kalvar = Player("Kalvar", 62)
Polish = Player("Polish", 63)
Kevin_Maples = Player("Kevin Maples", 64)
Bladewise = Player("Bladewise", 65)
Tai = Player("Tai", 66)
Squid = Player("Squid", 67)
Forrest = Player("Forrest", 68)
Joyboy = Player("Joyboy", 69)
Kodorin = Player("KoDoRiN", 70)
Ryan_Ford = Player("Ryan Ford", 71)
Free_Palestine = Player("Free Palestine", 72)
Ryobeat = Player("Ryobeat", 73)
Ka_Master = Player("Ka-Master", 74)
Kurv = Player("Kurv", 75)
Frenzy = Player("Frenzy", 76)
MoG = Player("MoG", 77)
Boyd = Player("Boyd", 78)
Cool_Lime = Player("Cool Lime", 79)
BBB = Player("Bobby Big Ballz", 80)
Nintendude = Player("Nintendude", 81)
Franz = Player("Franz", 82)
Nicki = Player("Nicki", 83)
lint = Player("lint", 84)
King_Momo = Player("King Momo", 85)
TheRealThing = Player("TheRealThing", 86)
Umarth = Player("Umarth", 87)
Zeo = Player("Zeo", 88)
Pricent = Player("Pricent", 89)
Prince_Abu = Player("Prince Abu", 90)
Amsah = Player("Amsah", 91)
Rocky = Player("Rocky", 92)
Sharkz = Player("Sharkz", 93)
HTwa = Player("HTwa", 94)
Kage = Player("Kage", 95)
Schythed = Player("Schythed", 96)
Panda = Player("Panda", 97)
Soonsay = Player("Soonsay", 98)
TheSWOOPER = Player("TheSWOOPER", 99)
Snowy = Player("Snowy", 100)
Plus100 = Player("Player Worse than Rank 100", 101)

player_list = [Hungrybox, Leffen, Mango, Axe, Wizzrobe, Zain, aMSa, Plup, iBDW, Mew2King, S2J, Fiction, SFAT, Moky, n0ne, Trif, Captain_Faceroll, Swedish_Delight, Hax, Lucky, Ginger, Spark, ChuDat, PewPewU, ARMY, lloD, AbsentPage, Bananas, KJH, Shroomed, Westballz, Medz, MikeHaze, Professor_Pro, TwoSaint, Gahtzu, Albert, Spud, FatGoku, Rishi, Bimbo, Setchi, Magi, Morsecode, JakenShaken, HugS, Stango, Zamu, Drephen, Michael, Ice, billybopeep, La_Luna, Colbol, OverTriforce, Slox, Kalamazhu, Nickemwit, Jerry, Aura, Nut, Kalvar, Polish, Kevin_Maples, Bladewise, Tai, Squid, Forrest, Joyboy, Kodorin, Ryan_Ford, Free_Palestine, Ryobeat, Ka_Master, Kurv, Frenzy, MoG, Boyd, Cool_Lime, BBB, Nintendude, Franz, Nicki, lint, King_Momo, TheRealThing, Umarth, Zeo, Pricent, Prince_Abu, Amsah, Rocky, Sharkz, HTwa, Kage, Schythed, Panda, Soonsay, TheSWOOPER, Snowy]

# GIANT LIST OF PLAYERS DONE

# SIZE TO NUMBERS
# 5 = Super Major
# 4 = Major
# 3 = Super regional
# 2 = Regional
# 1 = Super Local

Valhalla3 = Tournament("Valhalla III", 3, "Leffen")
Genesis7 = Tournament("Genesis 7", 5, "Zain")
VerdugoWest95 = Tournament("Melee at Verdugo West 95", 1, "Westballz")
SavingMrLombardi2 = Tournament("Saving Mr. Lombardi 2", 3, "Fiction")
Nimbus70 = Tournament("Nimbus 70", 1, "S2J")
SmashSummit9 = Tournament("Smash Summit 9", 4, "Hungrybox")


def main():
    # Hungrybox
    Hungrybox1O = [Spud, Captain_Faceroll, PewPewU, Zain, Fiction, Hax, Mango, Zain]
    Hungrybox1R = ["w", "w", "w", "l", "w", "w", "w", "l"]
    Hungrybox2O = [Hax, aMSa, Mango, Fiction, Plup, n0ne, Mango, Plup, Plup, Plup]
    Hungrybox2R = ["w", "w", "w", "w", "w", "w", "w", "w", "l", "w"]
    Hungrybox.lvl_calculator(Genesis7, 2, Hungrybox1O, Hungrybox1R)
    Hungrybox.lvl_calculator(SmashSummit9, 1, Hungrybox2O, Hungrybox2R)

    # Leffen
    Leffen1O = [Frenzy, Professor_Pro, Professor_Pro]
    Leffen1R = ["w", "w", "w"]
    Leffen2O = [Schythed, MikeHaze, Hax, Fiction, Mango, Hax]
    Leffen2R = ["w", "w", "w", "w", "l", "l"]
    Leffen3O = [Spark, Wizzrobe, Axe, n0ne, Zain, BBB, Mango, iBDW]
    Leffen3R = ["w", "w", "w", "w", "l", "w", "l", "l"]
    Leffen.lvl_calculator(Valhalla3, 1, Leffen1O, Leffen1R)
    Leffen.lvl_calculator(Genesis7, 5, Leffen2O, Leffen2R)
    Leffen.lvl_calculator(SmashSummit9, 9, Leffen3O, Leffen3R)

    # Mango
    Mango1O = [Nicki, Trif, aMSa, Leffen, Zain, Hungrybox]
    Mango1R = ["w", "w", "w", "w", "l", "l"]
    Mango2O = [Shroomed, Fiction, Hungrybox, aMSa, Hax, Plup, Leffen, Hungrybox, Axe, Zain, Plup]
    Mango2R = ["w", "w", "l", "w", "w", "l", "w", "l", "w", "w", "l"]
    Mango.lvl_calculator(Genesis7, 3, Mango1O, Mango1R)
    Mango.lvl_calculator(SmashSummit9, 3, Mango2O, Mango2R)

    # Axe
    # Axe has a loss to pchythed but it's at a tournament too small for me to even consider it a super local
    Axe1O = [Panda, Plup]
    Axe1R = ["l", "l"]
    Axe2O = [Zain, Leffen, Spark, Wizzrobe, Plup, aMSa, Fiction, Mango]
    Axe2R = ["w", "l", "w", "w", "l",  "w", "w", "l"]
    Axe.lvl_calculator(Genesis7, 33, Axe1O, Axe1R)
    Axe.lvl_calculator(SmashSummit9, 5, Axe2O, Axe2R)

    # Wizzrobe
    Wizzrobe1O = [Ryobeat, Medz, Spark, Captain_Faceroll]
    Wizzrobe1R = ["l", "w", "w", "l"]
    Wizzrobe2O = [Leffen, Wizzrobe, iBDW, Axe, Fiction]
    Wizzrobe2R = ["l", "l", "l", "l", "l"]
    Wizzrobe.lvl_calculator(Genesis7, 17, Wizzrobe1O, Wizzrobe1R)
    Wizzrobe.lvl_calculator(SmashSummit9, 9, Wizzrobe2O, Wizzrobe2R)

    # Zain
    Zain1O = [Boyd, JakenShaken, Shroomed, Hungrybox, Mango, Hungrybox]
    Zain1R = ["w", "w", "w", "w", "w", "w"]
    Zain2O = [n0ne, Axe, Wizzrobe, iBDW, Leffen, Fiction, Plup, iBDW, Mango]
    Zain2R = ["w", "l", "w", "w", "w", "w", "l", "w", "l"]
    Zain.lvl_calculator(Genesis7, 1, Zain1O, Zain1R)
    Zain.lvl_calculator(SmashSummit9, 4, Zain2O, Zain2R)

    # aMSa
    aMSa1O = [Ice, Mew2King, Mango, n0ne]
    aMSa1R = ["w", "w", "l", "l"]
    aMSa2O = [Magi, Hungrybox, Pricent, Mango, Fiction, Shroomed, BBB, Axe]
    aMSa2R = ["w", "l", "w", "l", "l", "w", "w", "l"]
    aMSa.lvl_calculator(Genesis7, 9, aMSa1O, aMSa1R)
    aMSa.lvl_calculator(SmashSummit9, 9, aMSa2O, aMSa2R)

    # Plup
    Plup1O = [Rocky, PewPewU, Axe, ARMY]
    Plup1R = ["w", "l", "w", "l"]
    Plup2O = [Hax, Shroomed, Magi, Hungrybox, Mango, Axe, Zain, Hungrybox, Mango, Hungrybox, Hungrybox]
    Plup2R = ["l", "w", "w", "l", "w", "w", "w", "l", "w", "w", "l"]
    Plup.lvl_calculator(Genesis7, 25, Plup1O, Plup1R)
    Plup.lvl_calculator(SmashSummit9, 2, Plup2O, Plup2R)

    # iBDW
    iBDW1O = [BBB, ARMY, PewPewU, Ice, Captain_Faceroll]
    iBDW1R = ["w", "w", "l", "w", "l"]
    iBDW2O = [Trif, ARMY, Albert, Lucky, Kalamazhu, Squid, Professor_Pro, Fiction, S2J, Fiction]
    iBDW2R = ["w", "l", "w", "w", "w", "w", "w", "l", "w", "l"]
    iBDW3O = [BBB, n0ne, Zain, Wizzrobe, Spark, Pricent, Leffen, Hax, Zain]
    iBDW3R = ["w", "l", "l", "w", "w", "w", "w", "w", "l"]
    iBDW.lvl_calculator(Genesis7, 13, iBDW1O, iBDW1R)
    iBDW.lvl_calculator(SavingMrLombardi2, 2, iBDW2O, iBDW2R)
    iBDW.lvl_calculator(SmashSummit9, 5, iBDW3O, iBDW3R)

    # Mew2King
    Mew2King1O = [Soonsay, Professor_Pro, aMSa, ARMY, Swedish_Delight]
    Mew2King1R = ["w", "w", "l", "w", "l"]
    Mew2King.lvl_calculator(Genesis7, 13, Mew2King1O, Mew2King1R)

    # S2J
    S2J1O = [Joyboy, Zain, Ryobeat, n0ne]
    S2J1R = ["w", "l", "w", "l"]
    S2J2O = [Kodorin, Trif, Captain_Faceroll, Trif]
    S2J2R = ["w", "w", "w", "w"]
    S2J3O = [Ginger, Westballz, Ice, Prince_Abu, Franz, Kalamazhu, Professor_Pro, Lucky, Ginger, Professor_Pro, iBDW]
    S2J3R = ["w", "w", "w", "w", "w", "l", "w", "w", "w", "w", "l"]
    S2J.lvl_calculator(Genesis7, 13, S2J1O, S2J1R)
    S2J.lvl_calculator(Nimbus70, 1, S2J2O, S2J2R)
    S2J.lvl_calculator(SavingMrLombardi2, 3, S2J3O, S2J3R)

    # Fiction
    Fiction1O = [Free_Palestine, ChuDat, Westballz, Leffen, Captain_Faceroll, n0ne, Hungrybox]
    Fiction1R = ["w", "w", "w", "l", "w", "w", "l"]
    Fiction2O = [Westballz, Kurv, Ginger]
    Fiction2R = ["l", "w", "l"]
    Fiction3O = [Spark, Lucky, Bimbo, ARMY, Ginger, iBDW, iBDW]
    Fiction3R = ["w", "l", "w", "w", "w", "w", "w"]
    Fiction4O = [Pricent, Mango, Hax, Hungrybox, aMSa, Magi, Zain, Wizzrobe, Axe]
    Fiction4R = ["w", "l", "w", "l", "w", "w", "l", "w", "l"]
    Fiction.lvl_calculator(Genesis7, 5, Fiction1O, Fiction1R)
    Fiction.lvl_calculator(VerdugoWest95, 4, Fiction2O, Fiction2R)
    Fiction.lvl_calculator(SavingMrLombardi2, 1, Fiction3O, Fiction3R)
    Fiction.lvl_calculator(SmashSummit9, 7, Fiction4O, Fiction4R)

    # SFAT
    SFAT1O = [Tai, Ginger, billybopeep, Panda, Hax]
    SFAT1R = ["w", "l", "w", "w", "l"]
    SFAT2O = [Professor_Pro, Captain_Faceroll, Ginger, Trif]
    SFAT2R = ["w", "l", "w", "l"]
    SFAT3O = [Captain_Faceroll, MikeHaze, Professor_Pro, Kodorin, Nut, Ginger, Trif]
    SFAT3R = ["w", "l", "w", "w", "w", "l", "l"]
    SFAT.lvl_calculator(Genesis7, 17, SFAT1O, SFAT1R)
    SFAT.lvl_calculator(Nimbus70, 4, SFAT2O, SFAT2R)
    SFAT.lvl_calculator(SavingMrLombardi2, 9, SFAT3O, SFAT3R)

    # moky
    Moky1O = [Forrest, Nut, Kevin_Maples, Ryobeat]
    Moky1R = ["l", "w", "l", "w"]
    Moky.lvl_calculator(Genesis7, 33, Moky1O, Moky1R)

    # n0ne
    n0ne1O = [Kodorin, Hax, MikeHaze, Ginger, S2J, aMSa, Fiction]
    n0ne1R = ["w", "l", "w", "w", "w", "w", "l"]
    n0ne2O = [Zain, iBDW, Leffen, Spark, Ryobeat, Hungrybox, Hax]
    n0ne2R = ["l", "w", "l", "w", "w", "l", "l"]
    n0ne.lvl_calculator(Genesis7, 7, n0ne1O, n0ne1R)
    n0ne.lvl_calculator(SmashSummit9, 9, n0ne2O, n0ne2R)

    # Trif
    Trif1O = [Plus100, Frenzy, Plus100]
    Trif1R = ["l", "w", "l"]
    Trif2O = [Forrest, Mango, Swedish_Delight]
    Trif2R = ["w", "l", "l"]
    Trif3O = [Ginger, S2J, Westballz, SFAT, Captain_Faceroll, S2J]
    Trif3R = ["w", "l", "w", "w", "w", "l"]
    Trif4O = [iBDW, ARMY, Albert, Kalamazhu, Squid, SFAT, ARMY]
    Trif4R = ["l", "l", "w", "w", "w", "w", "l"]
    Trif.lvl_calculator(Valhalla3, 4, Trif1O, Trif1R)
    Trif.lvl_calculator(Genesis7, 17, Trif2O, Trif2R)
    Trif.lvl_calculator(SavingMrLombardi2, 7, Trif3O, Trif3R)

    # Main part
    # printPlayers(player_list)
    sortAndPrintPlayers(player_list)

if __name__ == "__main__":
    main()
