import Tools
from pathlib import Path

# print(Tools.add(23,43) )
# print(Tools.multiply(45,3))
# print(Tools.hello(input("Enter your name : ")))

# Path = Path('我的汉语演讲.txt')
# content = Path.read_text()
# content = content.rstrip()
# content = content.splitlines()
# print(content)

ask = Path('Output.txt')
for p in range (1,4):
    p = (input("Enter a sentence"))
    ask.write_text(p + "\n")
    
read = Path('Output.txt')
content = read.read_text()
print(content)