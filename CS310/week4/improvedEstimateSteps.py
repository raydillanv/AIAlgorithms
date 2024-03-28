possibleStrings = []
agenda = []
globalMaxAgenda = 0
visited = {}  # Track visited states with their lowest cost

def estimate_steps(current, goal):
    # improved heuristic based on string length and character count differences
    length_diff = abs(len(current) - len(goal))
    char_diff = sum(abs(current.count(char) - goal.count(char)) for char in 'MIU')
    return max(length_diff, char_diff // 2)  # Division to avoid overestimation

def next_states(s):
    possibleStrings.clear()
    if s.endswith("I"):
        possibleStrings.append(s + "U")
    if s.startswith("M"):
        possibleStrings.append(s + s[1:])
    if "III" in s:
        applyIII(s)
    if "UU" in s:
        applyUU(s)
    return possibleStrings

def applyIII(e):
    index = e.find("III")
    while index != -1:
        new_e = e[:index] + 'U' + e[index + 3:]
        if new_e not in possibleStrings:
            possibleStrings.append(new_e)
        index = e.find("III", index + 1)

def applyUU(d):
    index = d.find("UU")
    while index != -1:
        new_d = d[:index] + d[index + 2:]
        if new_d not in possibleStrings:
            possibleStrings.append(new_d)
        index = d.find("UU", index + 1)

def extend_path(p):
    result_paths = []
    s = p[-1]
    intermediate_step = next_states(s)

    for i in intermediate_step:
        if i not in visited or visited[i] > len(p):
            multi_path = p.copy()
            multi_path.append(i)
            result_paths.append(multi_path)
            visited[i] = len(p)  # Update visited with the current path length
    return result_paths

def astar_search(goalString):
    global agenda, globalMaxAgenda
    agenda = [(["MI"], 0)]  # Path and initial cost
    extend_count = 0
    agenda_max_len = 0

    while agenda:
        current_path, current_cost = sorted(agenda, key=lambda x: x[1] + estimate_steps(x[0][-1], goalString))[0]
        agenda.remove((current_path, current_cost))

        if current_path[-1] == goalString:
            return current_path, extend_count, agenda_max_len

        new_paths = extend_path(current_path)
        for path in new_paths:
            agenda.append((path, current_cost + 1))

        agenda_max_len = max(agenda_max_len, len(agenda))
        extend_count += 1

        if len(agenda) > globalMaxAgenda:
            globalMaxAgenda = len(agenda)

    return [0, 0, 0]

if __name__ == "__main__":
    # Example usage of A* search
    result = astar_search("MUIIIIIIIIII")
    print("Path:", result[0], "Number of Expansions:", result[1], "Max Agenda Size:", globalMaxAgenda)
