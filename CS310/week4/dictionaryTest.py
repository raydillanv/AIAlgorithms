possibleStrings = []
agenda = []
globalMaxAgenda = 0

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

def breadth_first_dictionary_search(goalString):
    global agenda, globalMaxAgenda  # Accessing the global agenda
    agenda = [("MI", None)]  # tuple (state, ancestor)
    ancestors = {}  # dictionary to keep track of ancestors
    visited = set()  # Set to keep track of visited states
    expansions = 0
    max_agenda_size = 0

    while agenda:
        state, ancestor = agenda.pop(0)
        if state in visited:
            continue
        visited.add(state)
        expansions += 1

        if state == goalString:
            path = []
            while state: # Uses ancestors to trace back from goal to the initial state using path
                path.append(state)
                state = ancestors.get(state)
            return path[::-1], expansions, max(max_agenda_size, len(agenda)) # The path back

        for newState in next_states(state): # applies the next state found from the current state
            if newState not in visited:
                agenda.append((newState, state))
                ancestors[newState] = state

        max_agenda_size = max(max_agenda_size, len(agenda)) # agenda size

    return None, expansions, max_agenda_size

if __name__ == "__main__":
    result_path, expansions, max_agenda = breadth_first_dictionary_search("MIUUIUUII")
    print(f"Path: {result_path}, Expansions: {expansions}, Max Agenda: {max_agenda}")

    # result_path, expansions, max_agenda = breadth_first_dictionary_search("MUI")
    # print(f"Path: {result_path}, Expansions: {expansions}, Max Agenda: {max_agenda}")

