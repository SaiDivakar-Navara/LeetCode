class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        Arrow = 1
        x = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= x:
                continue
            else:
                x = points[i][1]
                Arrow += 1
        return Arrow