class Solution(object):
    def coloredCells(self, n):
        res=1

        i=0
        while i<n:
            res=res+(4*i)
            i+=1
            
        return(res)
        
        