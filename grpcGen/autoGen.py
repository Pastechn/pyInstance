
import os
import os.path

workDir = 'E:\\下载\\Xray-core-main'

os.chdir(workDir)
os.mkdir('proto')

class Logger():
    def __init__(self, messaege):
        self.message = messaege
    def info(self):
        print('[IF]', self.message)
    def error(self):
        print('[ER]', self.message)
    def ok(self):
        print('[OK]', self.message)

Logger.info(Logger('Searching files'))
# 遍历文件夹，寻找 proto 文件
allProtos = []
for root, dirs, files in os.walk('.'):
    for single in files:
        if single.endswith('.proto'):
            # 将文件名与相对目录拼接成完整的路径
            allProtos.append(os.path.join(root, single))

Logger.info(Logger('Generating components'))
# 逐一生成 py 文件
for single in allProtos:
    try:
        os.system('python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. ' + single)
        Logger.ok(Logger(single))
    except:
        Logger.error(Logger(single))

Logger.info(Logger('Searching generated components'))
# 遍历文件夹，寻找 py 文件
allPys = []
allDirs = set()
for root, dirs, files in os.walk('.'):
    for single in files:
        if single.endswith('.py'):
            # 将文件名与相对目录拼接成完整的路径
            allPys.append(os.path.join(root, single))
            # 将路径单独放入一个集合，便于生成文件夹结构
            allDirs.add(root)

Logger.info(Logger('Generating directories'))
# 生成文件夹
for single in allDirs:
    # 取出文件夹集合中的每个元素，并按照 \\ 劈分
    allLayers = single.split('\\')[1:]
    # 计算文件夹深度
    numLayers = len(allLayers)
    if numLayers == 0:
        continue
    current = '.\\proto'
    # 取出劈分后的单个元素，逐元素拼接，形成从外到里的文件夹结构
    for num in range(0, numLayers):
        current = current + '\\' + allLayers[num]
        # 创建文件夹，遇到重复或空元素则跳过
        try:
            os.mkdir(current)
            Logger.ok(Logger(current))
        except:
            Logger.error(Logger(current))

newPys = []
for single in allPys:
    srcList = single.split('\\')[1:]
    dstList = ['.', 'proto']
    dstList.extend(srcList)
    dstPath = '\\'.join(dstList)
    newPys.append(dstPath)

Logger.info(Logger('Cpoying files'))
numPys = len(newPys)
for num in range(0, numPys - 1):
    try:
        with open(allPys[num], 'r', encoding='utf-8') as srcFile:
            content = srcFile.read()
            with open(newPys[num], 'w', encoding='utf-8') as dstFile:
                dstFile.write(content)
                Logger.ok(Logger(newPys[num]))
    except:
        Logger.error(Logger(newPys[num]))
