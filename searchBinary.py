class Search:
    def binarySearch(self, lst: list, target) -> str:

       lst.sort()

       low = 0
       high = len(lst) - 1 
       mid = high - low // 2
       
       while(low <= high):
           if(lst[mid] == target):
               return mid
           elif(lst[mid] < target):
               low = mid + 1
           else:
               high = mid - 1
               
           mid = high - low // 2
           
       return 'Not Found'

cls = Search()
print(cls.binarySearch([12,3,5,10,8,1], 1))
print(cls.binarySearch([3,5,7,10,9,1], 7))
print(cls.binarySearch([7,8,9,10,1,2], 3))