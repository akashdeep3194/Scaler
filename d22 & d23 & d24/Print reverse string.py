import sys
sys.setrecursionlimit(10**5)
def rev(s,si,ei):
    if si>=ei:
        return s[si:ei+1]
    ans = s[ei] + rev(s,si+1,ei-1) +s[si]

    return ans

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    a = input()

    print(rev(a,0,len(a)-1))

    return 0

if __name__ == '__main__':
    main()

# main()
