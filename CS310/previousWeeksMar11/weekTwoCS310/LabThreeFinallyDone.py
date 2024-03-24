possibleStrings = []
agenda = []  # Making agenda a global variable
globalMaxAgenda = 0  # New global variable to store agenda length

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

def breadth_first_search(goalString):
    global agenda, globalMaxAgenda  # Accessing the global agenda
    agenda = [["MI"]]
    extend_count = 0
    agenda_max_len = 0

    while agenda:
        current_path = agenda.pop(0)
        if current_path[-1] == goalString:
            return current_path, extend_count, agenda_max_len

        new_paths = extend_path(current_path)
        agenda.extend(new_paths)
        agenda_max_len = max(agenda_max_len, len(agenda))
        extend_count += 1

        # Update global agenda length if needed
        if len(agenda) > globalMaxAgenda:
            globalMaxAgenda = len(agenda)

    return [0, 0, 0]

def depthlimited_dfs(goalString, limit):
    global agenda, globalMaxAgenda  # Accessing the global agenda
    agenda = [["MI"]]
    extend_count = 0
    agenda_max_len = 0

    while agenda:
        current_path = agenda.pop(0)
        if current_path[-1] == goalString:
            return current_path, extend_count, agenda_max_len

        if len(current_path) < limit:
            new_paths = extend_path(current_path)
            agenda = new_paths + agenda
            agenda_max_len = max(agenda_max_len, len(agenda))
            extend_count += 1

            # Update global agenda length if needed
            if len(agenda) > globalMaxAgenda:
                globalMaxAgenda = len(agenda)

    return [0, 0, 0]

def dfs_iter(goalString):
    limit = 2
    result = [0, 0, 0]

    while result[0] == 0:
        result = depthlimited_dfs(goalString, limit)
        limit += 1

    return result[0], result[1], globalMaxAgenda

# Example usage
currentPath, extendCount, agendaMaxLen = dfs_iter("MIUUIUUII")
print(currentPath)
print(extendCount)
print(agendaMaxLen)
