# The lottery is exciting. However, checking a million tickets for winnings only by hand is not. 
# So, you are given the task of creating a program that automatically checks if a ticket is a winner.
# 
# You are given a collection of tickets separated by commas and spaces (one or many). 
# 
# You need to check each ticket to see if it has a winning combination of symbols:
# •	A valid ticket has exactly 20 characters.
# •	A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' uninterruptedly repeated at least 6 times in both halves of the tickets.
# •	In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides
# 
# An example of a valid winning ticket:
# "Cash$$$$$$Ca$$$$$$sh"
# An example of a Jackpot winning valid ticket:
# "$$$$$$$$$$$$$$$$$$$$"
# 
# Input
# The input will be read from the console. The input consists of a single line containing all tickets separated by commas and one or more white spaces in the format:
# •	"{ticket}, {ticket}, … {ticket}"
# 
# Output
# 
# Print the result for every ticket in the order of their appearance, each on a separate line in the format:
# •	If the ticket is invalid: "invalid ticket"
# •	If the ticket is valid, but it is not winning: "ticket "{ticket}" - no match"
# •	If the ticket is valid and winning, but not a Jackpot: 
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}"
# •	It the ticket hits the Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!"
# 
# Constrains
# •	Number of tickets will be in range [0 … 100]

win_symbols = ('@', '#', '$', '^')
win_patterns = [x * 6 for x in win_symbols]
find_pattern = lambda x: next(filter(lambda y: y in x,win_patterns),None)

tickets_list = input().split(',')
tickets_list = [ticket.strip() for ticket in tickets_list if ticket.strip() != '']

for ticket in tickets_list:
    if len(ticket) != 20:
        print('invalid ticket')
    else:
        pattern_found = find_pattern(ticket[:10])      
        if pattern_found and (pattern_found in ticket[10:]): #winning ticket 
            pattern_char = pattern_found[0]

            if ticket == pattern_char * 20: #Jacpot ticket
                print(f'ticket "{ticket}" - 10{pattern_char} Jackpot!')
            
            else: #regular winnig ticket
                for i in range(10,5,-1):
                    if (pattern_char * i in ticket[:10]) and (pattern_char * i in ticket[10:]):
                        print(f'ticket "{ticket}" - {i}{pattern_char}')
                        break
        else: #valid but not winning
            print(f'ticket "{ticket}" - no match')

