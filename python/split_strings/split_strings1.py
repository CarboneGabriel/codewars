import re
#utilizo expresiones regulares
def solution(s):    
    return re.findall(".{2}", s + "_")

# re.findall(pattern, string, flags=0)
# busca el patron ".{2}" en la cadena "s" a la cual se agrega "_"
# y devuelve todos los números agrupados de a 2 en un arrays

input = "asdfads"
print(solution(input))


# test.describe("Example Tests")
# tests = (
#     ("asdfadsf", ['as', 'df', 'ad', 'sf']),
#     ("asdfads", ['as', 'df', 'ad', 's_']),
#     ("", []),
#     ("x", ["x_"]),
# )