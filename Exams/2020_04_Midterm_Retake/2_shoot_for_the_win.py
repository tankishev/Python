targets = list(map(int, input().split(' ')))

while True:
    input_line = input()
    if input_line == 'End':
        break

    i = int(input_line)
    if 0 <= i < len(targets):
        if targets[i] != -1:
            current_val = targets[i]
            for j, target in enumerate(targets):
                if i != j and target != -1:
                    if target > current_val:
                        targets[j] -= current_val
                    elif target <= current_val:
                        targets[j] += current_val
            targets[i] = -1

shot_targets = targets.count(-1)
print(f"Shot targets: {shot_targets} -> ", end='')
print(*targets, sep=' ')
