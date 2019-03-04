#credit card validation

c_num = input("enter your card #: ")


def cc_validation(card):
    list(card)
    c_list = []
    for n in card:
        c_list.append(int(n))
    last_num = c_list.pop(-1)
    c_list.reverse()
    for num in range(1,(len(c_list)),2):
        c_list[num] *= 2
    for num in range(len(c_list)):
        if c_list[num] > 9:
            c_list[num] -= 9
    for num in c_list:
            add =sum(c_list)
    if add % 10 == last_num:
        return True
    else:
        return False

print(cc_validation(c_num))