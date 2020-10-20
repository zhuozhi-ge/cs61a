HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def num_sevens(x):
    """Returns the number of times 7 appears as a digit of x.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    """
    "*** YOUR CODE HERE ***"
    if x < 10:
        if x == 7:
            return 1
        else:
            return 0
    return num_sevens(x // 10) + num_sevens(x % 10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
#     ans = 0
#     adder = -1
#     for i in range(1, n+1):
#         if (i-1) % 7 == 0 or num_sevens(i-1) != 0:
#             adder *= -1 
#         ans += adder
#     return ans
    def helper(i, adder, ans):
        if i == n+1:
            return ans
        if (i-1) % 7 == 0 or num_sevens(i-1) != 0:
            return helper(i+1, adder*(-1), ans+adder*(-1))
        else:
            return helper(i+1, adder, ans+adder)
    return helper(1, -1, 0)

def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    import math
    temp = 2**int(math.log(total, 2))
    def helper(n, m):
        if n == 0:
            return 1
        if m == 1:
            return 1
        if n < m:
            return helper(n, m / 2)
        return helper(n - m, m) + helper(n, m / 2)
    return helper(total, temp)

def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    """
    "*** YOUR CODE HERE ***"
    if n // 10 == 0:
        return 0
    if n // 100 == 0:
        if n % 10 == n // 10:
            return n % 10 - n // 10
        else:
            return n % 10 - n // 10 - 1
    return missing_digits(n // 10) + missing_digits(n % 100)


###################
# Extra Questions #
###################

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    nums = [1, 2, 3]
    nums.remove(start)
    nums.remove(end)
    other = nums[0]
    if n == 1:
        print_move(start, end)
        return
    move_stack(n-1, start, other),
    move_stack(1, start, end)
    move_stack(n-1, other, end)

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    fact1 = lambda f, n1: 1 if n1 == 0 else mul(n1,  f(f, sub(n1, 1)))
    return lambda n: fact1(fact1, n)