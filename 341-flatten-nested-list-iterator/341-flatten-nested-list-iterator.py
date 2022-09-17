# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        def flatten_nested_list(nest_list):
            flat_list = []
            for element in nest_list:
                if element.isInteger():
                    flat_list.append(element.getInteger())
                else:
                    flat_list.extend(flatten_nested_list(element.getList()))
            return flat_list
        self.queue = deque(flatten_nested_list(nestedList))
    
    def next(self) -> int:
        return self.queue.popleft()
    
    def hasNext(self) -> bool:
        return self.queue
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())