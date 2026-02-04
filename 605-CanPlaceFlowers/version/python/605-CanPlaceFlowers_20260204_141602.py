# Last updated: 2/4/2026, 2:16:02 PM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3        flowerbed.append(0)
4        flowerbed.insert(0,0)
5        plant = 0
6        for x in range(1, len(flowerbed)-1):
7            if flowerbed[x] == 0:
8                if flowerbed[x-1] == 0 and flowerbed[x+1] == 0:
9                    plant +=1
10                    flowerbed[x] = 1
11                if plant >= n:
12                    return True
13        return plant >= n