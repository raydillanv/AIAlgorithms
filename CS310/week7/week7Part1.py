import random
import time
import math

def successors_fixed(state):
    (piles, player) = state
    piles = tuple(piles)  # Ensure piles are a tuple
    succ = []
    for i, pile in enumerate(piles):
        for remove in range(1, min(pile, 3) + 1):  # Adjust to ensure no more than 3 sticks are removed
            new_piles = list(piles)
            new_piles[i] -= remove
            if not new_piles[i]:
                del new_piles[i]
            new_state = (tuple(new_piles), 3-player)
            succ.append(new_state)
    return succ

memoization_cache = {}

def max_value_fixed(state, alpha, beta):
    if state in memoization_cache:
        return memoization_cache[state], []
    if state[0] == ():
        memoization_cache[state] = 1
        return 1, [state]
    v = float('-inf')
    path = []
    for s in successors_fixed(state):

        mv, p = min_value_fixed(s, alpha, beta)
        if mv > v:
            v = mv
            path = p
            if v >= beta:
                memoization_cache[state] = v
                return v, [state] + path
            alpha = max(alpha, v)
    memoization_cache[state] = v
    return v, [state] + path

def min_value_fixed(state, alpha, beta):

    if state in memoization_cache:
        return memoization_cache[state], []
    if state[0] == ():
        memoization_cache[state] = -1
        return -1, [state]
    v = float('inf')
    path = []
    for s in successors_fixed(state):
        mv, p = max_value_fixed(s, alpha, beta)
        if mv < v:
            v = mv
            path = p
            if v <= alpha:
                memoization_cache[state] = v
                return v, [state] + path
            beta = min(beta, v)
    memoization_cache[state] = v
    return v, [state] + path

def minimax_prune(state):
    global memoization_cache
    memoization_cache = {}
    state = (tuple(state[0]), state[1])
    alpha = float('-inf')
    beta = float('inf')
    if state[1] == 1:
        v, path = max_value_fixed(state, alpha, beta)
    else:
        v, path = min_value_fixed(state, alpha, beta)
    return v, None  # Adjusted to return a tuple

# AI player that chooses a move based on the pruned minimax algorithm
def AI_player_basic(state):
    best_value = float('inf')
    best_move = None
    for succ in successors_fixed(state):
        value, _ = minimax_prune(succ)  # Utilize minimax with pruning to evaluate the successor
        if value < best_value:
            best_value, best_move = value, succ
    return best_move


# Main function to run game
def Nim():
    initialState = []
    state = ()

    print("Let's play Nim")

    valid = False
    while not valid:
        try:
            numPiles = int(input("How many piles initially? "))
            maxSticks = int(input("Maximum number of sticks? "))

            for i in range(numPiles):
                sticks = random.randint(1, maxSticks)
                initialState.append(sticks)

            print("The initial state is " + str(initialState))
            print("Do you want to play a) first or b) second")
            turn = input("Enter a or b: ")
            if turn.lower() == "a":
                state = (initialState, 1)  # Human first
                valid = True
            elif turn.lower() == "b":
                state = (initialState, 2)  # AI first
                valid = True
            else:
                raise ValueError("Invalid Input")
        except ValueError as e:
            print(str(e) + ", please re-enter")

    return state

# User's turn to choose a move
def userturn(state):
    succ = successors_fixed(state)

    if len(succ) == 1 and succ[0][0] == ():
        print("You picked up the last stick!")
        return succ[0]

    print("Next move options:")
    for i, s in enumerate(succ):
        print(f"{i}. {s[0]}")
    moveIndex = int(input("Enter next move option number: "))
    print(f"You moved to state {succ[moveIndex][0]}")

    return succ[moveIndex]

# Function to start the game and alternate turns
def game_begin(state):
    game_state = state

    print("Game start", game_state)
    while game_state[0] != ():
        if game_state[1] == 1:
            game_state = userturn(game_state)
        else:
            game_state = AI_player_basic(game_state)
        print("State is", game_state)

    if game_state[1] == 1:
        print("You win!")
    else:
        print("Win for player 2")

# Start the game
if __name__ == "__main__":
    init_state = Nim()
    game_begin(init_state)
