from typing import List
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or len(matrix)==0:
            return []
        ret=[]
        rs,re,cs,ce=0,len(matrix)-1,0,len(matrix[0])-1
        while rs<=re and cs<=ce:
            for i in range(cs,ce+1):
                ret.append(matrix[rs][i])
            rs+=1
            for i in range(rs,re+1):
                ret.append(matrix[i][ce])
            ce-=1
            if rs<=re:
                for i in range(ce,cs-1,-1):
                    ret.append(matrix[re][i])
            re-=1
            if cs<=ce:
                for i in range(re,rs-1,-1):
                    ret.append(matrix[i][cs])
            cs+=1
        return ret




obj=Solution()
print(obj.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]))