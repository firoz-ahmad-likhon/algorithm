class Matrix:
   def add(self, m1: list[list[int]], m2: list[list[int]]) -> list[list[int]]:
       matrix = [[0 for x in range(len(m1))] for y in range(len(m1[0]))]
  
       for r in range(len(m1)):
           for c in range(len(m1[0])):
               matrix[r][c] = m1[r][c] + m2[r][c]
    
       return matrix
   
   def transpose(self, m: list[list[int]]) -> list[list[int]]:
        matrix = [[0 for x in range(len(m))] for y in range(len(m[0]))]
   
        for r in range(len(m)):
            for c in range(len(m[0])):
                matrix[c][r] = m[r][c]
     
        return matrix
    
   def identity(self, m: list[list[int]]) -> bool:
    
        for r in range(len(m)):
            for c in range(len(m[0])):
                if(r == c and m[r][c] != 1):
                    return False
                if(r != c and m[r][c] != 0):
                    return False
      
        return True
        
cls = Matrix()

print(cls.add(
    [
     [8, 14, -6], 
      [12,7,4], 
      [-11,3,21]
    ], 
    [
     [3, 16, -6],
     [9,7,-4], 
     [-1,3,13]
    ]))
print(cls.transpose([
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
    ]))
print(cls.identity([
     [1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]
    ]))