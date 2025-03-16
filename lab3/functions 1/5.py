from itertools import permutations

def permutation(soz):
    for i in permutations(soz):
        print("".join(i))

a = input("soz engiz: ")
permutation(a)