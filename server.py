import socket
import threading


class ChatServer:
    clients_list = []  # 全体客户端列表
    last_received_message = ""  # 接收的最新信息

    #初始化操作
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_listen()

    #服务器开始监听
    def server_listen(self):
          # 创建套接字
        local_ip = "192.168.43.18"
        local_port = 10319
        # 此处为socket设置选项，参数"1",表示将SO_REUSEADDR标记为TRUE，操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口，
        # 否则操作系统会保留几分钟该端口。
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((local_ip, local_port))  # 绑定ip与端口
        print("Listening...")
        self.server_socket.listen(5)  # 允许有多少个连接在队列中等待，一般设置为5。
        self.receive()
        #self.rthread = threading.Thread(target=self.receive)
        #self.rthread.setDaemon(True)
        #self.rthread.start()

    #服务器端接受客户端发送数据函数
    def receive_messages(self, so, client):
        while True:
            try:
                buffer = so.recv(1024)
            except:
                print()
                break
            if not buffer:
                break
            self.last_received_message = buffer.decode('utf-8')
            print(self.last_received_message)
            self.broadcast()
        so.close()

    # 将消息广播给所有客户端
    def broadcast(self):
        for client in self.clients_list:
            socket, (ip, port) = client
            socket.send(self.last_received_message.encode('utf-8'))

    #服务器端接受客户端申请函数
    def receive(self):
        while True:
            client = so, (ip, port) = self.server_socket.accept()
            print(client)
            if client not in self.clients_list:
                self.clients_list.append(client)
            print('There is a connection request from', ip, ':', str(port))
            # 利用多线程，可同时处理多个客户端请求
            t = threading.Thread(target=self.receive_messages, args=(so, client))
            t.start()


if __name__ == "__main__":
    ChatServer()
