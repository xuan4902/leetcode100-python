class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #思路  思路正确，但是代码不会写，加强coding能力

        res = []

        #排序队首
        intervals.sort(key = lambda x:x[0])
        #for遍历
        i = 0
        while i < len(intervals):
            small_res = intervals[i][0]
            max = intervals[i][1]
            while i + 1 < len(intervals) and intervals[i + 1][0] <= max:
                if intervals[i + 1][1] > max:
                    max = intervals[i + 1][1]
                i += 1
            res.append([small_res,max])
            i += 1
        return res

        #while   next。first值《last。end值
        #  max
        #  next.end》last。end  修改end
        #存入last。start   max
        # return