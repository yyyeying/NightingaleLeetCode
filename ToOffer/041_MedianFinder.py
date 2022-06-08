from typing import List


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array: List[int] = []

    def addNum(self, num: int) -> None:
        # print("Add num {}".format(num))
        if len(self.array) == 0:
            self.array.append(num)
            # print(self.array)
            return
        for i in range(len(self.array)):
            if num <= self.array[i]:
                self.array.insert(i, num)
                # print(self.array)
                return
        self.array.append(num)
        return

    def findMedian(self) -> float:
        if len(self.array) == 0:
            return 0
        if len(self.array) % 2 == 0:
            return (self.array[int(len(self.array) / 2 - 1)] + self.array[int(len(self.array) / 2)]) / 2
        else:
            return self.array[int(len(self.array) / 2)]


if __name__ == '__main__':
    s = MedianFinder()
    s.addNum(2)
    s.addNum(1)
    s.addNum(4)
    s.addNum(3)
    print(s.findMedian())
