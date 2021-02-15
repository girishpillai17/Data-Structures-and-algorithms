class Solution:
    def romanToInt(self, s: str) -> int:
         
        mapping = {"I": 1,
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M": 1000 }
        
        total = 0

        if len(s) == 0:
            return 0
        i = 0
        while i < len(s)-1:
            print("i=",i)
            currentLet = mapping[s[i]]
            nextLet = mapping[s[i+1]]
            print("currentLet is ",currentLet)
            print("nextLet is ",nextLet)
            
            
            if currentLet >= nextLet:
                total += currentLet
                print("total is ", total)
            else:
                total += (nextLet-currentLet)
                i += 1
                print("total is ", total)
            print()
            i += 1

        currentLet = mapping[s[len(s)-2]]
        nextLet = mapping[s[len(s)-1]]

        if nextLet <= currentLet:
            total += nextLet
            print("total is ", total)
        else :
            total
            print("total is ", total)

        return total



        
