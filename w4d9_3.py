import sys

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    t = int(input())
    while(t>0):
        arr = list(map(int,sys.stdin.readline().strip().split()))
        l = arr[0]
        arr = arr[1:]
        co = 0
        ce = 0
        for ele in arr:
            if ele&1 == 0:
                ce += 1
            else:
                co += 1
        print(abs(ce-co))
        t-=1

    return 0

if __name__ == '__main__':
    main()