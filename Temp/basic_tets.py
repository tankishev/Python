def swap(string):
    start = string[0]
    end = string[-1]
    swapped = end + string[1:-1] + start
    return (swapped)


message = input ().split(' ')
number = 0
word = []
chr_ord = []
swap_letters = ''

for i in range(int(len(message))):
    chr_ord = list(message[i])
    if (int(chr_ord[0])) > 6:
      number += 10*int(int(chr_ord[0]))
      number += int (int(chr_ord[1]))
      word.append(chr(number))
      number = 0
      chr_ord.pop(0)
      chr_ord.pop(0)
      swap_letters = (''.join(chr_ord))
      if len(swap_letters) >= 2:
       swap_letters = swap (swap_letters)
       word.extend(swap_letters)
      else: word.extend(swap_letters)
      print (''.join(word), end = " ")
      word.clear()
      swap_letters = ''

    else:
      number += 100*int(int(chr_ord[0]))
      number += 10 * int(int(chr_ord[1]))
      number += int (int(chr_ord[2]))
      word.append(chr(number))
      number = 0
      chr_ord.pop(0)
      chr_ord.pop(0)
      chr_ord.pop(0)
      swap_letters = (''.join(chr_ord))
      if len(swap_letters) >= 2:
       swap_letters = swap (swap_letters)
       word.extend(swap_letters)
      else: word.extend (swap_letters)
      print (''.join(word), end = " ")
      word.clear()
      swap_letters = ''