class Solution:
    def Permutation(self, ss):
        # write code here
        # 递归，python中str类型无法修改，所以需要先转换成列表再进行处理
        if not ss:
            return []
        res = []
        self.Core(res, list(ss), 0)
        return res

    def Core(self, res, ss, i):
        if i == len(ss) - 1:
            res.append("".join(ss))
        else:
            for j in range(i, len(ss)):
                tmp = ss[i]
                ss[i] = ss[j]
                ss[j] = tmp
                # 按值传递
                self.Core(res, ss, i + 1)
                tmp = ss[i]
                ss[i] = ss[j]
                ss[j] = tmp

test = Solution()
print(test.Permutation('aa'))