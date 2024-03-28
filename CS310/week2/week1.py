# Collatz Sequences
""" think of any positive integer n, if n is even, divide it by 2, otherwise multiply it by 3 and add 1 to it,
keep going until you get to 1, at which point stop"""

""" Part 1"""


def collatz(n):
    sequence = []
    # print("こんにちは、世界!")
    counter = 0
    # if(n % 2) == 0: print("Input is even")
    while (counter != n):
        sequence.append(n)
        if (n == 1):
            # print(sequence)
            size = len(sequence)
            return size
            counter = n
        elif (n % 2) == 0:
            n = n // 2
            # counter+=1
        else:
            n = n * 3 + 1
            # counter+=1


""" Part 2"""


def biggest_seq(end):
    count = 1
    # topSequence = []
    topSequence = {}
    seqN = 0
    seqL = 0

    while (count <= end):
        # key = number tested, value = length of associated sequence
        topSequence.update({count: collatz(count)})
        # a dictionary would work better than a list, no wonder they taught it...
        # topSequence.append(collatz(count))

        count += 1

    # print(topSequence)
    # print(len(topSequence))
    # highest = max(topSequence, key= lambda x: topSequence[x])
    highest = max(zip(topSequence.values(), topSequence.keys()))
    # print(highest)

    # return seqL, seqN

    seqL, seqN = highest
    # print(seqL)
    # print(seqN)
    return seqL, seqN


""" Part 3"""
""" Given a string, return true f the string contains 3 A's in a row and False otherwise (non case sensitive)"""

def has_aaa(s):
    s = (s.strip().lower())
    if "aaa" in s:
        return True
    else:
        return False

""" Part 4 """
""" we have high value flowers, low value flowers, and greenery (the decorative
leaves and accessories. Given a budget, we want to spend our entire budget to create a bunch of
flowers. takes integer for number of high,
low and greenery items, and a budget, and returns a list of the flowers used to make the bunch. """

""" RULES: """
empty = []
def make_bunch(high, low, green, budget):
    h = 0
    l = 0
    g = 0
    bunch = [h,l, g]
    def buy_high():
        nonlocal budget, h, high

        if h == high:
            #print("There are no more high value flowers to buy.")
            return
        if h == 4:
            #print("4 is the max amount of high value flowers which can be used in a bunch.")
            return
        budget = budget - 4
        h+=1

    def buy_green():
        nonlocal budget, g, green

        if g < 4:
            g = 4
            budget = budget - 2
            return

        if g == green:
            #print("There is no more greenery to buy.")
            return
        if budget >= 0.5:
            budget = budget - 0.5
            g+=1

        #print(str(budget))

    def buy_low():
        nonlocal l, budget, low

        if l == low:
            #print("There are no more low value flowers to buy.")
            return
        else:
            budget = budget - 2
            l+=1

    def buy():
        nonlocal budget, h, l, g, green

        if green < 4:
            #print("Bunches needs at least 4 greenery")
            return []


        while budget != 0:
            #print("buying")
            buy_green()
            while budget >=4:
                buy_high()
                if h == high:
                    break
                if h == 4:
                    break

            while budget >= 2:
                buy_low()
                if l == low:
                    break
            while budget >= 0.5:
                buy_green()
                if g == green:
                    break





            if budget <= 0:
                #print("break point")
                break
            elif h == 4 and l == low and g == green:
                return []


     #print(str(budget))

    buy()

    #print("You have " + str(h) + " high value flowers.\nYou have " + str(l) + " low value flowers.\nYou have "+ str(g) + " greenery.\nYou have "+ str(budget) + " left to use.")

    if budget == 0:
        #print("budget is now 0")
        empty = []
        empty.append(h)
        empty.append(l)
        empty.append(g)
        return empty

    if budget != 0:
        return []


if __name__ == "__main__":
    # collatz(12)
    # biggest_seq(20)
    #has_aaa("teststrAAAng ")
    make_bunch(50, 1, 6, 100)
