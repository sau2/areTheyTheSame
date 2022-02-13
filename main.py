"""
Are they the "same"
https://www.codewars.com/kata/550498447451fbbd7600041c/python
Given two arrays a and b write a function comp(a, b) (or compSame(a, b)) that checks whether the two arrays have
the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears).
"Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144,
361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
...
"""


def compSame0(a=[121, 144, 19, 161, 19, 144, 19, 11], b=[121, 14641, 20736, 361, 25921, 361, 20736, 361]):
    # print('')
    # print('bool(b)',bool(b))
    # print('not(a and b)',not(a and b))
    # if not bool(b):
    #     return False
    # if not(a and b):
    #     return True
    if b == [] and a == []:
        return True
    if not a or not b:
        return False
    return set(b) == set(n ** 2 for n in a)
    # return not bool(set(b) - set(n ** 2 for n in a))
    # return list(set(b) - (set(n ** 2 for n in a)))


def compSame1(a=[121, 144, 19, 161, 19, 144, 19, 11], b=[121, 14641, 20736, 361, 25921, 361, 20736, 361]):
    if a is None or b is None:
        return False
    if b == [] and a == []:
        return True
    # if not a or not b:
    #     return False
    return set(b) == set(n ** 2 for n in a)


def compSame(a=[121, 144, 19, 161, 19, 144, 19, 11], b=[121, 14641, 20736, 361, 25921, 361, 20736, 361]):
    return False if a is None or b is None else sorted(b) == sorted(n ** 2 for n in a)

if __name__ == '__main__':
    print(compSame([1], [1]))
    print(compSame([0], [0]))
    print(compSame(None, None))
    print(compSame(None, [132, 14641, 20736, 361, 25921, 361, 20736, 361]))
    print(compSame([], []))
    print(compSame([], [132, 14641, 20736, 361, 25921, 361, 20736, 361]))
    print(compSame([121, 144, 19, 161, 19, 144, 19, 11], []))
    print(compSame([121, 144, 19, 161, 19, 144, 19, 11],
                   [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]))
    print(compSame([0, 121, 144, 19, 161, 19, 144, 19, 11],
                   [0, 11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]))
    print(compSame([1, 121, 144, 19, 161, 19, 144, 19, 11],
                   [1, 11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]))
    print(compSame())
    print(compSame([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]))
    print(compSame([1, 121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]))
    print(compSame([121, 144, 19, 161, 19, 144, 19, 11],
                   [1, 11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]))
    # print(compSame([], [132, 14641, 20736, 361, 25921, 361, 20736, 361]))
    # print(compSame(None, [132, 14641, 20736, 361, 25921, 361, 20736, 361]))

    # import timeit
    # print(min(timeit.repeat(stmt=compSame, number=10, repeat=5)))  # 0.0007859000000001171
