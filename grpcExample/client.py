
import grpc
import contact_pb2
import contact_pb2_grpc

def addRequest(address, port, token):
    # 连接 grpc 服务器
    channel = grpc.insecure_channel('localhost:8500')
    # 将打开的连接放入 AlterForwardStub 等待下一步的操作
    stub = contact_pb2_grpc.AlterForwardStub(channel)
    # AddFowrard(AddForwardRequest) 格式发送信息
    response = stub.AddForward(contact_pb2.AddForwardRequest(
        address = address,
        port = port,
        token = token
    ))
    print(response.message)

def removeRequest(address, port, token):
    channel = grpc.insecure_channel('localhost:8500')
    stub = contact_pb2_grpc.AlterForwardStub(channel)
    response = stub.RemoveForward(contact_pb2.RemoveForwardRequest(
        address = address,
        port = port,
        token = token
    ))
    print(response.message)

# 简易的客户端，没有进行异常处理
while True:
    choice = input('Operation[a/r]: ')
    if choice == 'a':
        a = input('Address: ')
        p = int(input('Port: '))
        t = input('Token: ')
        addRequest(a, p, t)
    elif choice == 'r':
        a = input('Address: ')
        p = int(input('Port: '))
        t = input('Token: ')
        removeRequest(a, p, t)
    else:
        print('Invalid input')
        continue
