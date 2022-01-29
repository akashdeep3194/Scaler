# "Given an integer N representing the number of pairs of parentheses,
# the task is to generate all combinations of well-formed(balanced) parentheses.

# Example 1:
# Input:
# N = 3
# Output:
# ((()))
# (()())
# (())()
# ()(())
# ()()()

# open>closed:
#     open another
#     close

# open = closed:
#     open another

# n = open = closed

def parentheses(open, closed, ele, n, ans):
    if open == closed and closed == n:
        ans.append(ele)
        return
    if open == closed:
        parentheses(open+1, closed, ele+"(", n, ans)
    elif open > closed:
        if open < n and closed <= n:
            parentheses(open+1, closed, ele+"(", n, ans)
        if closed < n and open <= n:
            parentheses(open, closed+1, ele+")", n, ans)

    return


answer = []

parentheses(0, 0, "", 4, answer)

for ele in answer:
    print(ele)
