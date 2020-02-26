# ETossed's Algorithmic Ranking of Melee
# This is a MAJOR work in progress, and I'm getting a foundation down for
# a more advanced ranking at some point

# Tournament is to be implemented in more complicated ELO system later
# Non-Local tournamnets are the only one that counts. Superlocals (i.e. Nimbus 70) do count.

import math

class Tournament(object):
    def __init__(self, name, size, winner):
        self.name = name
        self.size = size
        self.winner = winner

    def __repr__(self):
        temp = None
        if self.size == 1:
            temp = "Superlocal (Non-Cali)"
        if self.size == 2:
            temp = "Regional"
        elif self.size == 3:
            temp = "Super Regional"
        elif self.size == 4:
            temp = "Major"
        elif self.size == 5:
            temp = "Super Major"
        return "Tournament: " + self.name + "| Size: " + temp + " | Winner: " + self.winner.tag

class Player(object):
    def __init__(self, tag, rank):
        self.tag = tag
        self.rank = rank
        self.sets_played = 0
        self.tournaments = []
        self.wins = []
        self.losses = []
        self.melee_lvl = 1000

    def __lt__(self, other):
        return self.melee_lvl < other.melee_lvl

    def __repr__(self):
        return self.tag + " EAR-M: " + str(self.melee_lvl)

    def printTournaments(self):
        tournamentString = self.tag + "'s Tournaments Attended: "
        for i in range(len(self.tournaments)):
            tournamentString += ("\n" + self.tournaments[i].name)
        print(tournamentString)

    # ACTUAL CALCULATION DONE BELOW
    # STATIC ALGORITHM
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
            placement = 3
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

def printSortedPlayers(players):
    players.sort(reverse=True)
    newPlayerList = []
    for i in range(len(players)):
        if players[i].melee_lvl != 1000:
            newPlayerList.append(players[i])
    for i in range(len(newPlayerList)):
        print(str(i+1) + ". " + newPlayerList[i].tag + " | 2019 Rank: " + (str(newPlayerList[i].rank)) + " | EAR-M: " + (str("{:.2f}".format(newPlayerList[i].melee_lvl))) + "\n")

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
HugS = Player("HugS", 46)
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
Kodorin = Player("Kodorin", 70)
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

# TOURNAMENTS CONSIDERED

Valhalla3 = Tournament("Valhalla III", 3, Leffen)
Genesis7 = Tournament("Genesis 7", 5, Zain)
SavingMrLombardi2 = Tournament("Saving Mr. Lombardi 2", 3, Fiction)
SmashSummit9 = Tournament("Smash Summit 9", 4, Hungrybox)
HTL5 = Tournament("Hold That L 5", 1, Ginger)
DreamhackAnaheim = Tournament("Dreamhack Anaheim 2020", 2, Fiction)

