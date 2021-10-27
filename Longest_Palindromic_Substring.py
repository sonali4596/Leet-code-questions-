'''Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
Question link :https://leetcode.com/problems/longest-palindromic-substring/
'''

#Solution

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            #print("oddtemp",tmp)
            if len(tmp) > len(res):
                res = tmp
                #print("oddres",res)
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            #print("eventemp",tmp)
            if len(tmp) > len(res):
                res = tmp
                #print("evenres",res)
        return res
 
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    # the Helper is implemented to vcheck for palindrome you think as a  symmetrical        decoration string unwinding slowly 
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        #print("l",l)
        #print("r",r)
        #print("helper",s[l+1:r])
        return s[l+1:r]
