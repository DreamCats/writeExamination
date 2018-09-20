# maifeng
import math

class Songs(object):
    def __init__(self):
        super(Songs, self).__init__()

    def user_input(self, user_cmd:str):
        if user_cmd:
            try:
                user_cmd = user_cmd.split('\n')
                self.k = int(user_cmd[0])
                self.x = int(user_cmd[1].split(' ')[0])
                self.a = int(user_cmd[1].split(' ')[1])
                self.y = int(user_cmd[1].split(' ')[2])
                self.b = int(user_cmd[1].split(' ')[3])
            except Exception as e:
                print('input is not true', e)
        else:
            print('input is not true')
        
    def output(self):
        for i in range(0, self.x + 1):
            if (self.k - self.a * i) % self.b == 0:
                self.b_temp = (self.k - self.a * i) / self.b
                if self.b_temp > self.y:
                    print('没有组合')
                    for j in range(0, self.y + 1):
                        if (self.k - self.b * j) % self.a == 0:
                            self.a_temp = (self.k - self.b * j) / self.a
                            if self.a_temp > self.x:
                                print('没有组合')
                            else:
                                self.b_temp = j
                                self.a_result = math.factorial(self.x) / (math.factorial(self.a_temp) * (math.factorial(self.x - self.a_temp)))
                                self.b_result = math.factorial(self.y) / (math.factorial(self.b_temp) * (math.factorial(self.y - self.b_temp)))
                                if self.k % self.a == 0 and self.k % self.b == 0:
                                    print(self.a_result + self.b_result)
                                else:
                                    print(self.a_result * self.b_result)
                                break
                        else:
                            if j == self.y:
                                print('没有组合')
                else:
                    self.a_temp = i
                    self.a_result = math.factorial(self.x) / (math.factorial(self.a_temp) * (math.factorial(self.x - self.a_temp)))
                    self.b_result = math.factorial(self.y) / (math.factorial(self.b_temp) * (math.factorial(self.y - self.b_temp)))
                    if self.k % self.a == 0 and self.k % self.b == 0:
                        print(self.a_result + self.b_result)
                    else:
                        print(self.a_result * self.b_result)
                    break
            else:
                if i == self.x:
                    print('没有组合')


                    

       
                
def main():
    songs = Songs()
    user = '8\n3 2 3 3'
    # user = '20\n100 2 200 3'
    songs.user_input(user)
    songs.output()

if __name__ == '__main__':
    main()