# You are given a secret message you should decipher. To do that, you need to know that in each word:
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)


def last_num_index(word_: str) -> int:
    """
    :param word_:
    :return: int; the index of the last numeric character reading the word ltr
    """
    numbers = '0123456789'
    return max(i for i in range(len(word_)) if word_[i] in numbers)


word_list = input().split(' ')
output_list = []

for word in word_list:
    num = word[:last_num_index(word) + 1]
    first_char = chr(int(num))
    new_word = first_char + word[len(num):]
    if len(new_word) > 2:
        new_word = new_word[0:1] + new_word[-1] + new_word[2:-1] + new_word[1]
    
    output_list.append(new_word)

print(' '.join(output_list))
