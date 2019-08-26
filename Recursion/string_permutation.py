def permutation(string):

    out = []

    if len(string) == 1:
        out = [string]

    else:
        for i, let in enumerate(string):

            print("i = ", i)
            print("letter = ", let)

            for perm in permutation(string[:i] + string[i+1:]):

                print('perm = ', perm)

                out += [let + perm]
            
    return out

string = 'ABC'
print(permutation(string))





