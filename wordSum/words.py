# maifeng


class words_sum(object):
    def __init__(self):
        self.words = list('abcdefghigklmnopqrstuvwxyz')
        
    def user_inpiut(self, user_cmd):
        self.first_line = list(user_cmd.split('\n')[0])
        self.second_line = list(user_cmd.split('\n')[1])

    def output(self):
        first_num = len(self.first_line)
        second_num = len(self.second_line)
        sum_words = []
        carry_flag = 0
        if second_num < first_num:
            for i in range(0 ,first_num):
                if i < second_num:
                    first_value = self.words.index(self.first_line[first_num - i - 1]) + carry_flag
                    second_value = self.words.index(self.second_line[second_num - i - 1])
                    sum_value = first_value + second_value
                    if sum_value > 25:
                        sum_words.append(self.words[(sum_value - 26)])
                        carry_flag = 1
                    else:
                        sum_words.append(self.words[sum_value])
                        carry_flag = 0  
                else:
                    sum_words.append(self.words[i])         
        else:
             for i in range(0 ,second_num):
                if i < first_num:
                    first_value = self.words.index(self.first_line[first_num - i - 1]) 
                    second_value = self.words.index(self.second_line[second_num - i - 1]) + carry_flag
                    sum_value = first_value + second_value
                    if sum_value > 25:
                        sum_words.append(self.words[(sum_value - 26)])
                        carry_flag = 1
                    else:
                        sum_words.append(self.words[sum_value])
                        carry_flag = 0  
                else:
                    sum_words.append(self.words[i]) 
        sum_words.reverse()
        print(''.join(sum_words))


def main():
    w_s = words_sum()
    user_cmd = 'gfedcba\ncba'
    # user_cmd = 'cba\ngfedcba'
    user_cmd = 'xyz\ncab'
    w_s.user_inpiut(user_cmd)
    w_s.output()

if __name__ == '__main__':
    main()