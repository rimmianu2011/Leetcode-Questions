class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            
            mid = (left + right) // 2
            total_hour = 0
            for p in piles:
                total_hour += math.ceil(p / mid)
                # print(left, total_hour)
            if total_hour <= h:
                right = mid - 1
                result = min(mid, result)
            else:
                left = mid + 1
            # print('hi', total_hour)
        print(result)
        return result
        