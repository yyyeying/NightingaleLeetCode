from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        self.arr = arr
        self.quickSort()
        return self.arr[:k]

    def quickSort(self):
        if self.arr is None:
            return
        self.partition(0, len(self.arr) - 1)

    def partition(self, low, high):
        if low >= high:
            return
        base = self.arr[low]
        lptr = low + 1
        hptr = high
        while True:
            while lptr <= high and self.arr[lptr] < base:
                lptr += 1
            while hptr > low and self.arr[hptr] >= base:
                hptr -= 1
            if lptr < hptr:
                self.arr[lptr], self.arr[hptr] = self.arr[hptr], self.arr[lptr]
            else:
                break
        self.arr[low], self.arr[hptr] = self.arr[hptr], self.arr[low]
        self.partition(low, hptr)
        self.partition(hptr+1, high)


if __name__ == '__main__':
    print(Solution().getLeastNumbers([4, 43, 2, 1], 4))
