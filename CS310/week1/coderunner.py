# @author Dillan Victory 2024 Jan 19th
""" Write a function diag(x) that takes a string as input and outputs the string written in a
diagonal """
"""
P
 Y
  T
   H
    O
     N 
"""

def diag(x):
    #print(x)
    #d = [i for i in n]
    #print(d)
    count = 0
    #print(x[0])
    i = 0
    control = ""
    for c in x:
        #while(count!= x.len()):

        while(i!=count):
            control = control + " "
            i+=1
        print(control + x[count])
        count+=1





if __name__ == "__main__":
    diag("Python")