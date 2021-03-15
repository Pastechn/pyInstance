# gRPC Example

用于建立服务器与客户端之间基于 gRPC 的通信

## 需求

客户端发送请求，服务端完成请求并返回操作状态

## 使用方法

1. 安装依赖 `pip3 install grpcio grpcio-tools`
2. 运行服务端 `server.py`
3. 运行客户端 `client.py` 并按照提示操作

## 程序逻辑

### 服务端

1. 根据 `.proto` 文件编写服务端
2. 启动 gRPC 服务端

### 客户端

1. 连接服务端
2. 根据 `.proto` 文件发送请求

## 说明

本实例参考自[简书]("https://www.jianshu.com/p/43fdfeb105ff?from=timeline&isappinstalled=0")，甚至可以说是直接照搬。

本意是写一个 gRPC 通信的端口转发配置服务，其实已经完成得差不多了，如果有心的话直接在 `AlterForward()` 和 `RemoveForward()` 中加入IPtables代码就基本可以操作了，不过离完善还有很长的一段距离，得验证端口占用情况，以及转发的重复情况，等等。
