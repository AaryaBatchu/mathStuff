# Bayes' Experiment Monte Carlo Simulatio

# suppose you have a ball who's coordinates are determined by dice
# (in this case from (0, 0) to (5, 5) because coding is 0-indexed)

# then you make a random roll of the dice, and are told whether the ball is up/down, left/right of the ball (or right on top of it)
# then you can guess the ball's location

# the goal of this program is to find the mean number of guesses (x̄) and the standard deviation (σ)

# why? who cares

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# obviously we need some randomness
import random

n = 1000000  # the number of times we run the experiment
total_count = []  # list to keep track of all the guesses from each run
total = 0  # the total count of all the guesses

for i in range(n):
    ball = [random.randrange(6), random.randrange(6)]  # pick a random position for the ball from [0, 0] to [5, 5]

    
    possibilities = [[i, j] for i in range(6) for j in range(6)]  # all the posibilities there could be 
    guesses = 0  # reset the counter for how long it will take to guess the ball's position

    roll = None
    guess = None
    while guess != ball and roll != ball:
        guesses += 1  # add to the amount of guesses so far

        roll = [random.randrange(6), random.randrange(6)]  # simulate random roll of the dice
        
        # literally just check if the roll is up/down or left/right of ball and eliminate all the other posibilities
        if roll[0] < ball[0]:
            for possibility in possibilities:
                if possibility[0] <= roll[0]:
                    possibilities.pop(possibilities.index(possibility))
        elif roll[0] > ball[0]:
            for possibility in possibilities:
                if possibility[0] >= roll[0]:
                    possibilities.pop(possibilities.index(possibility))
        elif roll[0] == ball[0]:
            for possibility in possibilities:
                if possibility[0] != roll[0]:
                    possibilities.pop(possibilities.index(possibility))
        if roll[1] < ball[1]:
            for possibility in possibilities:
                if possibility[1] <= roll[1]:
                    possibilities.pop(possibilities.index(possibility))
        elif roll[1] > ball[1]:
            for possibility in possibilities:
                if possibility[1] >= roll[1]:
                    possibilities.pop(possibilities.index(possibility))
        elif roll[1] == ball[1]:
            for possibility in possibilities:
                if possibility[1] != roll[1]:
                    possibilities.pop(possibilities.index(possibility))

        guess = random.choice(possibilities)  # make a random guess from the possibilities
    

    total_count.append(guesses)  # add the num of guesses to the total_count list
    total += guesses  # add to the total 

mean = float(total / n)  # def of mean = (total sum) / (number of elements)

# simply finding the variance (the sum of the distance from the mean ^ 2)
variance = 0.0
for count in total_count:
    variance += (mean - count) ** 2
variance /= times

print("x̄: %f\nσ: %f" % (mean, (variance ** 0.5)))  # x̄ = mean, σ = standard deviation = √(variance)
