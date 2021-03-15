# gRPC API for Python

用于根据 `.proto` 自动生成 Python 适用的 gRPC 模块

## 需求

指定一个工作路径，自动遍历该路径下的所有 `.proto` 并编译生成 Python 适用的模块，且编译后仍保持 `.proto` 的文件结构

## 使用方法

1. 安装依赖 `pip3 install grpcio grpcio-tools`
2. 编辑脚本，将 `workDir` 修改为项目的根目录
3. 运行脚本
4. 生成的模块位于 `workDir/proto` 中

## 程序逻辑

1. 寻找 `.proto` 文件
2. 生成 `.py` 文件
3. 还原文件夹结构
4. 逐一复制文件

## 说明

在还原文件夹结构的步骤中，其实可以用 `os.makedirs()` 来自动递归创建文件夹。此处为了练习，并没有采用这个方法，而是将文件夹的层级拆分到一个列表中，再由外向内逐一使用 `os.mkdir()` 进行文件夹创建。在日志中可以看到，文件夹的创建是严格按顺序的，若文件夹已存在则交给 `except` 处理，日志中会显示 `[ER]` 类型的信息。

```
[IF] generating directories
[OK] .\proto\proxy
[OK] .\proto\proxy\http
[OK] .\proto\transport
[OK] .\proto\transport\internet
[OK] .\proto\transport\internet\tcp
[ER] .\proto\transport
[ER] .\proto\transport\internet
[OK] .\proto\transport\internet\headers
[OK] .\proto\transport\internet\headers\utp
```

日志部分原本使用了 `print()` 直接输出，现改为了使用 `Logger()` 实现（其实只是把原本的方法用面向对象的思维重写了）

此脚本的创建初衷是想要自己编写一个和 V2board 对接的控制器，并使用 Xray 内置的 API 来修改配置文件。而 Xray 内置 API 使用了 gRPC 标准，因此得先根据 `.proto` 文件编译出 Python 适用的模块。

理论上适用于任何项目的 `.proto` 自动编译。
