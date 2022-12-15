

import random

import sys

n = 12

#I want my function to accept both the sequences themselves and their lengths in order to scan both sequences
# for subsequences and so there is a recurrence relation/termination condition for the function
def myLCS_Re(DNA1, DNA2, lengthDNA1, lengthDNA2):
    # Termination condition
    if lengthDNA1 == 0:
        score = 0
        return score
    if lengthDNA2 == 0:
        score = 0
        return score
    # Recurrence relation
    elif DNA1[lengthDNA1 - 1] == DNA2[lengthDNA2 - 1]:
        score = 1 + myLCS_Re(DNA1, DNA2, lengthDNA1 - 1, lengthDNA2 - 1)
        return score
    # Recurrence relation
    elif DNA1[lengthDNA1 - 1] != DNA2[lengthDNA2 - 1]:
        score = max(myLCS_Re(DNA1, DNA2, lengthDNA1, lengthDNA2 - 1), myLCS_Re(DNA1, DNA2, lengthDNA1 - 1, lengthDNA2))
        return score
    print(DNA1, DNA2)
    print("LCS has length", score)

if len(sys.argv) == 1:
    DNA = ['A', 'C', 'G', 'T']
    random_seq_list = []
    DNA1 = ['A', 'C', 'G', 'T']
    random_seq_list1 = []
    for i in range(n):
        random_seq_list.append(random.choice(DNA))
    for i in range(n):
        random_seq_list1.append(random.choice(DNA1))
    random_seq = ''.join(random_seq_list)
    random_seq1 = ''.join(random_seq_list1)
    print(random_seq, random_seq1)
    print("LCS has length", myLCS_Re(random_seq, random_seq1, n, n))
elif len(sys.argv) == 2:
    n = int(sys.argv[1])
    DNA = ['A', 'C', 'G', 'T']
    random_seq_list = []
    DNA1 = ['A', 'C', 'G', 'T']
    random_seq_list1 = []
    for i in range(n):
        random_seq_list.append(random.choice(DNA))
    for i in range(n):
        random_seq_list1.append(random.choice(DNA1))
    random_seq = ''.join(random_seq_list)
    random_seq1 = ''.join(random_seq_list1)
    print(random_seq, random_seq1)
    print("LCS has length", myLCS_Re(random_seq, random_seq1, n, n))
elif len(sys.argv) == 3:
    n = int(len(sys.argv[1]))
    random_seq_list = []
    random_seq_list1 = []
    for i in sys.argv[1]:
        random_seq_list.append(i)
    for i in sys.argv[2]:
        random_seq_list1.append(i)
    random_seq = ''.join(random_seq_list)
    random_seq1 = ''.join(random_seq_list1)
    print(random_seq, random_seq1)
    print("LCS has length", myLCS_Re(random_seq, random_seq1, n, n))
