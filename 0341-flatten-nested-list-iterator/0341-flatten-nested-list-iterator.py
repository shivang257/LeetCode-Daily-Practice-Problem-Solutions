class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.data = nestedList
        self.cur = -1
        self.inneriter = None

    def next(self):
        """
        :rtype: int
        """
        if self.inneriter:
            return self.inneriter.next()
        return self.data[self.cur].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.inneriter and self.inneriter.hasNext():
            return True
        self.inneriter = None
        if self.cur < len(self.data)-1:
            self.cur += 1
            if self.data[self.cur].isInteger():
                return True
            self.inneriter = NestedIterator(self.data[self.cur].getList())
            if self.inneriter.hasNext():
                return True
            self.inneriter = None
            return self.hasNext()
        return False