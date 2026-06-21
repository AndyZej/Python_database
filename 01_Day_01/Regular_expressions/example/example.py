import re
line = "Luke, I am your father!"
result = re.search(r'your', line)
print(result)
print(result.group())

print()
line = """Millenium Falcon
X-Wing
VCX-100"""

result = re.search(r'\w+con', line)
print(result.group(0))

result = re.search(r'\w-\w+', line)
print(result.group(0))

result = re.findall(r'\d', line)
print(result)