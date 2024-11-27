class Solution:
    def trap(self, height: List[int]) -> int:
        # SOLUTION 2
        l, r = 0, len(height)-1
        output = 0
        max_l = 0
        max_r = 0

        while l < r:
            if height[l] <= height[r]:
                max_l = max(max_l, height[l])
                output = output + (max_l - height[l])
                l += 1
            else:
                max_r = max(max_r, height[r])
                output = output + (max_r - height[r])
                r -= 1

        print(output)
        return output



        # SOLUTION 1
        # max_left = [0]*len(height)
        # max_right = [0]*len(height)

        # max_l = 0
        # for i, n in enumerate(height):
        #     if i == 0:
        #         max_left[i] = 0
        #     else:
        #         max_l = max(max_l, height[i-1])
        #         max_left[i] = max_l

        # max_r = 0
        # max_right[len(height) - 1] = 0
        # for i in range(len(height)-2, -1, -1):
        #     if i == 0:
        #         max_r = max(max_right[i+1], height[i+1])
        #         max_right[i] = max_r
        #         break
        #     else:
        #         max_r = max(max_right[i+1], height[i+1])
        #         max_right[i] = max_r

        # result = 0
        # for i in range(len(height)):
        #     val = min(max_left[i], max_right[i]) - height[i]
        #     # print(val)
        #     if val < 0:
        #         result += 0
        #     else:
        #         result = result + val
        # # print(max_left)
        # # print(max_right)
        # print(result)
        # return(result)