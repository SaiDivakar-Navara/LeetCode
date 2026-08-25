class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        lsum = 0
        rsum = 0
        maxsum = 0
        for i in range(k):
            lsum = lsum + cardPoints[i]
            maxsum = lsum
        rindex = n-1
        for i in range(k-1, -1, -1):
            lsum = lsum - cardPoints[i]
            rsum  = rsum + cardPoints[rindex]
            rindex = rindex - 1
            maxsum  = max(maxsum, lsum + rsum)
        return maxsum

