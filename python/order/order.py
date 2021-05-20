def order(sentence):
    words = sentence.split(" ")
    output = []
    for i in range(10):
        for j in range(len(words)):
            if (words[j].find(str(i)) != -1):
                output += words[j]     
    return output.join(" ")

input = "4of Fo1r pe6ople g3ood th5e the2"

print(order(input))


# test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
# test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
# test.assert_equals(order(""), "")