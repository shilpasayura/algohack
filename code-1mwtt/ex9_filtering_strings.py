#Filtering a list of strings
#Given a list of strings, return a copy of the list that only #includes the strings that start with an lowercase letter.

def filtered_text(xs):
    # Return a copy of xs that only contains the strings that # starts with a lowercase letter
    ys = []
    for x in xs:
        if "a" <= x[0] and "z" >= x[0]:
            ys.append(x)
    return ys

def test(test_case, expected):
    actual = filtered_text(test_case)
    if actual == expected:
        print("Passed test for " + str(test_case))
    else:
        print("Didn't pass test for " + str(test_case))
        print("The result was " + str(actual) + " but it should have been " + str(expected))

test([], [])
test(["Learn", "to", "Code"], ["to"])
test(["Oxford", "University", "Computer", "Society"], [])
test(["learn", "to", "code"], ["learn", "to", "code"])