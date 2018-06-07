#Pairwise sum
#Given two lists xs and ys, return a new list zs 
# where each element is the sum of the corresponding elements # in xs and ys, i.e. sum2([1, 2, 3], [10, 11, 12]) == [11, 13, 15]. You may assume that the lists are the same length.

def sum2(xs, ys):
    zs = [] # new list
    for i in range(0, len(xs)):
        zs.append(xs[i] + ys[i])
    return zs

def test(test_case_xs, test_case_ys, expected):
    actual = sum2(test_case_xs, test_case_ys)
    if actual == expected:
        print("Passed test for " + str(test_case_xs) + ", " + str(test_case_ys))
    else:
        print("Didn't pass test for " + str(test_case_xs) + ", " + str(test_case_ys))
        print("The result was " + str(actual) + " but it should have been " + str(expected))

test([], [], [])
test([1, 2], [3, 4], [4, 6])
test([-10, 10, 20], [10, -10, -20], [0, 0, 0])