class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
    #    print(intervals) 
        result = [intervals[0]]
    #    print(result)
        for start, end in intervals[1:]:
            # print(start, end)
            last = result[-1][1]
            # print(last)
            if last >= start:
                #  print(last, start)
                 result[-1][1] = max(last, end)
            else:
                result.append([start,end])
        # print(result)
        return result