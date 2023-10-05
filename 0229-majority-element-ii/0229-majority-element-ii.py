class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m1,m2,c1,c2=0,0,0,0
        l=[]
        for n in nums:
            if(m1==n):
                c1+=1
            elif(m2==n):
                c2+=1
            elif(c1==0):
                m1=n
                c1+=1
            elif(c2==0):
                m2=n
                c2+=1
            else:
                c1-=1
                c2-=1
        x,y=0,0
        for i in range(len(nums)):
            if(nums[i]==m1):
                x+=1
            if(nums[i]==m2):
                y+=1
        if(x>len(nums)//3):
            l.append(m1)
        if(y>len(nums)//3):
            l.append(m2)
        return set(l)