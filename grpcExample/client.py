
import grpc
import contact_pb2
import contact_pb2_grpc

serverAddress = input('Server address and port: ')

def addRequest(stub, address, port, token):
    # AddFowrard(AddForwardRequest) 格式发送信息
    response = stub.AddForward(contact_pb2.AddForwardRequest(
        address = address,
        port = port,
        token = token
    ))
    print(response.message)

def removeRequest(stub, address, port, token):
    response = stub.RemoveForward(contact_pb2.RemoveForwardRequest(
        address = address,
        port = port,
        token = token
    ))
    print(response.message)

# 简易的客户端，没有进行异常处理
# 连接服务端
serverConnection = grpc.insecure_channel(serverAddress)
# 将打开的连接放入 AlterForwardStub 等待下一步的操作
s = contact_pb2_grpc.AlterForwardStub(serverConnection)
while True:
    choice = input('Operation[a/r]: ')
    if choice == 'a':
        a = input('Address: ')
        p = int(input('Port: '))
        t = input('Token: ')
        addRequest(s, a, p, t)
    elif choice == 'r':
        a = input('Address: ')
        p = int(input('Port: '))
        t = input('Token: ')
        removeRequest(s, a, p, t)
    else:
        print('Invalid input')
        continue
