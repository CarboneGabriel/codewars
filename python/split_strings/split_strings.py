def solution(s):
    output = []
    if (len(s)%2 == 1):
        s = s + "_"
    for x in range(0, len(s), 2):
     output.append(s[x:(x+2)])
    return output

input = "asdfadsf"
print(solution(input))


# test.describe("Example Tests")
# tests = (
#     ("asdfadsf", ['as', 'df', 'ad', 'sf']),
#     ("asdfads", ['as', 'df', 'ad', 's_']),
#     ("", []),
#     ("x", ["x_"]),
# )