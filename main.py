import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget
from Logic import Logic
from Main_call import Main_call
from Person_list import Person_list
from People_talk import People_talk
from Person_talk import Person_talk
from client import Chatclient
from server import ChatServer

'''
    小红-> 小蓝-1
    小蓝-> 小红-2
    小红-> 小紫-3
    小紫-> 小红-4
    小蓝-> 小紫-5
    小紫-> 小蓝-6
'''
name = "小陈".encode("utf-8")
if __name__ == '__main__':

    #主界面登录模块
    message = ""
    k = {}
    f = open('name.txt', 'r', encoding="utf-8-sig ") #解决方法博客：https://blog.csdn.net/qq_38882327/article/details/89637884
    for c in f.readlines():
        a = c.split(" ")
        n = a[0]
        p = a[1].strip()
        k[n] = p
    f.close()
    #创建QApplication类的实例
    app = QApplication(sys.argv)

    logic = Logic()

    main_call = Main_call()
    person_list = Person_list()
    people_talk = People_talk()
    senddata = people_talk.D_input
    all_chat = people_talk.D_textedit
    all_chat.setReadOnly(True)  # 只读
    all_chat.setText("")


    #------修改处
    # 修改部分，为每一个聊天对象建立一个对象，只需在下面各自的点击函数修改对象名即可
    person_talk_red = Person_talk()
    senddata_red = person_talk_red.D_input
    person_chat_red = person_talk_red.D_input_text
    person_chat_red.setReadOnly(True)
    person_chat_red.setText("")

    person_talk_blue = Person_talk()
    person_talk_purple = Person_talk()
    #------修改结束
    #登录界面槽函数
    def logic_signal_function():
        n = logic.D_name.text()
        p = logic.D_password.text()
        for key in k.keys():
            if(key == n) and (k[key] == p):
                global name
                name = n
                logic.hide()
                main_call.show()


    def client_listen(cs):
        # sthread = threading.Thread(target=self.send, args=(self.client_socket,))
        # sthread.start()
        rthread = threading.Thread(target=recv, args=(cs,))
        rthread.setDaemon(True)
        rthread.start()

    def recv(cs):
        while(True):
            recv_data = cs.recv(1024)
            if not recv_data:
                break
            recv_msg = recv_data.decode('utf-8')
            all_chat.append(recv_msg)
        cs.close()

    def text_changed(cs):
        msg = senddata.toPlainText()
        print('hello')
        global name
        if '\n' in msg:
            # msg = msg.replace('\n', '')
            senddata.setText("")
            message = name + ":" + msg
            cs.send(message.encode("utf-8"))  # 发送消息

    def text_changed_red(cs):
        print('hllo')
        msg = senddata_red.toPlainText()
        print(msg)
        global name
        if '\n' in msg:
            # msg = msg.replace('\n', '')
            senddata_red.setText("")
            message = name + ":" + msg
            cs.send(message.encode("utf-8"))  # 发送消息

            #主列表界面槽函数//////
    def main_call_people_talk_function():
        #main_call.hide()
        people_talk.show()
        # ChatServer().server_listen()  # 服务器启动
        c = Chatclient()
        cs = c.client_socket
        senddata.textChanged.connect(lambda:text_changed(cs))
        client_listen(cs)

    def main_call_person_talk_function():
        main_call.hide()
        person_list.show()

    def main_call_back_function():
        main_call.hide()
        logic.show()

    #人物列表槽函数
    def person_list_back_function():
        person_list.hide()
        main_call.show()

    #以下是三个人物的列表
    #-------修改处
    def person_list_blue_function():
        #person_list.hide()
        '''
        if name == "小蓝":
            print("自己不能和自己通信！")
            person_list.hide()
            main_call.show()
            return
        '''
        person_talk_blue.show()
        person_talk_blue.D_person_name.setText("小蓝")
        #检测当前登录和点击为同一对象时，退出当前界面，终端提示报错信息

        ChatServer().server_listen()  # 服务器启动
        c = Chatclient()
        cs = c.client_socket
        print("guo")
        senddata_red.textChanged.connect(lambda:text_changed_red(cs))
        client_listen(cs)

    def person_list_red_function():
        #person_list.hide()
        if name == "小红":
            print("自己不能和自己通信！")
            person_list.hide()
            main_call.show()
            return
        person_talk_red.show()
        person_talk_red.D_person_name.setText("小红")

    def person_list_purple_function():
        #person_list.hide()
        if name == "小紫":
            print("自己不能和自己通信！")
            person_list.hide()
            main_call.show()
            return
        person_talk_purple.show()
        person_talk_purple.D_person_name.setText("小紫")
    #------修改截至

    #logic.logic_signal.connect(logic_signal_function)
    #main_call.main_call_people_talk_signal.connect(main_call_people_talk_function)
    #main_call.main_call_person_talk_signal.connect(main_call_person_talk_function)
    #main_call.main_call_back_signal.connect(main_call_back_function)

    #登录界面槽函数
    logic.P_denglu.clicked.connect(logic_signal_function)

    #主列表界面槽函数
    main_call.P_back.clicked.connect(main_call_back_function)
    main_call.P_person.clicked.connect(main_call_person_talk_function)
    main_call.P_people.clicked.connect(main_call_people_talk_function)

    #个人聊天列表界面槽函数
    person_list.P_back.clicked.connect(person_list_back_function)
    person_list.P_blue.clicked.connect(person_list_blue_function)
    person_list.P_red.clicked.connect(person_list_red_function)
    person_list.P_purple.clicked.connect(person_list_purple_function)



    logic.show()
    sys.exit(app.exec_())
