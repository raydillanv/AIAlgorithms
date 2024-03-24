"""
Tuesday Janaury 23rd,

Lab 2

Rule1. If your string ends in an I, you can add a U on the end: xI -> xIU
Rules2. If the string starts with M, you can double what comes after the M:
Mx-> Mxx
Rule3. If you have III in a stringm you can replace it with a U:
xIIIy -> xUy
Rule4. If you have UU in a string, you can delete it altogether: xUUy -> xy

It turns out that transforming MI into MU is impossible, but it is possible to derive lots of other strings

"""

possibleStrings = []

def next_states(s):
    possibleStrings.clear()
    if s.endswith("I"):
        #print("Ends in I")
        #s = s + "U"
        if s not in possibleStrings:
            possibleStrings.append(s + "U")

        #print(s)
    if s.startswith("M"):
        #print("Starts with M")
        #s = s+s[1:]
        if s not in possibleStrings:
            possibleStrings.append(s+s[1:])

        #print(s)
    if "III" in s:
        #print("III is in " + s)
        #s = s.replace("III","U")
        #possibleStrings.append(s.replace("III","U"))
        applyIII(s)

        #print(s)
    if "UU" in s:
        #print("UU is in " + s)
        #s = s.replace("UU", "")
        #possibleStrings.append(s.replace("UU", ""))
        applyUU(s)

        #print(s)
    #print(possibleStrings)
    return possibleStrings


def applyIII(e):
    # Find the index of the first occurrence of "III"
    index = e.find("III")

    # Check if "III" is present in the string
    if index != -1:
        #print(f"Original: {e}")
        #print("Possible applications of the rule:")

        while index != -1:
            # Replace "III" with "U" and print the modified string
            new_e = e[:index] + 'U' + e[index + 3:]
            #print(new_e)

            if new_e not in possibleStrings:
                possibleStrings.append(new_e)

            # Find the index of the next occurrence of "III"
            index = e.find("III", index + 1)

    #else:
        #print("No matches found.")

def applyUU(d):
    # Find the index of the first occurrence of "UU"
    index = d.find("UU")

    # Check if "UU" is present in the string
    if index != -1:
        #print(f"Original: {d}")
        #print("Possible applications of the rule:")

        while index != -1:
            # Replace "UU" with "" and print the modified string
            new_d = d[:index] + '' + d[index + 2:]
            #print(new_d)
            if new_d not in possibleStrings:
                possibleStrings.append(new_d)

            # Find the index of the next occurrence of "UU"
            index = d.find("UU", index + 1)

    #else:
        #print("No matches found.")


if __name__ == "__main__":
    next_states("MI")
    #next_states("MIU")
    #next_states("MUI")
    #next_states("MIIII")
    #next_states("MUUII")
    #next_states("MUUUI")