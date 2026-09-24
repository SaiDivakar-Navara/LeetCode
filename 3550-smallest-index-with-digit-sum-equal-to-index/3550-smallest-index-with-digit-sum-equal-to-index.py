class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        sum_array = []
        st = []
        for i in nums:
            c = 0
            for j in str(i):
                c += int(j)
            sum_array.append(c)
        for i in range(len(sum_array)):
            if sum_array[i] == i:
                st.append(i)   
        if st:
            return min(st)
        return -1

