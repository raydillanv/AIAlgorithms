"""
Week 3 - The MIU System, part 2 worth 5% of your overall grade.



When you have tested your extend_path(s) function, test and submit it here.  It is worth 1% of your overall grade.
Deadline is 9th February at 22:30.
You should use your next_states(s) function to create a function called extend_path(p) which extends an existing path.
A path is a list of states, starting with the start state and progressing towards the goal state in single steps.
You should return a list of extended paths.  You can assume that a working version of next_states is already present here.

1. extend_path(["MI","MII"]) = [["MI","MII","MIIU"], ["MI","MII","MIIII"]]

Remember, you should test it carefully before submitting it.

"""

possibleStrings = []


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
    # print(possibleStrings)
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


# extend_path(p)

def extend_path(p):
    # print("You called extend_path with: ")
    # print(p)
    result_paths = []
    # where s is the intermediate state
    s = p[-1]
    intermediate_step = next_states(s)

    for i in intermediate_step:
        multi_path = p.copy()
        multi_path.append(i)
        result_paths.append(multi_path)

    # print(result_paths)
    return result_paths

"""
The agenda is a queue of paths, initially set to [["MI"]]. At each iteration, set currentpath to
be the first item at the start of the queue and remove it from the queue. If the last string of
currentpath is equal to goalState, then print out the length of the path, the number of times
extend_path(p) got called and the maximum size of the agenda, and return the currentpath
list (see examples below). 

- Otherwise, call extend_path(currentpath), add the new paths to end of the agenda and
repeat.
- You’ll also need add a limit to the number of times extend_path(p) can be called (in case the
string that you’re searching for turns out to be impossible to derive from "MI"). In such
cases, return [0,0,0] as the result. The limit can be quite large if needed, say, 5000.
- For submission, you can assume that working extend_path and next_states functions are
present.
- When submitting, you should not have any print values, but can return the values you need:
return currentPath, extendCount, agendaMaxLen

"""
agenda = [["MI"]]

def breadth_first_search(goalString):
    global agenda, agendaMaxLen, extendCount, currentPath
    agenda = [["MI"]]
    currentPath = []
    agendaMaxLen = 0
    extendCount = 0

    #extend_path(goalString)
    while goalString not in agenda:
        extendCount +=1
        if extendCount == 5000:
            return [0,0,0]
        if agendaMaxLen < len(agenda):
            agendaMaxLen = len(agenda)
        currentPath = agenda[0]
        agenda.pop(0)




        #print(str(currentPath[-1]))
        if str(currentPath[-1]) == goalString:
            # print("The current path is: " + str(currentPath))
            # print("Number of expansions: " + str(extendCount))
            # print("The agenda's max length was: " + str(agendaMaxLen))
            # print("Found goal.")
            return currentPath, extendCount, agendaMaxLen
        # else:
        # print("no goal")

        #agenda = agenda + extend_path(goalString)

        otherPaths = extend_path(currentPath)
        agenda = agenda + otherPaths
        # print(agenda)

"""
Depth-First Search with iterative deepening limited
"""
notSolution = True
def depthlimited_dfs(goalString, limit):
    global agenda, agendaMaxLen, extendCount, currentPath, notSolution
    agenda = [["MI"]]
    currentPath = []
    agendaMaxLen = 0
    extendCount = 0


    #extend_path(goalString)
    while goalString not in agenda:

        extendCount +=1
        # print(extendCount)
        #if extendCount == limit:
        #return currentPath, extendCount, agendaMaxLen
        if extendCount == 5000:
            return [0,0,0]
            # print("Value not found exited at 5000 attempts.")
        if agendaMaxLen < len(agenda):
            agendaMaxLen = len(agenda)
        currentPath = agenda[0]
        agenda.pop(0)

        #print(str(currentPath[-1]))
        if str(currentPath[-1]) == goalString :
            if str(currentPath[-1]) == goalString:
                notSolution = False
                print("Found goal: " + str(currentPath[-1]))
                print("The current path is: " + str(currentPath))
                print("Number of expansions: " + str(extendCount))
                print("The agenda's max length was: " + str(agendaMaxLen))
                return currentPath, extendCount, agendaMaxLen

        # else:
        # print("no goal")
        if extendCount == limit:
            print("Limit reached: Break.")
            return
            break


        otherPaths = extend_path(currentPath)
        agenda = otherPaths + agenda

        # if extendCount == limit:
        #     pass
        # else:
        #     otherPaths = extend_path(currentPath)
        #     agenda = otherPaths + agenda

        # agenda.index(0, otherPaths)
"""
Iterative Deepening
"""

limitGlobal = 2

def dfs_iter(goalString):
    global limitGlobal, notSolution
    limitGlobal = 2
    notSolution = True
    while (notSolution):
        limitGlobal+= 1
        depthlimited_dfs(goalString, limitGlobal)
    print("dfs_iter has finished")






if __name__ == "__main__":
    print("Main method is not commented out. If you are seeing text, comment it out before submission.\n")
    #depthlimited_dfs(goalString, limit)
    # depthlimited_dfs("MIUIUIUIU",4)

    dfs_iter("MIUIUIUIU")
    # dfs_iter("MIU")
    # dfs_iter("MUIU")
    # dfs_iter("MUIIU")


    # extend_path(['MIU', 'MII'])
    # extend_path(['MI'])
    # next_states("MI")
    # next_states("MII")
    # breadth_first_search("MUIU")
    # breadth_first_search("MUIU")
    #breadth_first_search("MUIIU")
    #breadth_first_search("MIUIUIUIU")
