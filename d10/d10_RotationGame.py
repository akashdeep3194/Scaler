import sys

def rotate(arr,b,n):
    part_a = arr[n-b:]
    part_b = arr[:n-b]
    part_a.extend(part_b)
    return part_a


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    arr = list(map(int,sys.stdin.readline().strip().split()))

    n = arr[0]
    arr = arr[1:]

    b = int(input())

    ans = rotate(arr,b%n,n)

    for ele in ans:
        print(ele,end=" ")

    return 0

if __name__ == '__main__':
    main()