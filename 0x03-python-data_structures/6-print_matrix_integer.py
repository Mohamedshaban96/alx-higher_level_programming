#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    coun = 0
    for x in matrix:
        coun = 0
        for i in x:
            if coun == len(x) - 1:
                print("{:d}".format(i), end='')
            else:
                print("{:d}".format(i), end="")
                coun += 1
        print()
