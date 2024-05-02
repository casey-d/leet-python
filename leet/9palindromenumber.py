class Leet9:
    def is_palindromenumber(num:int) -> bool:
        numstring = ""+str(num)
        rstring = "";
        for char in numstring:
            rstring=char+rstring
        return numstring==rstring



print(Leet9.is_palindromenumber(121))
print(Leet9.is_palindromenumber(-121))
