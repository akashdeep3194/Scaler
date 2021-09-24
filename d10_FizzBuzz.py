
class Solution:
	# @param A : integer
	# @return a list of strings
    def fizzBuzz(self, A):
        a=A
        arr = []
        for ele in range(1,a+1):
            ans = ""
            if ele%3 == 0:
                ans = "Fizz"
            if ele %5 == 0:
                ans += "Buzz"
            if ans == "":
                ans = ele
            arr.append(ans)