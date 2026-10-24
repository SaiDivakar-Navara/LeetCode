class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def count_days(s: str):
            days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            month = int(s[0:2])
            days = int(s[3:5])
            for i in range(month - 1):
                days += days_month[i]
            return days
        left = max(count_days(arriveAlice), count_days(arriveBob))
        right = min(count_days(leaveAlice), count_days(leaveBob))
        return max(0, right - left + 1)