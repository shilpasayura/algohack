#Sorting lists
#sort a list into ascending order. 

def uniques(xs):
    # return a list of all the unique elements
    ys = sorted(xs) #sort
    zs = []
    for i in range(0, len(ys)):
        if i == 0 or ys[i] != ys[i - 1]:
            zs.append(ys[i])
    return zs
def test(test_case, expected):
    actual = uniques(test_case)
    if actual == expected:
        print("Passed test for " + str(test_case))
    else:
        print("Didn't pass test for " + str(test_case))
        print("The result was " + str(actual) + " but it should have been " + str(expected))

test([], [])
test([0, 0, 0, 1], [0, 1])
test([1, 4, 5, 1, 5, 4], [1, 4, 5])
test([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
test([10, 10, 9, 9, 8, 7, 6, 5, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])