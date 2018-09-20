class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        #储存答案
        ans_list = []
        #用来切割words的指针
        i = 0
        
        while i < len(words):#开始遍历字符串
            beigin = i#选取的区间开始的指针
            wordsum = 0 #所有数字加起来的总字数
            leastspace = 0 #最少需要空几个空格
            end = i#选取的区间结尾的指针
            oneresult = ""#储存这一次添入最终结果的答案
            #不断去扩展end的范围，在能添加的情况下不断添加单词
            while end < len(words) and len(words[end]) + wordsum + leastspace <= maxWidth:
                leastspace += 1
                wordsum += len(words[end])
                end += 1
            
            leastspace -= 1
            oneresult = ""
            #如果end到了最后一项，也就是刚好把最后一个单词也包括了
 
            if end == len(words):
                for i in words[beigin:end]:
                    oneresult += i
                    if leastspace != 0:
                        #适当地添加空格
                        oneresult += " "
                        leastspace -= 1
                ans_list.append(oneresult)
                break
                        
            realsum = 0 
            for j in words[beigin:end]:
                realsum += len(j)#算出所有单词的总字符数
            #还剩下多少个位置可以留给空格
            left_space = maxWidth - realsum
            if leastspace != 0:
                #分配给每个单词后的空格
                eachspace = left_space // (leastspace)
                left_space2 = left_space - eachspace*leastspace
            else:
                
                oneresult += words[beigin] + left_space*" "
                ans_list.append(oneresult)
                i = end
                continue
            
            oneresult = ""
            for j in words[beigin:end]:#添加空格，并且保证先添加比较多的空格
                oneresult += j 
                if leastspace > 0:
                    oneresult += eachspace*" "
                    leastspace -= 1
                    if left_space2 > 0:#left_space2是用来添加额外的空格的，来营造出左边的空格比较多的效果
                        oneresult += " "
                        left_space2 -= 1
 
            ans_list.append(oneresult)
            i = end
        #保证最后一项的maxWidth达到标准（补全空格）
        if len(ans_list[-1]) < maxWidth:
            ans_list[-1] += " "*(maxWidth-len(ans_list[-1]))
        return ans_list


def main():
    sl = Solution()

    result = sl.fullJustify(['i\'m','king','of','the','world'],5)
    for res in result:
        print(res)

if __name__ == '__main__':
    main()