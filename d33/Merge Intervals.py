# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def isNewIntervalBeforeCurrent(self,current:Interval,new:Interval):
        if current.start>new.end:
            return True
        else:
            return False
    def isNewIntervalOverlappingCurrent(self,current:Interval,new:Interval):
        if not(current.start>new.end or current.end  < new.start):
            return True
        else:
            return False

    def insert(self, intervals:Interval, newInterval:Interval):
        ans = []
        i=0
        for i,iv in enumerate(intervals):
            if self.isNewIntervalBeforeCurrent(iv,newInterval):
                break
            elif self.isNewIntervalOverlappingCurrent(iv,newInterval):
                newInterval.start = min(iv.start,newInterval.start)
                newInterval.end = max(iv.end,newInterval.end)        
            else:
                # skip this interation
                ans.append(iv)
        else:
            i+=1
        ans.append(newInterval)
        ans.extend(intervals[i:])
        
        return ans
# s = Solution()
# a = Interval(1,3)
# b = Interval(6,9)
# c = Interval(2,5)

# ans = s.insert([a,b],c)
# for ele in ans:
#     print(ele.start,ele.end)
