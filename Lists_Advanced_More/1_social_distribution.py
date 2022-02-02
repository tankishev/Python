# A core idea of several left-wing ideologies is that the wealthiest should support the poorest, 
# no matter what, and that is exactly what you are called to do for this problem.
# 
# On the first line, you will be given the population (numbers separated by comma and space ", "). 
# On the second line, you will be given the minimum wealth. You should distribute the wealth so that no part of the population has less than the minimum wealth. 
# To do that, you should always take wealth from the wealthiest part of the population. 
# There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible". 


population_list = list(map(int, input().split(', ')))
min_wealth = int(input())

income_gap = sum([abs(x-min_wealth) for x in population_list if x < min_wealth])
distributable_wealth = sum([abs(x-min_wealth) for x in population_list if x > min_wealth])

if income_gap > distributable_wealth:
    print('No equal distribution possible')
else:
    while min(population_list) < min_wealth:
        wealth_transfer = min_wealth - min(population_list)
        population_list[population_list.index(min(population_list))] += wealth_transfer
        population_list[population_list.index(max(population_list))] -= wealth_transfer

    print(population_list)