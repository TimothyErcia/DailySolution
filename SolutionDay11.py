"""
This problem was asked by Slack.
You are given an N by M matrix of 0s and 1s. Starting from the top left corner,
how many ways are there to reach the bottom right corner?
You can only move right and down.
0 represents an empty space while 1 represents a wall you cannot walk through.

example
[[0,0,1],
[0,0,1],
[1,0,0]]
Starting from [0][0] to [2][2]
moves = [Right, down, down, right]
"""

def reachBottom(items):
    moves = []
    position_X = 0
    position_Y = 0

    max_position = len(items) - 1

    try:
        while position_X is not max_position or position_Y is not max_position:
            if items[position_Y][position_X + 1] == 1:
                moves.append("Down")
                position_Y += 1
        
            elif items[position_Y][position_X + 1] == 0:
                moves.append("Right")
                position_X += 1
            
    except:
        while position_X is not max_position or position_Y is not max_position:
            if position_X == max_position:
                moves.append("Down")
                position_Y += 1

            elif position_Y == max_position:
                moves.append("Right")
                position_X += 1

    return moves

item2 = [[0,0,0],
        [0,1,0],
        [0,0,0]]

rb = reachBottom(item2)
print(rb)
