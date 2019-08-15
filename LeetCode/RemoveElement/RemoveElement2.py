# __author__: Mai feng
# __file_name__: RemoveElement.py
# __time__: 2019:04:19:16:23


def removeElement(nums: list, val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)


def removeElement1(nums: list, val: int) -> int:
    save = []
    count = 0
    for i, num in enumerate(nums):
        if num == val:
            save.append(i - count)
            count += 1
    for s in save:
        del nums[s] 
    return len(nums)

if __name__ == "__main__":
    import time
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    start = time.time()
    res = removeElement(nums, val)
    end = time.time()
    print(res)
    print(end - start)
    
    nums = [0,1,2,2,3,0,4,2]
    start = time.time()
    res1 = removeElement1(nums, val)
    end = time.time()
    print(res1)
    print(end - start)


