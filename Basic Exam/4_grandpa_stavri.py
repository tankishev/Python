quantity = []
quality = []

for _ in range(int(input())):
    quantity.append(float(input()))
    quality.append(float(input()))

total_quantity = sum(quantity)
avg_quality = sum([x * y for x, y in zip(quality,quantity)]) / total_quantity

print(f'Liter: {total_quantity:.2f}')
print(f'Degrees: {avg_quality:.2f}')
if avg_quality < 38:
    print('Not good, you should baking!')
elif avg_quality > 42:
    print('Dilution with distilled water!')
else:
    print('Super!')
