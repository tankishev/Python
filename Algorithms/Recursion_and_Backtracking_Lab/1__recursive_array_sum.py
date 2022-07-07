nums = [int(x) for x in input().split()]


def recursive_sum(numarr):
    if not numarr:
        return 0
    return numarr.pop() + recursive_sum(numarr)


print(recursive_sum(nums))
