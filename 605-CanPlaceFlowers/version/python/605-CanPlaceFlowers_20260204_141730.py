# Last updated: 2/4/2026, 2:17:30 PM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3        can_place = 0
4        i = 0
5        if n <= 0:
6            return True
7        while i < len(flowerbed):
8            if flowerbed[i] == 0:
9                l_empty = i == 0 or flowerbed[i-1] == 0
10                r_empty = i == len(flowerbed)-1  or flowerbed[i+1] == 0
11                if l_empty and r_empty:
12                    flowerbed[i] = 1
13                    can_place += 1
14                    i += 2
15                    if can_place >= n:
16                        return True
17                else:
18                    i += 3
19            else:
20                i += 2
21            
22        return False
23
24        
25                
26