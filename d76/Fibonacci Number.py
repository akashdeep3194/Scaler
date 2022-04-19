from re import A


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    a = int(input())

    if a == 0:
        ans = 0
    if a == 1:
        ans = 1
    b = 0
    c = 1

    for i in range(1, a):
        ans = b + c
        b = c
        c = ans
    print(ans)

    return 0


if __name__ == '__main__':
    main()
