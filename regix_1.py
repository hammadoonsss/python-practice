# Remove Specific Chahracter from String
s="Hello, World:"

import re
st = re.sub("[:,]", "",s)
print("s", s)
print("st", st)
