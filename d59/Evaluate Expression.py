class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        ar = []

        for ele in A:
            if ele not in ("+", "-", "*", "/"):
                ar.append(ele)
            else:
                num2 = int(ar.pop())
                num1 = int(ar.pop())
                if ele == "+":
                    res = num1+num2
                if ele == "-":
                    res = num1-num2
                if ele == "*":
                    res = num1*num2
                if ele == "/":
                    res = num1//num2
                ar.append(res)
        return ar[-1]
        A = A[::-1]
        arr = []
        ctr = 0
        for ele in A:
            if ele in ("+", "-", "*", "/"):
                arr.append(ele)
                ctr = 0
            else:
                ele = int(ele)
                ctr += 1
                if ctr == 1:
                    arr.append(ele)
                while ctr == 2:
                    num = int(arr.pop())
                    op = arr.pop()
                    if op == "+":
                        if len(arr) == 0:
                            arr.append(ele+num)
                            break
                        if arr[-1] in ("+", "-", "*", "/"):
                            ctr = 1
                            arr.append(int(ele)+num)
                        else:
                            arr.append(int(ele)+num)
                            ctr = 2
                            ele = int(arr.pop())
                    if op == "-":
                        if len(arr) == 0:
                            arr.append(ele-num)
                            break
                        if arr[-1] in ("+", "-", "*", "/"):
                            ctr = 1
                            arr.append(ele-num)
                        else:
                            arr.append(ele-num)
                            ctr = 2
                            ele = int(arr.pop())

                    if op == "*":
                        if len(arr) == 0:
                            arr.append(ele*num)
                            break
                        if arr[-1] in ("+", "-", "*", "/"):
                            ctr = 1
                            arr.append(ele*num)
                        else:
                            arr.append(ele*num)
                            ele = int(arr.pop())
                            ctr = 2

                    if op == "/":
                        if len(arr) == 0:
                            arr.append(ele//num)
                            break
                        if arr[-1] in ("+", "-", "*", "/"):
                            ctr = 1
                            arr.append(ele//num)
                        else:
                            arr.append(ele//num)
                            ctr = 2
                            ele = int(arr.pop())
        return arr[-1]


if __name__ == "__main__":
    s = Solution()
    A = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
    print(s.evalRPN(A))
