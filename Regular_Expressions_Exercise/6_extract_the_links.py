# Write a program that extracts links from a given text. The text will come in the form of strings, each representing a sentence. You need to extract only the valid links from it. Example:

# "www.internet.com"

#                       Sub-Domain			 Domain name		        Domain extension
# The Sub-Domain must always be "www". The Domain name can consist of English alphabet letters (uppercase and lowercase), digits, and dashes ("–"). 
# The Domain extension consists of one or more domain blocks, a domain block consists of a dot followed by one or more lowercase English alphabet letters, 
# a Domain extension must have at least one domain block in order to be valid. The Sub-Domain and Domain name must be separated by a single dot. 
# Any link that does NOT follow the specified above rules should be treated as invalid.
# Example incorrect links:  
# •	"ww.justASite.bg"
# •	"lel.awesome.com"
# •	"www.weird_site.hit.bg"
# •	"www.no-symb#^ols-allow%ed.com"
# •	"www.mark.12"
# •	"www.web-site."
# •	"www.example-site._*^#"
# Example of correct links:  
# •	"Some textwww.softuni.bg"
# •	"Just a link in a www.sea-of-text.bg-swimming around"
# •	"Instruments www.Instruments.rom.com.trombone2000 Instrument here"
# •	"All your ice cream flavors-www.scream.for.ice.cream(We  also have squirrels)"
#  The output is all valid links you have found, printed – each on a new line.

import re

search_pattern = re.compile(r'www.[a-zA-Z0-9-]+(\.[a-z]+)+')

while True:
    input_text = input()
    if len(input_text) == 0:
        break
    matches = search_pattern.finditer(input_text)
    for match in matches:
        print(match.group(0))
