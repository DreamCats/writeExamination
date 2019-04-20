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


def removeElement2(nums: list, val: int) -> int:
    slow = -1
    for i in range(0, len(nums)):
        if nums[i] != val:
            slow += 1
            nums[slow] = nums[i]
    return slow + 1 


def removeElement3(nums: list, val: int) -> int:
    j=len(nums)
    for i in range(j-1,-1,-1):
        print(i)
        if nums[i]==val:
            nums.pop(i)    
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


    # nums = [0,1,2,2,3,0,4,2]
    nums = [2,2,3,2]
    start = time.time()
    res2 = removeElement2(nums, val)
    end = time.time()
    print(res2)
    print(end - start)

    nums = [2,2,3,2]
    start = time.time()
    res3 = removeElement3(nums, val)
    end = time.time()
    print(res3)
    print(end - start)