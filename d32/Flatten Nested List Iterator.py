class NestedIterator:

    def __init__(self, nestedList):
        self.nestedList = nestedList
        self.i = 0
        self.child_list = None
    
    def next(self):        
        if self.i == len(self.nestedList):
            return None            

        if type(self.nestedList[self.i]) is type(int(1)):
            val = self.nestedList[self.i]
            self.i += 1
            return val
        if self.child_list is not None:
            ele = self.child_list.next()
            if ele is None:
                self.child_list = None
                self.i += 1
                return self.next()
            return ele
        else:
            self.child_list = NestedIterator(self.nestedList[self.i])
            return self.child_list.next()


    def hasNext(self):
        if self.i < len(self.nestedList):
            return True
        else:
            return False

s = NestedIterator([[[[2,3]]]])

while s.hasNext():
    print(s.next(),len(s.nestedList))
