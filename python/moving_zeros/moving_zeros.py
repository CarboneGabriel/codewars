def move_zeros(array):
    zeros = array.count(0)
    for i in range(zeros):
        array.remove(0)
        array.append(0)
    return array

input = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
print(move_zeros(input))



# test.assert_equals(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),[1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
# test.assert_equals(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),[9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# test.assert_equals(move_zeros([0, 0]), [0, 0])
# test.assert_equals(move_zeros([0]), [0])
# test.assert_equals(move_zeros([]), [])