import re

emailRegex = r"[-_\w\.]{0,64}@[-\w]{1,63}\.*[-\w]{1,63}"

print(re.findall(emailRegex, "742363155@q.com"))