def main():
    # If a player's comment says "NONE" it means they have not attended any tournaments on the list above

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
    S2J2O = [Ginger, Westballz, Ice, Prince_Abu, Franz, Kalamazhu, Professor_Pro, Lucky, Ginger, Professor_Pro, iBDW]
    S2J2R = ["w", "w", "w", "w", "w", "l", "w", "w", "w", "w", "l"]
    S2J3O = [Tai, ARMY, Fiction, Westballz, Fiction, Fiction]
    S2J3R = ["w", "w", "l", "w", "w", "l"]
    S2J.lvl_calculator(Genesis7, 13, S2J1O, S2J1R)
    S2J.lvl_calculator(SavingMrLombardi2, 3, S2J2O, S2J2R)
    S2J.lvl_calculator(DreamhackAnaheim, 2, S2J3O, S2J3R)

    # Fiction
    Fiction1O = [Free_Palestine, ChuDat, Westballz, Leffen, Captain_Faceroll, n0ne, Hungrybox]
    Fiction1R = ["w", "w", "w", "l", "w", "w", "l"]
    Fiction2O = [Spark, Lucky, Bimbo, ARMY, Ginger, iBDW, iBDW]
    Fiction2R = ["w", "l", "w", "w", "w", "w", "w"]
    Fiction3O = [Pricent, Mango, Hax, Hungrybox, aMSa, Magi, Zain, Wizzrobe, Axe]
    Fiction3R = ["w", "l", "w", "l", "w", "w", "l", "w", "l"]
    Fiction4O = [Westballz, S2J, S2J, S2J]
    Fiction4R = ["w", "w", "l", "w"]
    Fiction.lvl_calculator(Genesis7, 5, Fiction1O, Fiction1R)
    Fiction.lvl_calculator(SavingMrLombardi2, 1, Fiction2O, Fiction2R)
    Fiction.lvl_calculator(SmashSummit9, 7, Fiction3O, Fiction3R)
    Fiction.lvl_calculator(DreamhackAnaheim, 1, Fiction4O, Fiction4R)

    # SFAT
    SFAT1O = [Tai, Ginger, billybopeep, Panda, Hax]
    SFAT1R = ["w", "l", "w", "w", "l"]
    SFAT2O = [Captain_Faceroll, MikeHaze, Professor_Pro, Kodorin, Nut, Ginger, Trif]
    SFAT2R = ["w", "l", "w", "w", "w", "l", "l"]
    SFAT.lvl_calculator(Genesis7, 17, SFAT1O, SFAT1R)
    SFAT.lvl_calculator(SavingMrLombardi2, 9, SFAT2O, SFAT2R)

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

    # Captain Faceroll
    CF1O = [Bladewise, Swedish_Delight, Hungrybox, Wizzrobe, iBDW, Fiction]
    CF1R = ["w", "w", "l", "w", "w", "l"]
    CF2O = [SFAT, MikeHaze, Professor_Pro, Kodorin, Nut, Prince_Abu, ARMY]
    CF2R = ["l", "l", "l", "w", "w", "w", "l"]
    Captain_Faceroll.lvl_calculator(Genesis7, 9, CF1O, CF1R)
    Captain_Faceroll.lvl_calculator(SavingMrLombardi2, 9, CF2O, CF2R)

    # Swedish Delight
    SD1O = [Kevin_Maples, Captain_Faceroll, La_Luna, Trif, Mew2King, Shroomed]
    SD1R = ["w", "l", "w", "w", "w", "l"]
    Swedish_Delight.lvl_calculator(Genesis7, 9, SD1O, SD1R)

    # Hax$
    Hax1O = [Aura, n0ne, Leffen, SFAT, Westballz, PewPewU, Shroomed, Leffen, Hungrybox]
    Hax1R = ["w", "w", "l", "w", "w", "w", "w", "w", "l"]
    Hax2O = [Hungrybox, Plup, Fiction, Mango, Pricent, Spark, n0ne, iBDW]
    Hax2R = ["l", "w", "l", "l", "w", "w", "w", "l"]
    Hax.lvl_calculator(Genesis7, 4, Hax1O, Hax1R)
    Hax.lvl_calculator(SmashSummit9, 7, Hax2O, Hax2R)

    # Lucky
    Lucky1O = [Ice, Plus100]
    Lucky1R = ["l", "l"]
    Lucky2O = [Fiction, Spark, Bimbo, Plus100, iBDW, MikeHaze, S2J]
    Lucky2R = ["w", "w", "w", "l", "l", "w", "l"]
    Lucky3O = [Squid, Westballz, Plus100]
    Lucky3R = ["w", "l", "l"]
    Lucky.lvl_calculator(Genesis7, 65, Lucky1O, Lucky1R)
    Lucky.lvl_calculator(SavingMrLombardi2, 7, Lucky2O, Lucky2R)
    Lucky.lvl_calculator(DreamhackAnaheim, 9, Lucky3O, Lucky3R)

    # Ginger
    Ginger1O = [Kalvar, SFAT, Shroomed, n0ne]
    Ginger1R = ["w", "w", "l", "l"]
    Ginger2O = [S2J, Westballz, Ice, Prince_Abu, Franz, SFAT, Fiction, S2J]
    Ginger2R = ["l", "l", "w", "w", "w", "w", "l", "l"]
    Ginger3O = [Prince_Abu, Magi, Magi]
    Ginger3R = ["w", "w", "w"]
    Ginger.lvl_calculator(Genesis7, 17, Ginger1O, Ginger1R)
    Ginger.lvl_calculator(SavingMrLombardi2, 5, Ginger2O, Ginger2R)
    Ginger.lvl_calculator(HTL5, 1, Ginger3O, Ginger3R)

    # Spark
    Spark1O = [Plus100, Free_Palestine, Wizzrobe]
    Spark1R = ["l", "w", "l"]
    Spark2O = [Fiction, Lucky, Bimbo, Plus100]
    Spark2R = ["l", "l", "w", "l"]
    Spark3O = [Leffen, Ryobeat, Axe, n0ne, iBDW, Hax]
    Spark3R = ["l", "w", "l", "l", "l", "l"]
    Spark.lvl_calculator(Genesis7, 25, Spark1O, Spark1R)
    Spark.lvl_calculator(SavingMrLombardi2, 17, Spark2O, Spark2R)
    Spark.lvl_calculator(SmashSummit9, 13, Spark3O, Spark3R)

    # ChuDat
    ChuDat1O = [Fiction, TheSWOOPER]
    ChuDat1R = ["l", "l"]
    ChuDat.lvl_calculator(Genesis7, 33, ChuDat1O, ChuDat1R)

    # PewPewU
    PPU1O = [HugS, Plup, iBDW, Hungrybox, Hax]
    PPU1R = ["w", "w", "w", "l", "l"]
    PewPewU.lvl_calculator(Genesis7, 9, PPU1O, PPU1R)

    # lloD
    # NONE

    # ARMY
    ARMY1O = [Drephen, iBDW, Aura, Plup, Mew2King]
    ARMY1R = ["w", "l", "w", "w", "l"]
    ARMY2O = [iBDW, Trif, Albert, Kalamazhu, Squid, Fiction, Captain_Faceroll, Trif, Professor_Pro]
    ARMY2R = ["w", "w", "w", "l", "w", "l", "w", "w", "l"]
    ARMY3O = [Nut, S2J, Westballz]
    ARMY3R = ["w", "l", "l"]
    ARMY.lvl_calculator(Genesis7, 17, ARMY1O, ARMY1R)
    ARMY.lvl_calculator(SavingMrLombardi2, 5, ARMY2O, ARMY2R)
    ARMY.lvl_calculator(DreamhackAnaheim, 4, ARMY3O, ARMY3R)

    # AbsentPage
    # NONE

    # Bananas
    # NONE

    # KJH
    # NONE

    # Shroomed
    Shroomed1O = [Rishi, Panda, Ginger, Zain, Swedish_Delight, Hax]
    Shroomed1R = ["w", "w", "w", "l", "w", "l"]
    Shroomed2O = [Mango, Magi, Plup, Pricent, aMSa]
    Shroomed2R = ["l", "w", "l", "l", "l"]
    Shroomed.lvl_calculator(Genesis7, 7, Shroomed1O, Shroomed1R)
    Shroomed.lvl_calculator(SmashSummit9, 17, Shroomed2O, Shroomed2R)

    # Westballz
    Westballz1O = [Ryobeat, Fiction, Hax]
    Westballz1R = ["w", "l", "l"]
    Westballz2O = [S2J, Ginger, Ice, Prince_Abu, Franz, MikeHaze]
    Westballz2R = ["l", "w", "l", "l", "w", "l"]
    Westballz3O = [Schythed, Lucky, Fiction, Tai, ARMY, S2J]
    Westballz3R = ["w", "w", "l", "w", "w", "l"]
    Westballz.lvl_calculator(Genesis7, 13, Westballz1O, Westballz1R)
    Westballz.lvl_calculator(SavingMrLombardi2, 13, Westballz1O, Westballz1R)
    Westballz.lvl_calculator(DreamhackAnaheim, 3, Westballz3O, Westballz3R)

    # Medz
    Medz1O = [JakenShaken, Wizzrobe]
    Medz1R = ["l", "l"]
    Medz.lvl_calculator(Genesis7, 49, Medz1O, Medz1R)

    # Professor_Pro
    Prof1O = [Leffen, Leffen]
    Prof1R = ["l", "l"]
    Prof2O = [billybopeep, Mew2King, Kodorin, Ice]
    Prof2R = ["w", "l", "w", "l"]
    Prof3O = [SFAT, Captain_Faceroll, MikeHaze, Kodorin, Nut, S2J, iBDW, ARMY, S2J]
    Prof3R = ["l", "w", "w", "w", "w", "w", "l", "w", "l"]
    Professor_Pro.lvl_calculator(Valhalla3, 2, Prof1O, Prof1R)
    Professor_Pro.lvl_calculator(Genesis7, 25, Prof2O, Prof2R)
    Professor_Pro.lvl_calculator(SavingMrLombardi2, 4, Prof3O, Prof3R)

    # 2Saint
    # NONE

    # Gahtzu
    Gahtzu1O = [Plus100, Plus100]
    Gahtzu1R = ["l", "l"]
    Gahtzu.lvl_calculator(Genesis7, 49, Gahtzu1O, Gahtzu1R)

    # Albert
    Albert1O = [iBDW, Trif, ARMY, Kalamazhu, Squid]
    Albert1R = ["l", "l", "l", "l", "w"]
    Albert2O = [Plus100, Tai]
    Albert2R = ["l", "l"]
    Albert.lvl_calculator(SavingMrLombardi2, 17, Albert1O, Albert1R)
    Albert.lvl_calculator(DreamhackAnaheim, 9, Albert2O, Albert2R)

    # Spud
    Spud1O = [FatGoku, Hungrybox, La_Luna]
    Spud1R = ["w", "l", "l"]
    Spud.lvl_calculator(Genesis7, 33, Spud1O, Spud1R)

    # FatGoku
    FatGoku1O = [Spud, Plus100]
    FatGoku1R = ["l", "l"]
    FatGoku2O = [TheSWOOPER, Magi, Drephen, Prince_Abu]
    FatGoku2R = ["w", "l", "w", "l"]
    FatGoku.lvl_calculator(Genesis7, 65, FatGoku1O, FatGoku1R)
    FatGoku.lvl_calculator(HTL5, 4, FatGoku1O, FatGoku1R)

    # Rishi
    Rishi1O = [Shroomed, Ice]
    Rishi1R = ["l", "l"]
    Rishi.lvl_calculator(Genesis7, 49, Rishi1O, Rishi1R)

    # Bimbo
    Bimbo1O = [Plus100, TheSWOOPER]
    Bimbo1R = ["l", "l"]
    Bimbo2O = [Fiction, Spark, Lucky, Plus100, Plus100]
    Bimbo2R = ["l", "l", "l", "l", "l"]
    Bimbo.lvl_calculator(Genesis7, 97, Bimbo1O, Bimbo1R)
    Bimbo.lvl_calculator(SavingMrLombardi2, 25, Bimbo2O, Bimbo2R)

    # Setchi
    # NONE

    # Magi
    Magi1O = [Plus100, Plus100]
    Magi1R = ["l", "l"]
    Magi2O = [aMSa, Shroomed, Plup, Pricent, Fiction, Wizzrobe]
    Magi2R = ["l", "l", "l", "w", "l", "l"]
    Magi3O = [TheRealThing, FatGoku, Ginger, Prince_Abu, Ginger]
    Magi3R = ["w", "w", "l", "w", "l"]
    Magi.lvl_calculator(Genesis7, 129, Magi1O, Magi1R)
    Magi.lvl_calculator(SmashSummit9, 13, Magi2O, Magi2R)
    Magi.lvl_calculator(HTL5, 2, Magi3O, Magi3R)

    # Morsecode762
    # NONE

    # JakenShaken
    JS1O = [Medz, Zain, Plus100]
    JS1R = ["w", "l", "l"]
    JakenShaken.lvl_calculator(Genesis7, 33, JS1O, JS1R)

    # HugS
    Hugs1O = [PewPewU, Prince_Abu]
    Hugs1R = ["l", "l"]
    Hugs2O = [Plus100, Squid]
    Hugs2R = ["l", "l"]
    HugS.lvl_calculator(Genesis7, 65, Hugs1O, Hugs1R)
    HugS.lvl_calculator(SavingMrLombardi2, 33, Hugs2O, Hugs2R)

    # Stango
    # NONE

    # Zamu
    Zamu1O = [Plus100, Wizzrobe]
    Zamu1R = ["l", "l"]
    Zamu.lvl_calculator(Genesis7, 65, Zamu1O, Zamu1R)

    # Drephen
    Drephen1O = [ARMY, Plus100]
    Drephen1R = ["l", "l"]
    Drephen2O = [Prince_Abu, FatGoku]
    Drephen2R = ["l", "l"]
    Drephen.lvl_calculator(Genesis7, 65, Drephen1O, Drephen1R)
    Drephen.lvl_calculator(HTL5, 5, Drephen2O, Drephen2R)

    # Michael
    # NONE

    # Ice
    Ice1O = [Lucky, aMSa, Rishi, Professor_Pro, iBDW]
    Ice1R = ["w", "l", "w", "w", "l"]
    Ice2O = [Westballz, Franz, S2J, Ginger, Prince_Abu]
    Ice2R = ["w", "w", "l", "l", "l"]
    Ice.lvl_calculator(Genesis7, 17, Ice1O, Ice1R)
    Ice.lvl_calculator(SavingMrLombardi2, 17, Ice2O, Ice2R)

    # billybopeep
    BBP1O = [Professor_Pro, BBB, SFAT]
    BBP1R = ["l", "w", "l"]
    billybopeep.lvl_calculator(Genesis7, 33, BBP1O, BBP1R)

    # La Luna
    LaLuna1O = [Plus100, Joyboy, Spud, Swedish_Delight]
    LaLuna1R = ["l", "w", "w", "l"]
    La_Luna.lvl_calculator(Genesis7, 25, LaLuna1O, LaLuna1R)

    # Colbol
    # NONE

    # OverTriforce
    Over1O = [Frenzy, Plus100]
    Over1R = ["l", "l"]
    OverTriforce.lvl_calculator(Valhalla3, 5, Over1O, Over1R)

    # Slox
    # NONE

    # Kalamazhu
    Kzhu1O = [Plus100, Plus100]
    Kzhu1R = ["l", "l"]
    Kzhu2O = [iBDW, Trif, ARMY, Albert, Squid, S2J]
    Kzhu2R = ["l", "w", "w", "w", "w", "l"]
    Kalamazhu.lvl_calculator(Genesis7, 97, Kzhu1O, Kzhu1R)
    Kalamazhu.lvl_calculator(SavingMrLombardi2, 9, Kzhu2O, Kzhu2R)

    # Nickemwit
    # NONE

    # Jerry
    # NONE

    # Aura
    Aura1O = [Hax, Tai, ARMY]
    Aura1R = ["l", "w", "l"]
    Aura.lvl_calculator(Genesis7, 33, Aura1O, Aura1R)

    # Nut
    Nut1O = [Plus100, Moky]
    Nut1R = ["l", "l"]
    Nut2O = [Prince_Abu, SFAT, Captain_Faceroll, MikeHaze, Professor_Pro, Kodorin]
    Nut2R = ["l", "l", "l", "l", "l", "l"]
    Nut3O = [Kurv, ARMY, Plus100]
    Nut3R = ["w", "l", "l"]
    Nut.lvl_calculator(Genesis7, 65, Nut1O, Nut1R)
    Nut.lvl_calculator(SavingMrLombardi2, 25, Nut2O, Nut2R)
    Nut.lvl_calculator(DreamhackAnaheim, 17, Nut3O, Nut3R)

    # Kalvar
    Kalvar1O = [Ginger, Plus100]
    Kalvar1R = ["l", "l"]
    Kalvar.lvl_calculator(Genesis7, 65, Kalvar1O, Kalvar1R)

    # Polish
    # NONE

    # Kevin Maples
    KevinMaples1O = [Swedish_Delight, Moky]
    KevinMaples1R = ["l", "l"]
    Kevin_Maples.lvl_calculator(Genesis7, 49, KevinMaples1O, KevinMaples1R)

    # Bladewise
    Bladewise1O = [Captain_Faceroll, Plus100]
    Bladewise1R = ["l", "l"]
    Bladewise.lvl_calculator(Genesis7, 65, Bladewise1O, Bladewise1R)

    # Tai
    Tai1O = [SFAT, Aura]
    Tai1R = ["l", "l"]
    Tai2O = [MikeHaze, S2J, Albert, Schythed, Westballz]
    Tai2R = ["w", "l", "w", "w", "l"]
    Tai.lvl_calculator(Genesis7, 49, Tai1O, Tai1R)
    Tai.lvl_calculator(DreamhackAnaheim, 5, Tai2O, Tai2R)

    # Squid
    Squid1O = [Franz, HugS, iBDW, Trif, ARMY, Albert, Kalamazhu]
    Squid1R = ["l", "w", "l", "l", "l", "l", "l"]
    Squid2O = [Lucky, Schythed]
    Squid2R = ["l", "l"]
    Squid.lvl_calculator(SavingMrLombardi2, 25, Squid1O, Squid1R)
    Squid.lvl_calculator(DreamhackAnaheim, 13, Squid2O, Squid2R)

    # Forrest
    Forrest1O = [HTwa, Moky, Trif, Wizzrobe]
    Forrest1R = ["w", "w", "l", "l"]
    Forrest.lvl_calculator(Genesis7, 33, Forrest1O, Forrest1R)

    # Joyboy
    Joyboy1O = [S2J, La_Luna]
    Joyboy1R = ["l", "l"]
    Joyboy.lvl_calculator(Genesis7, 65, Joyboy1O, Joyboy1R)

    # Kodorin
    Kodorin1O = [n0ne, Professor_Pro]
    Kodorin1R = ["l", "l"]
    Kodorin2O = [Franz, SFAT, Captain_Faceroll, MikeHaze, Professor_Pro, Nut]
    Kodorin2R = ["w", "l", "l", "w", "l", "w"]
    Kodorin.lvl_calculator(Genesis7, 33, Kodorin1O, Kodorin1R)
    Kodorin.lvl_calculator(SavingMrLombardi2, 17, Kodorin2O, Kodorin2R)

    # Ryan Ford
    # NONE

    # Free Palestine
    FP1O = [Fiction, Spark]
    FP1R = ["l", "l"]
    Free_Palestine.lvl_calculator(Genesis7, 49, FP1O, FP1R)

    # Ryobeat
    Ryobeat1O = [Umarth, Wizzrobe, Westballz, Moky, TheSWOOPER, S2J]
    Ryobeat1R = ["w", "w", "l", "w", "w", "l"]
    Ryobeat2O = [Axe, Spark, BBB, Wizzrobe, n0ne]
    Ryobeat2R = ["l", "l", "l", "l", "l"]
    Ryobeat.lvl_calculator(Genesis7, 17, Ryobeat1O, Ryobeat1R)
    Ryobeat.lvl_calculator(SmashSummit9, 17, Ryobeat2O, Ryobeat2R)

    # Ka-Master
    # NONE

    # Kurv
    Kurv1O = [Plus100, Plus100]
    Kurv1R = ["l", "l"]
    Kurv2O = [Plus100, Plus100]
    Kurv2R = ["l", "l"]
    Kurv3O = [Plus100, Nut]
    Kurv3R = ["l", "l"]
    Kurv.lvl_calculator(Genesis7, 97, Kurv1O, Kurv1R)
    Kurv.lvl_calculator(SavingMrLombardi2, 33, Kurv2O, Kurv2R)
    Kurv.lvl_calculator(DreamhackAnaheim, 33, Kurv3O, Kurv3R)

    # Frenzy
    Frenzy1O = [OverTriforce, Leffen, Trif]
    Frenzy1R = ["w", "l", "l"]
    Frenzy.lvl_calculator(Valhalla3, 5, Frenzy1O, Frenzy1R)

    # MoG
    # NONE

    # Boyd
    Boyd1O = [Zain, Plus100]
    Boyd1R = ["l", "l"]
    Boyd.lvl_calculator(Genesis7, 65, Boyd1O, Boyd1R)

    # Cool Lime
    # NONE

    # Bobby Big Ballz
    BBB1O = [iBDW, billybopeep]
    BBB1R = ["l", "l"]
    BBB2O = [Wizzrobe, iBDW, Ryobeat, Axe, Leffen, aMSa]
    BBB2R = ["l", "l", "w", "l", "l", "l"]
    BBB.lvl_calculator(Genesis7, 49, BBB1O, BBB1R)
    BBB.lvl_calculator(SmashSummit9, 13, BBB2O, BBB2R)

    # Nintendude
    Nintendude1O = [Panda, Plus100]
    Nintendude1R = ["l", "l"]
    Nintendude.lvl_calculator(Genesis7, 97, Nintendude1O, Nintendude1R)

    # Franz
    Franz1O = [Plus100, Plus100]
    Franz1R = ["l", "l"]
    Franz2O = [Squid, Kodorin, S2J, Ginger, Westballz, Ice, Prince_Abu]
    Franz2R = ["w", "l", "l", "l", "l", "l", "l"]
    Franz.lvl_calculator(Genesis7, 129, Franz1O, Franz1R)
    Franz.lvl_calculator(SavingMrLombardi2, 25, Franz1O, Franz1R)

    # Nicki
    Nicki1O = [Mango, TheSWOOPER]
    Nicki1R = ["l", "l"]
    Nicki.lvl_calculator(Genesis7, 65, Nicki1O, Nicki1R)

    # Lint
    # NONE

    # King Momo
    # NONE

    # TheRealThing
    TRT1O = [Schythed, Plus100]
    TRT1R = ["l", "l"]
    TRT2O = [Magi, Prince_Abu]
    TRT2R = ["l", "l"]
    TheRealThing.lvl_calculator(Genesis7, 65, TRT1O, TRT1R)
    TheRealThing.lvl_calculator(HTL5, 5, TRT2O, TRT2R)

    # Umarth
    Umarth1O = [Ryobeat, Plus100]
    Umarth1R = ["l", "l"]
    Umarth.lvl_calculator(Genesis7, 65, Umarth1O, Umarth1R)

    # Zeo
    Zeo1O = [Plus100, Plus100]
    Zeo1R = ["l", "l"]
    Zeo.lvl_calculator(SavingMrLombardi2, 25, Zeo1O, Zeo1R)

    # Pricent
    Pricent1O = [Fiction, aMSa, Shroomed, Magi, Hax, iBDW]
    Pricent1R = ["l", "l", "w", "l", "l", "l"]
    Pricent.lvl_calculator(SmashSummit9, 13, Pricent1O, Pricent1R)

    # Prince Abu
    PA1O = [Rocky, HugS, MikeHaze]
    PA1R = ["l", "w", "l"]
    PA2O = [Nut, S2J, Ginger, Westballz, Ice, Franz, Captain_Faceroll]
    PA2R = ["w", "l", "l", "w", "w", "w", "l"]
    PA3O = [Drephen, Ginger, TheRealThing, FatGoku, Magi]
    PA3R = ["w", "l", "w", "w", "l"]
    Prince_Abu.lvl_calculator(Genesis7, 33, PA1O, PA1R)
    Prince_Abu.lvl_calculator(SavingMrLombardi2, 13, PA2O, PA2R)
    Prince_Abu.lvl_calculator(HTL5, 3, PA3O, PA3R)

    # Amsah
    # NONE

    # Rocky
    Rocky1O = [Prince_Abu, Plup, Plus100]
    Rocky1R = ["w", "l", "l"]
    Rocky.lvl_calculator(Genesis7, 49, Rocky1O, Rocky1R)

    # Sharkz
    # NONE

    # HTwa
    HTwa1O = [Forrest, Plus100]
    HTwa1R = ["l", "l"]
    HTwa.lvl_calculator(Genesis7, 129, HTwa1O, HTwa1R)

    # Kage
    # NONE

    # Schythed
    Schythed1O = [TheRealThing, Leffen, Plus100]
    Schythed1R = ["w", "l", "l"]
    Schythed.lvl_calculator(Genesis7, 65, Schythed1O, Schythed1R)

    # Panda
    Panda1O = [Nintendude, Axe, Shroomed, SFAT]
    Panda1R = ["w", "w", "l", "l"]
    Panda.lvl_calculator(Genesis7, 25, Panda1O, Panda1R)

    # Soonsay
    Soonsay1O = [Mew2King, Plus100]
    Soonsay1R = ["l", "l"]
    Soonsay.lvl_calculator(Genesis7, 65, Soonsay1O, Soonsay1R)

    # TheSWOOPER
    TS1O = [Plus100, Bimbo, Nicki, ChuDat, Ryobeat]
    TS1R = ["l", "w", "w", "w", "l"]
    TS2O = [FatGoku, Plus100]
    TS2R = ["l", "l"]
    TheSWOOPER.lvl_calculator(Genesis7, 25, TS1O, TS1R)
    TheSWOOPER.lvl_calculator(HTL5, 9, TS2O, TS2R)

    # Snowy
    # NONE

    # TOP 100 MPGR PLAYERS DONE

    # Main part
    printSortedPlayers(player_list)

if __name__ == "__main__":
    main()
