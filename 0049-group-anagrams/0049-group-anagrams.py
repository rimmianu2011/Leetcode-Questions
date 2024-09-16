class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) <= 1:
            return [strs]
        
        new_strs = defaultdict(list)
        for i in range(len(strs)):
            sort_s = ''.join(sorted(strs[i]))
            new_strs[sort_s].append(strs[i])

        # print(new_strs)
        result = list(new_strs.values())
        print(result)
        return result
