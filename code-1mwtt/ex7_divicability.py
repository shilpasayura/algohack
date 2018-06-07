#Divisibility
#Given a number n, 
#compute a list of all the integers x 
#divisible by 3 or 5 that are 0 <= x < n. 
#example, three_or_five(10) == [0, 3, 5, 6, 9].

def threes_or_fives(n):
    xs = []
    for x in range(0, n):
        if x % 3 == 0 or x % 5 == 0:
            xs.append(x)
    return xs

def test(test_case, expected):
    actual = threes_or_fives(test_case)
    if actual == expected:
        print("Passed test for " + str(test_case))
    else:
        print("Didn't pass test for " + str(test_case))
        print("The result was " + str(actual) + " but it should have been " + str(expected))

test(0, [])
test(3, [0])
test(5, [0, 3])
test(6, [0, 3, 5])
test(10, [0, 3, 5, 6, 9])