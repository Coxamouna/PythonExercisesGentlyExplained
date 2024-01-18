# constant variable to store the winning states [player one's POV],
# as the first element being player one's play and the second being
# player two's play:

VALID_HANDS = ['rock', 'paper', 'scissors']
WIN_STATES = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]
# ('rock', 'scissors') translates to rock beats scissors

def rpsWinner(player1, player2):
    # checking if the moves played are valid - no Spook, Lizard, etc. moves allowed:
    if (player1 not in VALID_HANDS) or (player2 not in VALID_HANDS):
        return 'invalid play'
    # if they throw the same hand, game ends inna tie:
    if (player1 == player2):
        return 'tie'
    # create the game variable to store the hands played as pairs,
    # and if the pair is in the winning state list, player one
    # wins, else player two wins:
    game = (player1, player2)
    if game in WIN_STATES:
        return 'player one'
    else:
        return 'player two'
   
assert rpsWinner('lizard', 'lizard') == 'invalid play'
assert rpsWinner('spook', 'rock') == 'invalid play'
assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('lizard', 'fireball') == 'invalid play'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie' 