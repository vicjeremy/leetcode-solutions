# Last updated: 2/4/2026, 1:50:26 PM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3        can_place = 0
4        if n <= 0:
5            return True
6        for i in range(len(flowerbed)):
7            if flowerbed[i] == 0:
8                l_empty = i == 0 or flowerbed[i-1] == 0
9                r_empty = i == len(flowerbed)-1  or flowerbed[i+1] == 0
10                if l_empty and r_empty:
11                    flowerbed[i] = 1
12                    can_place += 1
13                    i+=2
14                    if can_place >= n:
15                        return True
16        return False
17
18        
19                
20