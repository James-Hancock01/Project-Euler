import re

regex = re.compile(r'(.+ .+)( \1)+')
match = regex.search('305515168')
print(match.group(1))
