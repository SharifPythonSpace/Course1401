import re

# Match strings starting with "The"
regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
for string in strings:
	if re.match(regex, string):
		print(f'Matched: {string}')
	else:
		print(f'Not matched: {string}')
