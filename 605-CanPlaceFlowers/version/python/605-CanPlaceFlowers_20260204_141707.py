# Last updated: 2/4/2026, 2:17:07 PM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3        i = 0
4        if n == 0:
5            return True
6        while i < len(flowerbed):
7            if flowerbed[i] == 0:
8                l_empty = i == 0 or flowerbed[i-1] == 0
9                r_empty = i == len(flowerbed)-1  or flowerbed[i+1] == 0
10                if l_empty and r_empty:
11                    flowerbed[i] = 1
12                    n -= 1
13                    i += 2
14                    if n == 0:
15                        return True
16                else:
17                    i += 3
18            else:
19                i += 2
20            
21        return False