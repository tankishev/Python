def reverse_array(nums: list, retval=None) -> None:
    if retval is None:
        retval = []
    if not nums:
        print(*retval, sep=' ')
        return

    retval.append(nums.pop())
    reverse_array(nums, retval)


nums = [int(el) for el in input().split()]

reverse_array(nums)
