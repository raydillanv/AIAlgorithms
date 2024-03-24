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

    print(result_paths)
    return result_paths


def breadth_first_search(goalString):
    print(goalString)


if __name__ == "__main__":
    print("Main method is not commented out.")
    # extend_path(['MIU', 'MII'])
    extend_path(['MI', 'MII'])
    # next_states("MI")
    # next_states("MII")
