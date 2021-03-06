def merge(xs, ys):
    # return a sorted list with the merged contents of the sorted lists xs and ys
    i = 0
    j = 0
    zs = []
    while not (i == len(xs) or j == len(ys)):
        if xs[i] < ys[j]:
            zs.append(xs[i])
            i = i + 1
        else:
            zs.append(ys[j])
            j = j + 1
    while i != len(xs):
        zs.append(xs[i])
        i = i + 1
    while j != len(ys):
        zs.append(ys[j])
        j = j + 1
    return zs
    
def merge_sort(xs):
    # sort xs
    if len(xs) <= 1:
        return xs
    else:
        first_half = xs[:(len(xs) // 2)]
        first_half_sorted = merge_sort(first_half)
        second_half = xs[(len(xs) // 2):]
        second_half_sorted = merge_sort(second_half)
        return merge(first_half_sorted, second_half_sorted)

def test(test_case_xs, expected):
    actual = merge_sort(test_case_xs)
    if actual == expected:
        print("Passed test for " + str(test_case_xs))
    else:
        print("Didn't pass test for " + str(test_case_xs))
        print("The result was " + str(actual) + " but it should have been " + str(expected))
        
test([], [])
test([0], [0])
test([1, 2], [1, 2])
test([2, 1], [1, 2])
test([4, 3, 2, 1], [1, 2, 3, 4])
test([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8])
test([8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8])
test([8, 7, 6, 5, 4, 3, 2, 1, 10, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])