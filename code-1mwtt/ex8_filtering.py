#Filtering a list
#Given a list of numbers, return a copy of the list that only #includes the even numbers.

def filtered_even(xs):
    # Return a copy of the list that only includes even number
    ys = []
    for x in xs:
        if x % 2 == 0:
            ys.append(x)
    return ys

def test(test_case, expected):
    actual = filtered_even(test_case)
    if actual == expected:
        print("Passed test for " + str(test_case))
    else:
        print("Didn't pass test for " + str(test_case))
        print("The result was " + str(actual) + " but it should have been " + str(expected))

test([], [])
test([0], [0])
test([0, 2, 3], [0, 2])
test([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [10, 8, 6, 4, 2, 0])