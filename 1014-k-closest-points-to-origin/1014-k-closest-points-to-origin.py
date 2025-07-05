class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # ###### MINHEAP

        dist = []
        result = []

        for start, end in points:
            d = (start**2 + end**2)
            dist.append([d, start, end])
        # print(dist)

        heapq.heapify(dist)

        while k > 0:
            d, x, y = heapq.heappop(dist)
            k = k - 1
            result.append([x,y])
        return result





        # ###### HASHMAP: couldn't handle the edge case
        # distance = []
        # h_map = {}

        # for start, end in points:
        #     # print(start, end)
        #     d = (start**2 + end**2)**(1/2)
        #     # distance.append(d)
        #     h_map[(start, end)] = d

        # # distance.sort()
        # h_sort = dict(sorted(h_map.items(), key=lambda i: i[1]))
        # # print(distance)
        # print(h_sort)
        # result = list(h_sort.keys())[:k]
        # print(result)
        # return result
