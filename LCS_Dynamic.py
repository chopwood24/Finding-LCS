
import random

import sys

n = 12

# Create two random sequences of length 12 if user enters no additional argument
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
    # Create table of zeros with dimension (1+|random_seq|)-by-(1+|random_seq1|)
    opt = []
    row = []
    for i in range(len(random_seq) + 1):
        row.append(0)
    for j in range(len(random_seq1) + 1):
        opt.append(row)
    for base1 in range(len(random_seq) + 1):
        for base2 in range(len(random_seq1) + 1):
            # I want the values of the table at all positions where either random_seq[0] or random_seq1[0]
            # to equal zero.
            if base1 == 0:
                opt[base1][base2] = 0
            if base2 == 0:
                opt[base1][base2] = 0
            # If base1 in random_seq is equal to base2 in random_seq1 at the same index within their respective
            # sequences, I want the value of the table at position opt[base1][base2] to equal one plus
            # whatever the the value of the table is up one and to the left one of position opt[base1][base2]
            elif random_seq[base1 - 1] == random_seq1[base2 - 1]:
                opt[base1][base2] = opt[base1 - 1][base2 - 1] + 1
            # If base1 in random_seq is not equal to base2 in random_seq1 at the same index within their respective
            # sequences, I want the value of the table at position opt[base1][base2] to equal the value of the table
            # directly above or directly to the left of opt[base1][base2], depending on which value is larger
            elif random_seq[base1 - 1] != random_seq1[base2 - 1]:
                opt[base1][base2] = max(opt[base1 - 1][base2], opt[base1][base2 - 1])
    # Print both sequences
    print(random_seq, random_seq1)
    # Print the final table
    print(opt)
    # I want to print the length of the LCS which should be located at the bottom right corner of the completed table
    print("LCS has length", opt[len(random_seq)][len(random_seq1)])

# If the user provides one additional argument in the form of an integer, I want to generate 2 random sequences that
# are the length of the integer the user provided
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
    # Create table of zeros with dimension (1+|random_seq|)-by-(1+|random_seq1|)
    opt = []
    row = []
    for i in range(len(random_seq) + 1):
        row.append(0)
    for k in range(len(random_seq1) + 1):
        opt.append(row)
    for base1 in range(len(random_seq) + 1):
        for base2 in range(len(random_seq1) + 1):
            # I want the values of the table at all positions where either random_seq[0] or random_seq1[0]
            # to equal zero.
            if base1 == 0:
                opt[base1][base2] = 0
            if base2 == 0:
                opt[base1][base2] = 0
            # If base1 in random_seq is equal to base2 in random_seq1 at the same index within their respective
            # sequences, I want the value of the table at position opt[base1][base2] to equal one plus
            # whatever the the value of the table is up one and to the left one of position opt[base1][base2]
            elif random_seq[base1 - 1] == random_seq1[base2 - 1]:
                opt[base1][base2] = opt[base1 - 1][base2 - 1] + 1
            # If base1 in random_seq is not equal to base2 in random_seq1 at the same index within their respective
            # sequences, I want the value of the table at position opt[base1][base2] to equal the value of the table
            # directly above or directly to the left of opt[base1][base2], depending on which value is larger
            elif random_seq[base1 - 1] != random_seq1[base2 - 1]:
                opt[base1][base2] = max(opt[base1 - 1][base2], opt[base1][base2 - 1])
    # Print both sequences
    print(random_seq, random_seq1)
    # Print the final table
    print(opt)
    # I want to print the length of the LCS which should be located at the bottom right corner of the completed table
    print("LCS has length", opt[len(random_seq)][len(random_seq1)])
# If the user provides two addition arguments in the form of two sequences, I want to assign those sequences to
# random_seq and random_seq1
elif len(sys.argv) == 3:
    random_seq_list = []
    random_seq_list1 = []
    for i in sys.argv[1]:
        random_seq_list.append(i)
    for i in sys.argv[2]:
        random_seq_list1.append(i)
    random_seq = ''.join(random_seq_list)
    random_seq1 = ''.join(random_seq_list1)
    # Create table of zeros with dimension (1+|random_seq|)-by-(1+|random_seq1|)
    opt = []
    row = []
    for i in range(len(random_seq) + 1):
        row.append(0)
    for k in range(len(random_seq1) + 1):
        opt.append(row)
    for base1 in range(len(random_seq) + 1):
        for base2 in range(len(random_seq1) + 1):
            # I want the values of the table at all positions where either random_seq[0] or random_seq1[0]
            # to equal zero.
            if base1 == 0:
                opt[base1][base2] = 0
            if base2 == 0:
                opt[base1][base2] = 0
            # If base1 in random_seq is equal to base2 in random_seq1 at the same index within their respective
            # sequences, I want the value of the table at position opt[base1][base2] to equal one plus
            # whatever the the value of the table is up one and to the left one of position opt[base1][base2]
            elif random_seq[base1 - 1] == random_seq1[base2 - 1]:
                opt[base1][base2] = opt[base1 - 1][base2 - 1] + 1
            # If base1 in random_seq is not equal to base2 in random_seq1 at the same index within their respective
            # sequences, I want the value of the table at position opt[base1][base2] to equal the value of the table
            # directly above or directly to the left of opt[base1][base2], depending on which value is larger
            elif random_seq[base1 - 1] != random_seq1[base2 - 1]:
                opt[base1][base2] = max(opt[base1 - 1][base2], opt[base1][base2 - 1])
    # Print both sequences
    print(random_seq, random_seq1)
    # Print the final table
    print(opt)
    # I want to print the length of the LCS which should be located at the bottom right corner of the completed table
    print("LCS has length", opt[len(random_seq)][len(random_seq1)])

