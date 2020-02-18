# ETossed's Algorithmic Ranking of Melee
# This is a MAJOR work in progress, and I'm getting a foundation down for
# a more advanced ranking at some point

class Player(object):
    def __init__(self, tag, rank):
        self.tag = tag
        self.rank = rank
        self.sets_played = 0
        self.tournaments = []
        self.melee_lvl = 0

    def __lt__(self, other):
        return self.melee_lvl < other.melee_lvl

    def __repr__(self):
        return self.tag + " EAR-M: " + str(self.melee_lvl)

    def lvl_calculator(self, tournament, opponents, history):
        # Tournament is the tournament that was attended
        # Opponents is a player array
        # History is the list correlated with opponents with w or l
        self.tournaments.append(tournament)
        for i in range(len(opponents)):
            self.sets_played += 1
            if history[i] == "w":
                self.melee_lvl += (10 * ((51 - opponents[i].rank) / 50))
            elif history[i] == "l":
                self.melee_lvl -= (5 * ((opponents[i].rank) /50))
            else:
                raise ValueError('NotWOrL')

def sortAndPrintPlayers(players):
    players.sort(reverse=True)
    for i in range(len(players)):
        if players[i].sets_played != 0:
            print(players[i].tag + " - EAR-M: " + "{:.5}".format(str(players[i].melee_lvl)))

def printPlayers(players):
    for i in range(len(players)):
        if players[i].sets_played != 0:
            print(players[i].tag + " | 2019 Rank: " + (str(players[i].rank)) + " | EAR-M: " + "{:.5}".format(str(players[i].melee_lvl)))

def printTournaments(player):
    tournamentString = player.tag + ": "
    for i in range(len(player.tournaments)):
        tournamentString += (player.tournaments[i] + ", ")
    print(tournamentString)

# GIANT LIST OF PLAYERS BEAR-MW
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
Plus50 = Player("Player With Above 50 Losses", 51)
# GIANT LIST OF PLAYERS DONE

player_list = [Hungrybox, Leffen, Mango, Axe, Wizzrobe, Zain, aMSa, Plup, iBDW, Mew2King, S2J, Fiction, SFAT, Moky, n0ne, Trif, Captain_Faceroll, Swedish_Delight, Hax, Lucky, Ginger, Spark, ChuDat, PewPewU, ARMY, lloD, AbsentPage, Bananas, KJH, Shroomed, Westballz, Medz, MikeHaze, Professor_Pro, TwoSaint, Gahtzu, Albert, Spud, FatGoku, Rishi, Bimbo, Setchi, Magi, Morsecode, JakenShaken, HugS, Stango, Zamu, Drephen, Michael]

