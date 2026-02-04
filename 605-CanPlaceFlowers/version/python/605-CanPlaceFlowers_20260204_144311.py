# Last updated: 2/4/2026, 2:43:11 PM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        total = 0
        length = len(flowerbed) - 1
        i = 1
        while i < length:
            if flowerbed[i + 1] == 1:
                i += 3
                continue
            if flowerbed[i] == 1:
                i += 2
                continue
            else:
                i += 2
                total += 1

        if total >= n:
            return True
        return False

        