class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        ans = ""
        arr = []
        for ele in A[1:]:
            if ele == "/":
                if ans == "." or ans == "/":
                    pass
                elif ans == "..":
                    if len(arr) != 0:
                        arr.pop()
                else:
                    if len(ans) > 0:
                        arr.append(ans)
                ans = ""
            else:
                ans = ans + ele
        if ans != "":
            if ans == "." or ans == "/":
                pass
            elif ans == "..":
                if len(arr) > 0:
                    arr.pop()
            elif len(ans) != 0:
                arr.append(ans)
        ans = ""
        if len(arr) == 0:
            ans = "/"
        for ele in arr[:]:
            ans = ans + "/" + ele
        return ans


if __name__ == "__main__":
    s = Solution()
    # A = "/./.././ykt/xhp/nka/eyo/blr/emm/xxm/fuv/bjg/./qbd/./../pir/dhu/./../../wrm/grm/ach/jsy/dic/ggz/smq/mhl/./../yte/hou/ucd/vnn/fpf/cnb/ouf/hqq/upz/akr/./pzo/../llb/./tud/olc/zns/fiv/./eeu/fex/rhi/pnm/../../kke/./eng/bow/uvz/jmz/hwb/./././ids/dwj/aqu/erf/./koz/.."
    A = "/asd"
    print(s.simplifyPath(A))
