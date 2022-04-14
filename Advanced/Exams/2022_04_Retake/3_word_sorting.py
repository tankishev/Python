def words_sorting(*args):
    word_dict = {}
    for word in args:
        if word not in word_dict:
            word_dict[word] = 0
        ascii_sum = sum(ord(el) for el in word)
        word_dict[word] += ascii_sum
    sum_of_values = sum(el for el in word_dict.values())
    if sum_of_values % 2 == 0:
        sorted_dict = [item for item in sorted(word_dict.items(), key=lambda item: item[0])]
    else:
        sorted_dict = [item for item in sorted(word_dict.items(), key=lambda item: -item[1])]

    retdict = []
    for item in sorted_dict:
        key, value = item[0], item[1]
        retdict.append(f"{key} - {value}")

    return '\n'.join([el for el in retdict])

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))


