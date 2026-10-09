class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        totalUnits = 0
        for boxes, units in boxTypes:
            boxesTaken = min(boxes, truckSize)
            totalUnits += boxesTaken * units
            truckSize -= boxesTaken
            if truckSize == 0:
                break
        return totalUnits