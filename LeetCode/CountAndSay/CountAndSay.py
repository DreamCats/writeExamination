# __author__: Mai feng
# __file_name__: CountAndSay.py
# __time__: 2019:05:06:09:35

import pysnooper
@pysnooper.snoop()
def countAndSay(n: int) -> str:
    if n < 1 or n > 30:
        return None
    if n == 1: return '1'
    if n == 2: return '11'
    temp = '11'
    res = ''
    for i in range(2, n):
        count = 0
        pre = temp[0]
        for j, curr in enumerate (temp): 
            if curr == pre:
                count += 1
                if j == len(temp) - 1:
                    res += str(count) + pre
                    break
                else:
                    pre = curr
                    continue
            else:
                if count != 1:
                    res += str(count) + pre
                    count = 1
                else:
                    res +='1' + str(pre)
                if  j == len(temp) - 1:
                    res += '1' + curr
                    break
            pre = curr
        temp = res
        res = ''
    return temp

if __name__ == "__main__":
    res = countAndSay(6)
    print(res)
    