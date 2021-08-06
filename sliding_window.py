'''You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

'''
# leet code question link : https://leetcode.com/problems/sliding-window-maximum/
#this solution has used data structure double linked list. 
class Solution:
    def maxSlidingWindow(self, list1: List[int], k: int) -> List[int]:
        deque1=collections.deque()
        ans=[]
        for i in range(len(list1)):
            #print("i",i)
            if(len(deque1)!=0 and deque1[0]==(i-k)):
                #print(" if deque before pop",deque1)
                deque1.popleft()
                #print(" if deque after pop",deque1)
            
            while len(deque1)!=0 and list1[deque1[len(deque1)-1]]<list1[i]:
                #print("deque backelement",deque1[len(deque1)-1])
                #print(" while deque after pop",deque1)
                deque1.pop() 
                #print("while deque after pop",deque1)
            deque1.append(i)
            #print(" deque afterpush",deque1)
            if(i>=k-1):
                ans.append(list1[deque1[0]])
                #print(" ans afterpush",ans)
        return ans
