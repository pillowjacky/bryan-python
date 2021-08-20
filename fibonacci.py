def in_loop(count):
    n1 = 0
    n2 = 1
    print(f'{n1} {n2}', end=" ")
    for _ in range(count - 2):
        n3 = n1 + n2
        print(n3, end=" ")
        n1 = n2
        n2 = n3


def in_recursion(count):
    n1 = 0
    n2 = 1
    print(f'{n1} {n2}', end=" ")
    __in_recursion(count - 2, n1, n2)


def __in_recursion(count, n1, n2):
    if count > 0:
        n3 = n1 + n2
        print(n3, end=" ")
        n1 = n2
        n2 = n3
        return __in_recursion(count - 1, n1, n2)


if __name__ == '__main__':
    in_loop(12)
    print()
    in_recursion(12)
