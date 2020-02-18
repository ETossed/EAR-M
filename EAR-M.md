# NEEDS TO BE UPDATED AS OF FEBRUARY 18TH

## Melee ELO Python Program (Super-Basic) Pseudocode / Overview

### This is a static model, rather than a more intuitive dynamic model based off of updated ELO and rank

* Create a class: Player(string tag, int sets_played, float elo_score)

* elo_score is calculated by each non-local win against top 100 players and ALL non-local losses
    * elo_score = [10 * ((51 - opposite player rank) / 50)] - [5 * ((opposite player rank) / 50)]
    * elo_score example: hungrybox (0 elo, rank 1) beats axe (0 elo, rank 4)
        * hungrybox.elo_score =+ (10 * (47/50)) -> hungrybox.elo_score = 9.4
        * axe.elo_score -= (5 * (1/50)) -> axe.elo_score = -.14

* sets_played is just kept track of for implementing a dynamic model and to eventually figure out an algorithm for not punishing attendance, which I think the model should do, but just incase it doesn't it's being kept track of

* elo_score data: run some kind of loop through smash.gg's API using all valid non-local tournaments with top 50 players in attendance
