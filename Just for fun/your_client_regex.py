import re


def autocorrect(input_str: str) -> str:
    pattern = r'\b(youu*)\b|\b(u)\b'
    replace_str = 'your client'
    retval = ''

    matches = re.finditer(pattern, input_str, flags=re.IGNORECASE)
    if not matches:
        return input_str

    i = 0
    for match in matches:
        retval += input_str[i:match.span()[0]] + replace_str
        i = match.span()[1]

    if i < len(input_str) - 1:
        retval += input_str[i:]

    return retval


print(autocorrect(input()))
