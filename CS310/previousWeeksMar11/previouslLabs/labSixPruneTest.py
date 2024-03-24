memoization_cache = {}

def successors_fixed(state):
    (piles, player) = state
    piles = tuple(piles)  # Ensure piles are a tuple
    succ = []
    for i, pile in enumerate(piles):
        for remove in range(1, 4):
            if pile >= remove:
                new_piles = list(piles)
                new_piles[i] -= remove
                if not new_piles[i]:
                    del new_piles[i]
                new_state = (tuple(new_piles), 3-player)
                succ.append(new_state)
    return succ

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
    state = (tuple(state[0]), state[1])  # Ensure the state conforms to hashable types
    alpha = float('-inf')
    beta = float('inf')
    if state[1] == 1:
        v, path = max_value_fixed(state, alpha, beta)
    else:
        v, path = min_value_fixed(state, alpha, beta)
    return str(v)

import time

def test_timing(state):
    # Start a timer
    start = time.time()
    # Call minimax function
    value = minimax_prune(state)
    end = time.time()
    #calculate and return
    duration = end-start
    #print('Time taken:', duration)
    return duration, value

output = (test_timing(([5,2,2,3],1)))
print("Time taken", output[0])
print("Value returned", output[1])
