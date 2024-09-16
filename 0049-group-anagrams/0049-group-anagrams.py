class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # method 1: with O(n*mlogm)

        # if len(strs) <= 1:
        #     return [strs]

        # new_strs = defaultdict(list)
        # for i in range(len(strs)):
        #     sort_s = ''.join(sorted(strs[i]))
        #     new_strs[sort_s].append(strs[i])

        # # print(new_strs)
        # result = list(new_strs.values())
        # print(result)
        # return result


        # method 2 :with O(n*m*26)

        new_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1 

            new_dict[tuple(count)].append(s)

        return new_dict.values()
