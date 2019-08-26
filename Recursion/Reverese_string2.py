def reverse(stri):
    if len(stri) == 0:
        return stri
    
    temp = stri[0]
    reverse(stri[1:])

    print(temp, end='')

stri = 'Girish Pillai'
reverse(stri)