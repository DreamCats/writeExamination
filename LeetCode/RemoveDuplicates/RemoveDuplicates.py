# __author__: Mai feng
# __file_name__: RemoveDuplicates.py
# __time__: 2019:04:15:18:28

def removeDuplicates(nums: list) -> int:
    if len(nums) <= 1:
        return len(nums)
    a_nums = sorted(set(nums))
    print(a_nums)
    for i, a in enumerate(a_nums):
        nums[i] = a
    return len(a_nums)



if __name__ == "__main__":
    nums = [-2, -1, 1,1,2,2,3]
    n = removeDuplicates(nums)
    print(n)