import heapq

class MedianFinder:
    def __init__(self):
        self.left_big_basket = []
        self.right_small_basket = []

    def addNum(self, num):
        if not self.left_big_basket or num <= -self.left_big_basket[0]:
            heapq.heappush(self.left_big_basket, -num)
        else:
            heapq.heappush(self.right_small_basket, num)

        left_count = len(self.left_big_basket)
        right_count = len(self.right_small_basket)
        if left_count - right_count > 1:
            max_left = -heapq.heappop(self.left_big_basket)
            heapq.heappush(self.right_small_basket, max_left)
        elif right_count - left_count > 0:
            min_right = heapq.heappop(self.right_small_basket)
            heapq.heappush(self.left_big_basket, -min_right)

    def findMedian(self):
        total = len(self.left_big_basket) + len(self.right_small_basket)
        if total % 2 == 1:
            return -self.left_big_basket[0]
        else:
            return (-self.left_big_basket[0] + self.right_small_basket[0]) / 2


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(3)
    print("放入3，中位数：", mf.findMedian())

    mf.addNum(1)
    print("放入1，中位数：", mf.findMedian())

    mf.addNum(4)
    print("放入4，中位数：", mf.findMedian())

    mf.addNum(1)
    print("放入1，中位数：", mf.findMedian())

    mf.addNum(5)
    print("放入5，中位数：", mf.findMedian())