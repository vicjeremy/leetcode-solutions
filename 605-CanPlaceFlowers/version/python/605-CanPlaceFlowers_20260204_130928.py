# Last updated: 2/4/2026, 1:09:28 PM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3        can_place = 0
4        flowerbed = [0] + flowerbed + [0]
5        if n <= 0:
6            return True
7        for i in range(1, len(flowerbed)-1):
8            if flowerbed[i] == 0:
9                if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1]:
10                    flowerbed[i] = 1
11                    can_place += 1
12                    if can_place >= n:
13                        return True
14        
15        return False
16
17        
18                
19