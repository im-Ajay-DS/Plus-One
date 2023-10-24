class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        join=""
        for i in range(len(digits)):
            join=join+str(digits[i])
        add=int(join)+1
        ans=[]
        for i in str(add):
            ans.append(int(i))
        return ans
