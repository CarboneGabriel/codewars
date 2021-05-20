def find_nb(m):
    vol = 0
    n = 0
    while vol < m:
        vol += n**3
        n += 1
        if (vol > m):
            return -1
    return n-1

input = 4183059834009

print(find_nb(input))


# n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n
# test.assert_equals(find_nb(4183059834009), 2022)
# test.assert_equals(find_nb(24723578342962), -1)
# test.assert_equals(find_nb(135440716410000), 4824)
# test.assert_equals(find_nb(40539911473216), 3568)
# test.assert_equals(find_nb(26825883955641), 3218)