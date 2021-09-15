class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list1=[]
        
        for i  in range(len(nums)):
            
            for y in range(i+1,len(nums)):
                
                z=0-nums[i]-nums[y]
                if z in nums:
                    
                    list1.append([nums[i],nums[y],z])
        print(list1)
        return list1 
