
import re

excludeObject = []
# 打开列表文件
with open('whitelist.txt', 'r', encoding='utf-8') as exclude:
    rawExcludeObject = exclude.readlines()
# 使用正则表达式筛选出有效的 Mac 地址
for idx in range(0, len(rawExcludeObject)):
    currentLine = rawExcludeObject[idx]
    try:
        currentLine = re.match('[0-9,a-z]{2}:[0-9,a-z]{2}:[0-9,a-z]{2}:[0-9,a-z]{2}:[0-9,a-z]{2}:[0-9,a-z]{2}', currentLine).group(0)
    except:
        continue
    if len(currentLine) == 0:
        continue
    excludeObject.append(currentLine)

print(excludeObject)