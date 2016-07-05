"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################



def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 0.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1

    times = 0
    sum = 0
    flag = 0 #
    while times < num_rolls :
        temp = dice()
        if temp == 1:
            flag = 1
        sum += temp
        times += 1
    if flag == 1:
    	return 0
    else:    
    	return sum

    # END Question 1


def  is_primer(n): 
	if n == 0 or n == 1:
		return False
	now_test = 2
	while now_test <= n-1:
		if n % now_test == 0:
			return False
		now_test += 1
	return True
def next_primer(n):
	while True:
		n += 1
		if is_primer(n):
			return n




def maxer(a,b):
	if(a > b):
		return a
	else:
		return b

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    first = opponent_score % 10
    second = opponent_score // 10
    

    if num_rolls == 0:
    	temp_final = maxer(first,second) + 1
    else :
    	temp_final = roll_dice(num_rolls,dice) 

    if is_primer(temp_final):
    	temp_final = next_primer(temp_final)

    return temp_final

    # END Question 2


def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    if (score + opponent_score)%7 == 0:
    	return four_sided
    else:
    	return six_sided
    # END Question 3


def is_swap(score0, score1):
    """Returns whether the last two digits of SCORE0 and SCORE1 are reversed
    versions of each other, such as 19 and 91.
    """
    # BEGIN Question 4
    def getfirst(x):
    	a = x // 10
    	if a >= 10:
    		a = a % 10
    	return a
    def getsecond(x):
    	return x % 10

    return getsecond(score0) == getfirst(score1) and getfirst(score0) == getsecond(score1)

    # END Question 4


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player
###for reference
#def other(player):
#def is_swap(score0, score1):
#def take_turn(num_rolls, opponent_score, dice=six_sided):

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    "*** strategy1(score1,score0) ***"
    
    now_player = 0
    while True:

        if score0 >= goal or score1 >= goal:
            break
        
        dice_type = select_dice(score0,score1)
      
        if now_player == 0:
            tmp = take_turn( strategy0(score0,score1), score1, dice_type )
            score0 += tmp
            if tmp == 0:
            	score1 += strategy0(score0,score1)

            
        else :
            tmp = take_turn( strategy1(score1,score0), score0, dice_type )
            score1 += tmp
            if tmp == 0:
            	score0 += strategy1(score1,score0)
            
        if is_swap(score0, score1):
            score1 , score0 = score0 , score1
            

        now_player = other(now_player)

    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n

    return strategy


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    5.5

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 0.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 5.5.
    Note that the last example uses roll_dice so the hogtimus prime rule does
    not apply.
    """
    # BEGIN Question 6
    def f(*args):
        sum = 0
        k = 0
        while k < num_samples:
            sum += fn(*args)
            k += 1
        res = sum / num_samples
        return res
    return f    

    # END Question 6


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN Question 7
    maxer = -1
    index = -1
    k = 10
    while k > 0:
        if make_averaged(roll_dice)(k,dice) >= maxer:
            maxer = make_averaged(roll_dice)(k,dice)
            index = k
        k -= 1
    return index   
    # END Question 7


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def  m_(a,b):
    if a > b:
        return a
    else:
        return b

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 8
    "*** REPLACE THIS LINE ***"
    first_ = opponent_score // 10
    second_ = opponent_score % 10
    temp = m_(first_, second_) + 1
    if is_primer(temp):
        temp = next_primer(temp)
    if  temp >= margin:
        return 0
    else:
        return num_rolls
    # END Question 8


def swap_strategy(score, opponent_score, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 9
    "*** REPLACE THIS LINE ***"
   
    your_first = opponent_score // 10
    your_second = opponent_score % 10

    score = score + m_(your_second, your_first) + 1
    my_first = score // 10
    my_second = score % 10
    if my_second == your_first and my_first == your_second and score < opponent_score:
        return 0
    else:
        return num_rolls
    # END Question 9


def final_strategy(score, opponent_score):
    """

    We should combine these three strategries

    def swap_strategy(score, opponent_score, num_rolls):
    def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    def max_scoring_num_rolls(dice=six_sided, num_samples=1000):

    
    """
    if score < 5:
        return swap_strategy(score, opponent_score,2)
    if score < 140:
        return bacon_strategy(score, opponent_score,6,2)
    else:
        return 2

    # END Question 10


##########################
# Command Line Interface #
##########################


# Note: Functions in this section do not need to be changed. They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()

##############test######################
