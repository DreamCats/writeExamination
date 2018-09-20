
# author:maifeng


class Twin(object):
    def __init__(self):
        super(Twin, self).__init__()

    def user_input(self, user_cmd):
        if user_cmd:
            self.s_num, self.s  = self.deal_input(user_cmd)
        else:
            print('用户输入为空')
            return None
    
    def deal_input(self, user_cmd):
        if user_cmd:
            user_cmd = user_cmd.split('\n')
            s_num = user_cmd[0]
            s = user_cmd[1:]
            return s_num, s
        else:
            return None

    def output(self):
        success = 'Yeah'
        fail = 'Sad'
        result = False
        for i, content in enumerate(self.s):
            for j in range(i + 1, int(self.s_num)):
                if len(content) == len(self.s[j]):
                    result = self.detect_words(content, self.s[j])
                    if result == True:
                        break
                else:
                    continue
            if result == True:
                break
        if result == True:
            print(success)
        else:
            print(fail)

    def detect_words(self, s1, s2):
        result = True
        s1_num = len(s1)
        for i, s in enumerate(s1):
            for j, s_ in enumerate(s2):
                if s == s_:
                    s1_back = i - 1
                    s1_forward = i + 1
                    s2_back = j - 1
                    s2_forward = j + 1
                    if s1_forward == s1_num:
                        s1_forward = 0
                    if s2_forward == s1_num:
                        s2_forward = 0    
                    if s1[s1_back] == s2[s2_back] or s1[s1_back] == s2[s2_forward]:
                        if s1[s1_forward] == s2[s2_back] or s1[s1_forward] == s2[s2_forward]:
                            result = True
                            break
                        else:
                            result = False
                    else:
                        result = False 
            if result == False:          
                return result                       
        return result

def main():
    twin = Twin()
    content = '2\nabcde\neabcd'
    # content = '2\nhelloworld\nworldhello'
    # content = '3\n2\nhelloworld\nhdlrowolle'
    twin.user_input(content)
    twin.output()


if __name__ == '__main__':
    main()