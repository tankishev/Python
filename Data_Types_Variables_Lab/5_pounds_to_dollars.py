# Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.
# 1 British Pound = 1.31 Dollars.
# Examples
# Input	Output
# 80	104.800
# 39	51.090


GBP = int(input())
print("{:.3f}".format(GBP * 1.31))