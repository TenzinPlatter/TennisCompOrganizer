import sys
import re

r = open(sys.argv[1], "r")
f = open("new.txt", "w")
insideBracketsPattern = r'\((.*?)\)'
leadingWhitespacePattern = r'^\s*'
for line in r.readlines():
    leadingWhitespace = re.search(leadingWhitespacePattern, line)
    if "raise" in line:
        insideBrackets = re.findall(insideBracketsPattern, line)[0]
        newLine = f"{leadingWhitespace.group()}print({insideBrackets})\n{leadingWhitespace.group()}exit()\n"
    else:
        newLine = line
    f.write(newLine)
r.close()
f.close()

