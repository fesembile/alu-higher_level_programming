#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    func = 0
    for i in range(x):
        try:
           print("{}".format(my_list[i]), end="")
           func += 1
        except IndexError:
            break
    print("")
    return (func)
