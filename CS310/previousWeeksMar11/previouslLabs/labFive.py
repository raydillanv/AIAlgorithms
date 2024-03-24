def successors(state):
    (piles, player) = state
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

def max_value(state):
    if state[0] == ():
        return 1, [state]
    v = float('-inf')
    path = []
    for s in successors(state):
        mv, p = min_value(s)
        if mv > v:
            v = mv
            path = p
            if v == 1:
                break
    return v, [state] + path


def min_value(state):
    if state[0] == ():
        return -1, [state]
    v = float('inf')
    path = []
    for s in successors(state):
        mv, p = max_value(s)
        if mv < v:
            v = mv
            path = p
            if v == -1:
                break
    return v, [state] + path


def minimax_value(state):
    if state[1] == 1:
        v, path = max_value(state)
    else:
        v, path = min_value(state)
    # return v, path
    return str(v)

#
# print(minimax_value(([4],1)))
# print(minimax_value(([2,3],1)))
# print(minimax_value(([9,9],1)))
# print(minimax_value(([5,5,5],1)))
# v = minimax_value(([2,3],1))
# print(v)

import time

def test_timing(state):
    # Start a timer
    start = time.time()
    # Call minimax function
    value = minimax_value(state)
    end = time.time()
    #calculate and return
    duration = end-start
    #print('Time taken:', duration)
    return duration, value

output = (test_timing(([8,8,8],1)))
print("Time taken", output[0])
print("Value returned", output[1])
