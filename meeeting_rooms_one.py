class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            start = intervals[i].start
            end = intervals[i - 1].end
            if start < end:
                return False

        return True


a = []
a.append(Interval(start=0, end=6))
a.append(Interval(start=5, end=30))

sol = Solution()
print(sol.canAttendMeetings(a))
