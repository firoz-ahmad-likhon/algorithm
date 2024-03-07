# https://www.youtube.com/watch?v=-f6fjBhu8eA
class Binary:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''
        
        lenA = len(a) - 1
        lenB = len(b) - 1
            
        while(lenA >= 0 or lenB >= 0):
            
            if(lenA >= 0):
                digit1 = int(a[lenA], base=2)
            else:
                digit1 = 0
                
            if(lenB >= 0):
                digit2 = int(b[lenB], base=2)
            else:
                digit2 = 0
                
            carry, digit = divmod(digit1 + digit2 + carry, 2)

            result += str(digit)

            lenA -= 1
            lenB -= 1
            
        if(carry):
            result += str(carry)
            
        return result[::-1]
