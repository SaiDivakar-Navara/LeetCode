class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        answer = []
        for i in range(len(s)):
            min_distance = float('inf')
            for j in range(len(s)):
                if s[j] == c:
                    distance = abs(i - j)
                    min_distance = min(min_distance, distance)
            answer.append(min_distance)
        return answer

