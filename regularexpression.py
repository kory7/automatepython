import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search("My number is 776-890-12324")
print("Your phone number is " + mo.group())
