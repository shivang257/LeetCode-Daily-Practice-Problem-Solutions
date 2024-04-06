class Solution(object):
    def minRemoveToMakeValid(self, s):
        str_ls = list(s)
        opened = 0
        for i, ch in enumerate(str_ls):
            if ch == '(':
                opened += 1
            elif ch == ')':
                opened -= 1

            if opened < 0: 
                
                str_ls[i] = ''
                opened += 1
           

        if opened > 0:
            
            for i in range(len(str_ls)-1, -1, -1):
                if str_ls[i] == '(': 
                    str_ls[i] = ''
                    opened -= 1
                if opened == 0: break
            
        return ''.join(str_ls)