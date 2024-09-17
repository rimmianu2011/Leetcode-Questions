class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict_num = {}
        k_freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            if i in dict_num:
                dict_num[i] += 1
            else:
                dict_num[i] = 1
        # print(dict_num)

        for n, v in dict_num.items():
            k_freq[v].append(n)

        k_res = []

        for i in range(len(k_freq)-1, 0, -1):
            for j in k_freq[i]:
                k_res.append(j)
                if len(k_res) == k:
                    return k_res
            # print(k_res)
        