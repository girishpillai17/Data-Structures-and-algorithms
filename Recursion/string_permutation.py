def permutation(stri):

    out = []

    if len(stri) == 1:
        out = [stri]

    else:

        for i,letter in enumerate(stri):

            for j in permutation(stri[:i] + stri[i+1:]):

                out += [letter + j]

    return out

stri = 'ABC'
print(permutation(stri))



