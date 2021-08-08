'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
question link: https://leetcode.com/problems/4sum/
'''
#the write solution
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        front=0
        back=0
        nums.sort()
        #print(nums)
        ans=[]
        inci=incj=1
        
        def dodge_duplicate(n:int):
            j=0
            for p in range(n+1,len(nums)):
                if(nums[n+1]==nums[p]):
                    j+=1
                else:
                    break;
            #print("dodjing value",j)
            return j
        def dodge_duplicate_back(n:int):
            j=0
            for p in range(n-1,0,-1):
                if(nums[n]==nums[p]):
                    j+=1
                else:
                    break;
            #print("dodjing value back",j)
            return j
       
        i=0
        while i<len(nums)-1:
            #print("i=",i)
            j=i+1
            while j<(len(nums)-1):
                #print("j=",j)
                n=target-nums[i]-nums[j]
                #print("n=",n)
                front=j+1
                #print("front=",front)
                back=len(nums)-1
                #print("back=",back)
                while(front<back):
                    if(nums[front]+nums[back])<n:
                        #print("front before",front)
                        if(nums[front]==nums[front+1]):
                            front+=dodge_duplicate(front)+1
                        else:
                            front+=1
                        #print("front after",front)
                        
                       
                       
                        
                        
                        
                    elif(nums[front]+nums[back])>n:
                        #print("back before",back)
                        if(nums[back]==nums[back-1]):
                            back-=dodge_duplicate_back(back)+1
                        else:
                            back-=1
                        #print("back after ",back)
                        
                    else:
                        ans.append([nums[i],nums[j],nums[front],nums[back]])
                        if(nums[front]==nums[front+1]):
                            front+=dodge_duplicate(front)+1
                        else:
                            front+=1
                        if(nums[back]==nums[back-1]):
                            back-=dodge_duplicate_back(back)+1
                        else:
                            back-=1
                        #print("ans list ",ans)
                        #print("front",front)
                        #print("back",back)
                if(nums[j]==nums[j+1]):
                    j+=dodge_duplicate(j)+1
                    
                    #print("incj",j)
                else:
                     j=j+1
            if(nums[i]==nums[i+1]):
                    i+=dodge_duplicate(i)+1
                   
                    #print("inci",i)
            else:
                     i=i+1
        #print("answer list finally",ans)
        return ans 
       
       
       
       
       
#-------------------------------------------------------------------------------------------------------------------------       
#this solution gives memory exceeded
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        front=0
        back=0
        nums.sort()
       # print(nums)
        ans=[]
        inci=incj=1
        #print("hey")
        def dodge_duplicate(n:int):
            j=0
            for p in range(n+1,len(nums)):
                if(nums[n+1]!=nums[p]):
                    j=p
                    break;
            return j
        #print("hi")
        i=0
        while i<len(nums):
            #print("i=",i)
            j=i+1
            while j<len(nums):
               # print("j=",j)
                n=target-nums[i]-nums[j]
                #print("n=",n)
                front=j+1
                #print("front=",front)
                back=len(nums)-1
               # print("back=",back)
                while(front<back):
                    if(nums[front]+nums[back])<n:
                        #print("inside while if sum ",nums[front]+nums[back])
                        front=dodge_duplicate(front)
                        #print("dodge duplicate for foront ",dodge_duplicate(front))
                        #print("inside while if front ",front)
                        
                    elif(nums[front]+nums[back])>n:
                        #print("inside while elif sum ",front+back)
                        back=dodge_duplicate(back)
                        #print("dodge duplicate for back ",dodge_duplicate(back))
                        #print("inside while elif back ",back)
                    else:
                        ans.append([i,j,front,back])
                        #print("ans list ",ans)
                if(nums[j]==nums[j+1]):
                    incj=dodge_duplicate(j)
                    #print("incj",incj)
                else:
                     j=j+1
            if(nums[i]==nums[i+1]):
                    inci=dodge_duplicate(i)
                    #print("inci",inci)
            else:
                     i=i+1
        #print("answer list finally",ans)
        return ans        
