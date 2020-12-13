from tkinter import Tk, Frame, Scrollbar, Label, END, Entry, Text, VERTICAL, Button, messagebox
import socket
import threading


class Chatclient:
    # 客户端

    #初始化
    def __init__(self):
        self.message = None
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 声明socket类型
        self.client_connect()
        # self.client_listen()
        # self.client_socket.close()

    #客户端请求连接
    def client_connect(self):
        local_ip = "192.168.43.18"
        local_port = 10319
        self.client_socket.connect((local_ip, local_port))  # 连接服务端
        print(self.client_socket)

    # 客户端生成新的线程，诱发数据接受函数
    def client_listen(self):
        # sthread = threading.Thread(target=self.send, args=(self.client_socket,))
        # sthread.start()
        rthread = threading.Thread(target=self.recv, args=(self.client_socket,))
        rthread.setDaemon(True)
        rthread.start()

    #客户端接受数据函数
    def recv(self, cs):
        while(True):
            recv_data = cs.recv(1024)
            if not recv_data:
                break
            self.message = recv_data.decode('utf-8')
        cs.close()

    #客户端发送数据函数
    def send(self, cs):
        while (True):
            send_data = input().strip()
            if not send_data:
                break
            cs.send(send_data.encode("utf-8"))
        cs.close()

if __name__ == "__main__":
    c = Chatclient()
