import random
import time
import math

def successors_fixed(state):
    (piles, player) = state
    piles = tuple(piles)
    succ = []
    L = 0
    for i, pile in enumerate(piles):
        for remove in range(1, min(pile, 3) + 1):  # Adjust to ensure no more than 3 sticks are removed
            new_piles = list(piles)
            new_piles[i] -= remove
            if not new_piles[i]:
                del new_piles[i]
            new_state = (tuple(new_piles), 3-player)
            succ.append(new_state)
    return succ

def is_terminal(state):
    (piles, player) = state
    return len(piles) == 0  # Terminal if no sticks left

def evaluate(state):
    (piles, player) = state
    if len(piles) == 0:  # Current player has no move (loses)
        return -1
    else:
        return 1  # Non-terminal or winning state

def rollout(state):
    while not is_terminal(state):
        moves = successors_fixed(state)
        state = random.choice(moves)  # Randomly select successor
    return evaluate(state)

def AI_player_rollout(state):
    best_move = None
    best_score = float('-inf')
    num_rollouts = 100  # Number of rollouts to perform for each possible move

    for move in successors_fixed(state):
        total_score = 0
        for _ in range(num_rollouts):
            score = rollout(move)
            total_score += score
        average_score = total_score / num_rollouts

        if average_score > best_score:
            best_score = average_score
            best_move = move

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
            game_state = AI_player_rollout(game_state)
        print("State is", game_state)

    if game_state[1] == 1:
        print("You win!")
    else:
        print("Win for player 2")

# Start the game
if __name__ == "__main__":
    init_state = Nim()
    game_begin(init_state)
