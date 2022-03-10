def possible_permutations(start_list: list) -> iter:

    def gen_list(get_list=None, tmp_list=None, depth=0):
        nonlocal start_list
        nonlocal ret_list

        if not tmp_list:
            tmp_list = ['' for _ in range(len(start_list))]

        if not get_list and depth == 0:
            work_list = start_list.copy()
        else:
            work_list = get_list.copy()

        while work_list:
            tmp_list[depth] = work_list.pop()
            pass_list = [el for el in start_list if el not in tmp_list[:depth+1]]
            gen_list(pass_list, tmp_list, depth + 1)
        else:
            if tmp_list not in ret_list:
                ret_list.append([x for x in tmp_list])

    start_list.reverse()
    ret_list = []
    gen_list()

    for item in ret_list:
        yield item


if __name__ == '__main__':
    [print(n) for n in possible_permutations([1, 2, 3])]
