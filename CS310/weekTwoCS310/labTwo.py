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
    #print(possibleStrings)
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



if __name__ == "__main__":
    next_states("MI")
    next_states("MIU")
    next_states("MUI")
    next_states("MIIII")
    next_states("MUUII")
    next_states("MUUUI")

