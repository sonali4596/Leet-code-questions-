'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''

#approach 1
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1 or numRows>=len(s)):
            return s
        delta=-1
        row=0
        res=[[] for i in range(numRows)]
        for i in s:
            res[row].append(i)
            if(row==0 or row ==(numRows-1)):
                delta*=-1
            row+=delta
        for i in range(numRows):
            res[i]="".join(res[i])
        
        return "".join(res)