def main():
    # Hungrybox
    Hungrybox1O = [Spud, Captain_Faceroll, PewPewU, Zain, Fiction, Hax, Mango, Zain]
    Hungrybox1R = ["w", "w", "w", "l", "w", "w", "w", "l"]
    Hungrybox2O = [Hax, aMSa, Mango, Fiction, Plup, n0ne, Mango, Plup, Plup, Plup]
    Hungrybox2R = ["w", "w", "w", "w", "w", "w", "w", "w", "l", "w"]
    Hungrybox.lvl_calculator("Genesis 7", Hungrybox1O, Hungrybox1R)
    Hungrybox.lvl_calculator("Smash Summit 9", Hungrybox2O, Hungrybox2R)

    # Leffen
    Leffen1O = [Professor_Pro, Professor_Pro]
    Leffen1R = ["w", "w"]
    Leffen2O = [MikeHaze, Hax, Fiction, Mango, Hax]
    Leffen2R = ["w", "w", "w", "l", "l"]
    Leffen3O = [Spark, Wizzrobe, Axe, n0ne, Zain, Mango, iBDW]
    Leffen3R = ["w", "w", "w", "w", "l", "l", "l"]
    Leffen.lvl_calculator("Valhalla III", Leffen1O, Leffen1R)
    Leffen.lvl_calculator("Genesis 7", Leffen2O, Leffen2R)
    Leffen.lvl_calculator("Smash Summit 9", Leffen3O, Leffen3R)

    # Mango
    Mango1O = [Trif, aMSa, Leffen, Zain, Hungrybox]
    Mango1R = ["w", "w", "w", "w", "l", "l"]
    Mango2O = [Shroomed, Fiction, Hungrybox, aMSa, Hax, Plup, Leffen, Hungrybox, Axe, Zain, Plup]
    Mango2R = ["w", "w", "l", "w", "w", "l", "w", "l", "w", "w", "l"]
    Mango.lvl_calculator("Genesis 7", Mango1O, Mango1R)
    Mango.lvl_calculator("Smash Summit 9", Mango2O, Mango2R)

    # Axe
    Axe1O = [Plus50, Spark, Spark]
    Axe1R = ["l", "w", "w"]
    Axe2O = [Plus50, Plup]
    Axe2R = ["l", "l"]
    Axe3O = [Zain, Leffen, Spark, Wizzrobe, Plup, aMSa, Fiction, Mango]
    Axe3R = ["w", "l", "w", "w", "l",  "w", "w", "l"]
    Axe.lvl_calculator("Settle It!", Axe1O, Axe1R)
    Axe.lvl_calculator("Genesis 7", Axe2O, Axe2R)
    Axe.lvl_calculator("Smash Summit 9", Axe3O, Axe3R)

    # Wizzrobe
    Wizzrobe1O = [Plus50, Medz, Spark, Captain_Faceroll]
    Wizzrobe1R = ["l", "w", "w", "l"]
    Wizzrobe2O = [Leffen, Wizzrobe, iBDW, Axe, Fiction]
    Wizzrobe2R = ["l", "l", "l", "l", "l"]
    Wizzrobe.lvl_calculator("Genesis 7", Wizzrobe1O, Wizzrobe1R)
    Wizzrobe.lvl_calculator("Smash Summit 9", Wizzrobe2O, Wizzrobe2R)

    # Zain
    Zain1O = [JakenShaken, Shroomed, Hungrybox, Mango, Hungrybox]
    Zain1R = ["w", "w", "w", "w", "w"]
    Zain2O = [n0ne, Axe, Wizzrobe, iBDW, Leffen, Fiction, Plup, iBDW, Mango]
    Zain2R = ["w", "l", "w", "w", "w", "w", "l", "w", "l"]
    Zain.lvl_calculator("Genesis 7", Zain1O, Zain1R)
    Zain.lvl_calculator("Smash Summit 9", Zain2O, Zain2R)

    # aMSa
    aMSa1O = [Mew2King, Mango, n0ne]
    aMSa1R = ["w", "l", "l"]
    aMSa2O = [Hungrybox, Mango, Fiction, Shroomed, Axe]
    aMSa2R = ["l", "l", "l", "w", "l"]
    aMSa.lvl_calculator("Genesis 7", aMSa1O, aMSa1R)
    aMSa.lvl_calculator("Smash Summit 9", aMSa2O, aMSa2R)

    # Plup
    Plup1O = [Plus50]
    Plup1R = ["l"]
    Plup2O = [PewPewU, Axe, ARMY]
    Plup2R = ["l", "w", "l"]
    Plup3O = [Hax, Shroomed, Hungrybox, Mango, Axe, Zain, Hungrybox, Mango, Hungrybox, Hungrybox]
    Plup3R = ["l", "w", "l", "w", "w", "w", "l", "w", "w", "l"]
    Plup.lvl_calculator("CFL Smackdown #262", Plup1O, Plup1R)
    Plup.lvl_calculator("Genesis 7", Plup2O, Plup2R)
    Plup.lvl_calculator("Smash Summit 9", Plup3O, Plup3R)


    # iBDW
    iBDW1O = [HugS, Fiction, Fiction]
    iBDW1R = ["w", "l", "l"]
    iBDW2O = [ARMY, PewPewU, Captain_Faceroll]
    iBDW2R = ["w", "l", "l"]
    iBDW3O = [Trif, ARMY, Albert, Lucky, Professor_Pro, Fiction, S2J, Fiction]
    iBDW3R = ["w", "l", "w", "w", "w", "l", "w", "l"]
    iBDW4O = [n0ne, Zain, Wizzrobe, Spark, Leffen, Hax, Zain]
    iBDW4R = ["l", "l", "w", "w", "w", "w", "l"]
    iBDW.lvl_calculator("Verdugo West #94", iBDW1O, iBDW1R)
    iBDW.lvl_calculator("Genesis 7", iBDW2O, iBDW2R)
    iBDW.lvl_calculator("Saving Mr. Lombardi 2", iBDW3O, iBDW3R)
    iBDW.lvl_calculator("Smash Summit 9", iBDW4O, iBDW4R)

    # Mew2King
    Mew2King1O = [Professor_Pro, aMSa, ARMY, Swedish_Delight]
    Mew2King1R = ["w", "l", "w", "l"]
    Mew2King.lvl_calculator("Genesis 7", Mew2King1O, Mew2King1R)


    # Main part
    #printPlayers(player_list)
    sortAndPrintPlayers(player_list)

    # TOP 10 MPGR - EAR-M Values for 2020
    # Hungrybox - EAR-M: 111.7
    # Mango - EAR-M: 88.10
    # Zain - EAR-M: 84.30
    # Leffen - EAR-M: 52.2
    # iBDW - EAR-M: 50.7
    # Plup - EAR-M: 48.99
    # Axe - EAR-M: 39.90
    # aMSa - EAR-M: 8.6
    # Mew2King - EAR-M: 6.100
    # Wizzrobe - EAR-M: -0.40


if __name__ == "__main__":
    main()
