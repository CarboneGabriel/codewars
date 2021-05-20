def is_valid_walk(walk):
    pos = [0,0]
    min = 0
    for i in range(len(walk)):
        if (walk[i] == "n"): pos[1] += 1
        elif (walk[i] == "s"): pos[1] -= 1
        elif (walk[i] == "e"): pos[0] += 1
        elif (walk[i] == "w"): pos[0] -= 1
        print(pos)
        min += 1
        print(min)
    if (min == 10 and pos == [0,0]):
        return True
    else: return False 

input = ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's']
print(is_valid_walk(input))




# test.expect(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True');
# test.expect(not is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False');
# test.expect(not is_valid_walk(['w']), 'should return False');
# test.expect(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False');