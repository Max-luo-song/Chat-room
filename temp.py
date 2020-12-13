import socket
import threading


class ChatServer:
    clients_list = []  # 全体客户端列表
    last_received_message = ""  # 接收的最新信息
    name1 = ""  # 发送者
    name2 = ""  # 接收者
    n1 = ""
    n2 = ""
    client = ""

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_listen()


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
        f1 = open('dict.txt', 'r', encoding="utf-8-sig ")
        f2 = open('client.txt', 'r', encoding="utf-8-sig ")
        for c in f1.readlines():
            a = c.split(" ")
            self.name1 = a[0]
            self.name2 = a[1].strip()
            print(self.name1)
            print(self.name2)
        for c in f2.readlines():
            a = c.split(" ")
            self.n1 = a[0]
            self.n2 = a[1].strip()

            if(self.n1 == self.name1) and (self.n2 == self.name2):
                self.client = a[3].strip()
                print(self.client)
        socket, (ip, port) = self.client
        socket.send(self.last_received_message.encode('utf-8'))
        f1.close()
        f2.close()

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
