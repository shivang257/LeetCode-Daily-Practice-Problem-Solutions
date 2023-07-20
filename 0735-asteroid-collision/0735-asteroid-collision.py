class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] >= 0 and a < 0:
                collision = stack[-1] + a 
                if collision <= 0:
                    stack.pop() 
                if collision >= 0:
                    break
            else:
                stack.append(a)
        return stack