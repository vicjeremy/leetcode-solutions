# Last updated: 2/4/2026, 2:15:22 PM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3        if n == 0 :
4            return True
5        m = len(flowerbed)
6        for i in range(m):
7            if flowerbed[i] == 0:
8                if (i == 0 or flowerbed[i - 1] == 0) and (i == m - 1 or flowerbed[i + 1] == 0):
9                    flowerbed[i] = 1
10                    n -= 1
11                    if n == 0 :
12                        return True
13        return False