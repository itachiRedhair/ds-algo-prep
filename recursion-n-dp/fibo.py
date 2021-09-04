# The total number of nodes in the tree will represent the runtime, since each call only does 0(1) work
# outside of its recursive calls. Therefore, the number of calls is the runtime.
# I Tip: Remember this for future problems. Drawing the recursive calls as a tree is a great way to
# figure out the runtime of a recursive algorithm.
# How many nodes are in the tree? Until we get down to the base cases (leaves), each node has two children.
# Each node branches out twice.

# The root node has two children. Each of those children has two children (so four children total in the"grand-
# children" level). Each of those grandchildren has two children, and so on. If we do this n times, we'll have

# roughly O( 2") nodes. This gives us a runtime of roughly 0( 2").

def fibo_recursive(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibo_recursive(n) + fibo_recursive(n-1)


def fibo_dp(n):
    def fibo(n, memo_list):
        if n == 0:
            return 0

        if n == 1:
            return 1

        if memo_list[n] == 0:
            memo_list[n] = fibo(n-1, memo_list) + fibo(n-2, memo_list)

        return memo_list[n]
    fibo(n, [0]*n)


def fibonacci_bottoms_up_dp(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    a = 0
    b = 1

    for i in range(2, n):
        c = a+b
        a = b
        b = c

    return a + b
