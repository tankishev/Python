food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())

for i in range(1,31):
    food -= 0.300
    if i % 2 == 0:
        hay -= food * 0.05
    if i % 3 == 0:
        cover -= weight / 3

if min(food, hay, cover) > 0.001:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")
