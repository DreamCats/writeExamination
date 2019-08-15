# __author__: Mai feng
# __file_name__: MaxSubArray.py
# __time__: 2019:05:18:15:58


import pysnooper
@pysnooper.snoop()
def maxSubArray(nums: list) -> int:
    res = nums[0]
    temp = 0
    for num in nums:
        if temp > 0:
            temp += num
        else:
            temp = num
        res = max(res, temp)
    return res


if __name__ == "__main__":
    # l = [-2,1,-3,4,-1,2,1,-5,4]
    # l = [1,2,-1]
    # l = [-3,1,-2]
    # l = [-1, -2 , -3]
    # l = [-2,1,-1,4,-1,2,1,-5,4]
    l=[-2,-1]
    l = [1,2,-1,-2,2,1,-2,1,4,-5,4]
    res = maxSubArray(l)
    print(res)