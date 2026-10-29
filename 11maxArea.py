#双指针，一直往最大的地方跑
class Solution(object):    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype
        """
        left_index = 0
        right_index = len(height) - 1
        max_area = 0
        while left_index < right_index:
            cur_area = (right_index - left_index) * min(height[right_index],height[left_index])
             #判断后运行，时间开销小
            if cur_area > max_area:
                max_area = cur_area
            if height[right_index] > height[left_index]:
                left_index += 1
            else:
                right_index -= 1
            #每次都会运行，时间开销大
            max_area = max(cur_area,max_area)
        return max_area



#递归方法（超时）
class Solution(object):    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_index = 0
        right_index = len(height) - 1
        return self.method(left_index,right_index,height)
    
    def method(self, left_index , right_index , height):
        if left_index == right_index:
                return 0
        cur_area = (right_index - left_index) * min(height[right_index],height[left_index])
        move_left = self.method(left_index + 1,right_index ,height)
        move_right = self.method(left_index,right_index - 1 ,height) 
            
        max_area = max(cur_area,move_left,move_right)
        # next_max_area = max(method(left_index + 1,right_index ,height),v(left_index,right_index - 1 ,height))
        return max_area    
            
            
            