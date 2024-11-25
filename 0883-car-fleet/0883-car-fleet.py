class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        comb = [[p, s] for p, s in zip(position, speed)]  
        stack = []
        for p, s in sorted(comb) [::-1]:
        
            time = (target-p)/s
            # print(type(time))
            stack.append(time)

            if len(stack) > 1 and ( time <= stack[-2]):
                stack.pop()
        print(stack)
        return len(stack)