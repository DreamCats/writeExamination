# __author__: Mai feng
# __file_name__: RemoveElement.py
# __time__: 2019:04:19:16:23


def removeElement(nums: list, val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)


if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    res = removeElement(nums, val)
    print(res)


