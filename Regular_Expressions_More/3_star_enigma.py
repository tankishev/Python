# The war is in its peak, but you, young Padawan, can turn the tides with your programming skills. 
# You are tasked to create a program to decrypt the messages of The Order and prevent the death of hundreds of lives. 
# You will receive several messages, which are encrypted using the legendary star enigma. You should decrypt the messages, following these rules:
# 
# To properly decrypt a message, you should count all the letters [s, t, a, r] – case insensitive and remove the count from the current ASCII value of each symbol of the encrypted message.
# 
# After decryption:
# Each message should have a planet name, population, attack type ('A', as attack or 'D', as destruction) and soldier count.
# The planet name starts after '@' and contains only letters from the Latin alphabet. 
# The planet population starts after ':' and is an Integer;
# The attack type may be "A"(attack) or "D"(destruction) and must be surrounded by "!" (exclamation mark).
# The soldier count starts after "->" and should be an Integer.
# The order in the message should be: planet name -> planet population -> attack type -> soldier count. Each part can be separated from the others by any character except: '@', '-', '!', ':' and '>'.
# Input / Constraints
# •	The first line holds n – the number of messages– integer in range [1…100];
# •	On the next n lines, you will be receiving encrypted messages.
# Output
# After decrypting all messages, you should print the decrypted information in the following format:
# First print the attacked planets, then the destroyed planets.
# "Attacked planets: {attackedPlanetsCount}"
# "-> {planetName}"
# "Destroyed planets: {destroyedPlanetsCount}"
# "-> {planetName}"
# The planets should be ordered by name alphabetically.

import re

message_parser = re.compile(r'(?<=@)([a-zA-Z]+)(?:[^\@\!\:\>\-]+)?(?::(\d+))(?:[^\@\!\:\>\-]+)?!(A|D)!(?:[^\@\!\:\>\-]+)?->(\d+)')

def decrypt(message):
    decrypt_symbols = r'[starSTAR]'
    decrypt_matches = re.findall(decrypt_symbols, message)
    key = len(decrypt_matches)
    return ''.join([chr(ord(x) - key) for x in message])

planets_attacked = []
planets_destroyed = []

number_of_messages = int(input())

for _ in range(number_of_messages):
    encrypted_message = input()
    decrypted_message = decrypt(encrypted_message)

    parsed_message = message_parser.search(decrypted_message)
    if parsed_message:
        attack_result = parsed_message.group(3)
        planet_name = parsed_message.group(1)
        if attack_result == 'A':
            planets_attacked.append(planet_name)
        elif attack_result == 'D':
            planets_destroyed.append(planet_name)

planet_count = len(planets_attacked)
print(f'Attacked planets: {planet_count}')
if planet_count > 0:
    planets_attacked.sort()
    for planet in planets_attacked:
        print(f'-> {planet}')

planet_count = len(planets_destroyed)
print(f'Destroyed planets: {planet_count}')
if planet_count > 0:
    planets_destroyed.sort()
    for planet in planets_destroyed:
        print(f'-> {planet}')