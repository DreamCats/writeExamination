# __author__: Mai feng
# __file_name__: demo.py
# __time__: 2019:04:04:21:50

def solution():
    x = 153423646
    if x == 0:
        return 0
    sign = True if x < 0 else False
    x = abs(x)
    x_list = reversed (list(str(x)))
    y = int(''.join(x_list))
    y = - y if sign else y
    if y <= 2**31 - 1 and y >= -2**31:
        return y
    return 0


if __name__ == "__main__":
    y = solution()
    print(y)



