# Let's play! You have to return which player won! In case of a draw return Draw!.

player1, player2 = input("Rock, Paper or Scissors? player 1 then player 2 ").split()

# rock = 4
# paper = 5
# scissors = 8
# 4 < 5 < 8

# def rps(p1, p2):
#     beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
#     if beats[p1] == p2:
#         return "Player 1 won!"
#     if beats[p2] == p1:
#         return "Player 2 won!"
#     return "Draw!"

RPS = lambda P1, P2:'Draw' if len(P1) == len(P2) else 'Player 1 won!' if (P1 == 'scissors' and P2 != "rock") or (len(P1) > len(P2) and P1 != 'scissors') or (P1 == 'rock' and P2 == 'scissors') else 'Player 2 won!'

print(RPS(player1, player2))

# def rps(p1, p2):
#     hand = {'rock':0, 'paper':1, 'scissors':2}
#     results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
#     return results[hand[p1] - hand[p2]]

# this solution uses negative index which goes:
# a = [0, 1, 2]
# a[-2] = 1
# a[-1] = 2
# a[-3] = 0