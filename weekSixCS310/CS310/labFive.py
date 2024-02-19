agenda = []
globalMaxAgenda = 0
visited = {}  # Track visited states ...
# Above Variables From MUI Previous Improved Algorithm, maybe need some of them here too
def minimax_value(state):
    # return the minimax value of a state
    global agenda, globalMaxAgenda
    sam = state
    piles = sam[0]
    player = sam[-1]

    print("The state is: " + str(piles) + " and Player is: " + str(player))
    return sam

def makeMove(piles):
    
    moveMade = piles
    return moveMade

if __name__ == "__main__":
    # Example usage of minimax
    minimax_value(([3, 2], 1))

    minimax_value(([4], 1))
    # print(minimax_value(([4],1)))
    # Example Play: [([4], 1), ([1], 2), ([], 1)] 1

