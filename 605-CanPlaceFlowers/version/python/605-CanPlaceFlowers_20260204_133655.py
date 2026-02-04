# Last updated: 2/4/2026, 1:36:55 PM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3        can_place = 0
4        if n <= 0:
5            return True
6        for i in range(len(flowerbed)):
7            if flowerbed[i] == 0:
8                if (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
9                    flowerbed[i] = 1
10                    can_place += 1
11                elif (i == 0 and flowerbed[i+1] == 0):
12                    flowerbed[i] = 1
13                    can_place += 1
14                elif i == len(flowerbed)-1 and flowerbed[i-1] == 0:
15                    flowerbed[i] = 1
16                    can_place += 1
17                elif flowerbed[i-1] == 0 == flowerbed[i+1]:
18                    flowerbed[i] = 1
19                    can_place += 1
20            if can_place >= n:
21                return True
22        return False
23
24        
25                
26