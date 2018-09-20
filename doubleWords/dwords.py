class Dwords(object):
    def __init__(self):
        pass

    def user_input(self, user_input):
        if user_input:
            user_cmd = list(user_input)
            old_word = ''
            count_list = []
            count = 1
            records = {}
            for i in range(len(user_cmd)):
                if i == 0:
                    old_word = user_cmd[i]
                else:
                    if user_cmd[i] == old_word:
                        count = count + 1
                        if i == len(user_cmd) - 1:
                            count_list.append(count)
                    else:
                        count_list.append(count)
                        count = 1                       
                    old_word = user_cmd[i]
            for i, count in enumerate(count_list):
                if i == len(count_list) - 2:
                    break
                else:
                    if count == count_list[i + 2]:
                        if count > count_list[i + 1]:
                            before_num = 0
                            for j in range(i):
                                before_num  = before_num + count_list[j]
                            record = ''.join(user_cmd[before_num:(before_num + count * 2 + count_list[i + 1])])
                            records[record] = count
                        else:
                            continue
                    else:
                        continue
            result = max(records, key=records.get)
            print(count_list)
            print(records)
            print(result)
    
def main():
    dwords = Dwords()
    user_cmd = 'aabcccdeeea'
    user_cmd = 'AAABCCCDEEEEFCCCC'
    dwords.user_input(user_cmd)

if __name__ == '__main__':
    main()