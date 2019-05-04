# __author__: Mai feng
# __file_name__: SearchInsert.py
# __time__: 2019:05:04:14:04


import pysnooper
@pysnooper.snoop()
def searchInsert(nums: list, target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    return (low + high) // 2 + 1

if __name__ == "__main__":
    nums = [1,3,6,7,9]
    target = 10
    res = searchInsert(nums, target)
    print(res)