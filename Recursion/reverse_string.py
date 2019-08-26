def rreverse(s):
    if len(s) <= 1:
        return s
    
    return rreverse(s[1:]) + s[0]

s = 'hello'
print(rreverse(s))