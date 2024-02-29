class Search:
    def linearSearch(self, lst: list, target) -> str:
     
       for x in range(len(lst)):
           if(lst[x] == target):
               return x

       return 'Not Found'
        
cls = Search()
print(cls.linearSearch([12,3,5,10,8,1], 1))
print(cls.linearSearch([3,5,7,10,9,1], 7))
print(cls.linearSearch([7,8,9,10,1,2], 3))