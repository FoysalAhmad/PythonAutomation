"""def isPhoneNumber(text):
	if len(text) != 12:
		return False;

	for i in range(0,3):
		if not text[i].isdigit():
			return False

	if text[3] != '-':
		return False

	for i in range(4,7):
		if not text[i].isdigit():
			return False

	if text[7] != '-':
		return False

	for i in range(8,12):
		if not text[i].isdigit():
			return False
	return True"""

import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999'

phoneNumRex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRex.findall(message)

print(mo)

"""foundNumber = False
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print('phone number found: '+chunk)
		foundNumber = True
if not foundNumber:
	print('Could not find any phone number!')


print(isPhoneNumber('336-615-4419'))
print (isPhoneNumber('hello'))"""