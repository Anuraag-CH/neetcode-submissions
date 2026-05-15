class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        res= []
        n =2

        for i in range(0,n):
            for j in nums :
                res.append(j)
        
        return res
        