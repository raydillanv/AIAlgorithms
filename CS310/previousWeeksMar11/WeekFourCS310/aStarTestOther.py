possibleStrings = []
agenda = []
globalMaxAgenda = 0

def estimate_steps(current, goal):
    # Simple heuristic function as a starting point
    return 0 if current == goal else 1

def next_states(s):
    possibleStrings.clear()
    if s.endswith("I"):
        if s not in possibleStrings:
            possibleStrings.append(s + "U")
    if s.startswith("M"):
        if s not in possibleStrings:
            possibleStrings.append(s + s[1:])
    if "III" in s:
        applyIII(s)
    if "UU" in s:
        applyUU(s)
    return possibleStrings

def applyIII(e):
    index = e.find("III")
    if index != -1:
        while index != -1:
            new_e = e[:index] + 'U' + e[index + 3:]
            if new_e not in possibleStrings:
                possibleStrings.append(new_e)
            index = e.find("III", index + 1)

def applyUU(d):
    index = d.find("UU")
    if index != -1:
        while index != -1:
            new_d = d[:index] + '' + d[index + 2:]
            if new_d not in possibleStrings:
                possibleStrings.append(new_d)
            index = d.find("UU", index + 1)

def extend_path(p):
    result_paths = []
    s = p[-1]
    intermediate_step = next_states(s)

    for i in intermediate_step:
        multi_path = p.copy()
        multi_path.append(i)
        result_paths.append(multi_path)

    return result_paths

def astar_search(goalString):
    global agenda, globalMaxAgenda
    agenda = [(["MI"], 0)]  # Path and initial cost
    extend_count = 0
    agenda_max_len = 0

    while agenda:
        # sorts agenda based on total cost of actual path cost + estimated path cost
        current_path, current_cost = sorted(agenda, key=lambda x: x[1] + estimate_steps(x[0][-1], goalString))[0]


        # removes the next for expansion
        agenda.remove((current_path, current_cost))
        # Goal Check
        if current_path[-1] == goalString:
            return current_path, extend_count, agenda_max_len

        # Get our new paths and costs
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
    # result = astar_search("MIUUIUUII")
    result = astar_search("MIUUIUUII")
    print("Path:", result[0], "Number of Expansions:", result[1], "Max Agenda Size:", globalMaxAgenda)
