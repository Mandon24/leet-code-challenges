from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True if n == 1 else False
        can_plant = False
        for bed_index in range(0, len(flowerbed)):
            if n == 0:
                break
            if bed_index == 0:
                if flowerbed[bed_index] == 0 and flowerbed[bed_index + 1] == 0:
                    flowerbed[bed_index] = 1
                    can_plant = True
                    n -= 1
            elif bed_index == len(flowerbed) - 1:
                if flowerbed[bed_index] == 0 and flowerbed[bed_index - 1] == 0:
                    flowerbed[bed_index] = 1
                    can_plant = True
                    n -= 1                
            else:
                if flowerbed[bed_index] == 0:
                    if flowerbed[bed_index - 1] == 0 and flowerbed[bed_index + 1] == 0:
                        flowerbed[bed_index] = 1
                        can_plant = True
                        n -= 1  
                    else:
                        can_plant = False
                else:
                    continue
        if n > 0:
            return False
        return can_plant
