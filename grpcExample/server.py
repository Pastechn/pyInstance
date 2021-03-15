
import contact_pb2
import contact_pb2_grpc
import grpc
import time
from concurrent import futures

# 定义服务端接受的方法，其实就是把 proto 文件中服务器对应的内容翻译一遍
# ====================
# service  -->  class
# grpc     -->  def
# returns  -->  return
# ====================
# 以下开始翻译
# service AlterForward {}
class AlterForward(contact_pb2_grpc.AlterForwardServicer):
    # rpc AddForward(AddForwardRequest)
    def AddForward(self, request, context):
        print(time.strftime("%H:%M:%S", time.localtime()) + ' [IF] add forward: {0}:{1}, from {2}'.format(request.address, str(request.port), request.token))
        # returns (AddForwardResponse)
        return contact_pb2.AddForwardResponse(
            # string message = 1;
            message = 'Add: {0}:{1}, from {2}'.format(request.address, str(request.port), request.token)
        )
    # rpc RemoveForward(RemoveForwardRequest)
    def RemoveForward(self,request,context):
        print(time.strftime("%H:%M:%S", time.localtime()) + ' [IF] remove forward: {0}:{1}, from {2}'.format(request.address, str(request.port), request.token))
        # returns (RemoveForwardResponse)
        return contact_pb2.RemoveForwardResponse(
            # string message = 1;
            message = 'Remove: {0}:{1}, from {2}'.format(request.address, str(request.port), request.token)
        )

def grpcServer():
    # 利用 futurs 创建一个 grpc 服务器对象，最大线程为 5
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    # 将刚才翻译形成的 class 对象，利用 add_AlterForwardServicer_to_server 方法绑定到 grpc 服务器上
    # 使得 AlterForward() 可以正常接收内容并产生回复
    contact_pb2_grpc.add_AlterForwardServicer_to_server(AlterForward(), server)
    # 定义 grpc 服务器地址与端口
    server.add_insecure_port('[::]:8500')
    # 启动服务器
    server.start()
    print(time.strftime("%H:%M:%S", time.localtime()) + ' [IF] Start listening 8500')
    server.wait_for_termination()

# 启动 grpc 服务器
try:
    grpcServer()
except:
    print(time.strftime("%H:%M:%S", time.localtime()) + ' [IF] Server exits')