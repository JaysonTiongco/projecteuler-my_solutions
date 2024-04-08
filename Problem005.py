# Problem 5 - Smallest Multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from timer import timed


@timed
def problem_005() -> int:
    num = 2520

    while True:
        num += 2520
        print(num)
        for i in range(11, 20):
            print(f"{num} % {i} = {num%i}")
            if num % i != 0:
                break
        else:
            break

    return num


if __name__ == '__main__':
    print(f"answer: {problem_005()}")
