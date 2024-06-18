import re
text = "fasdfas(hello)dsf asdf"
pattern = r"\((.*?)\)"
new = re.findall(pattern, text)
print(new)
