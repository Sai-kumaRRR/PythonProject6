my_dict = {'b': 2, 'a': 5, 'c': 6}
for k, v in my_dict.items():
    if k == 'b':
        print("b is found!")
        op = 'b' in my_dict
        op2 = 'd' in my_dict
        print(op)
        print(op2)
        my_dict2 = {True: 123}
        print(my_dict2)
        print(type(my_dict2))
        print(my_dict2(True))
