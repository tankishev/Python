def crunch(word_elements, target, output, component=None):
    if component is None:
        component = []
    if not target:
        output.add(' '.join([x for x in component]))

    for el in word_elements:
        if target[:len(el)] == el and word_elements.get(el) > 0:
            word_elements[el] -= 1
            new_component = [e for e in component]
            new_component.append(el)
            new_target = target[len(el):]
            crunch(word_elements, new_target, output, new_component)
            word_elements[el] += 1


def solution():
    data = [el for el in input().split(', ')]
    target = input()

    word_elements = {}
    for el in data:
        if el not in word_elements:
            word_elements[el] = 0
        word_elements[el] += 1

    output = set()
    crunch(word_elements, target, output)
    print(*sorted(list(output)), sep='\n')


if __name__ == '__main__':
    solution()
