#!/usr/bin/env python3

"""
.....................IRC-client.........................

.......................Radebe...........................

"""

import socket
import threading
import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox as mb


def _channel_(channel):
    if channel.startswith("#") is False and channel.startswith("!") is False:
        return "#" + channel
    return channel


# helper
def print_response():
    resp = client.get_response()
    if resp:
        msg = resp.strip().split(":")
        print("< {}> {}".format(msg[1].split("!")[0], msg[2].strip()))


class MyClient:

    def __init__(self, username, channel,
                 server="irc.freenode.net", port=6667):
        self.username = username
        self.server = server
        self.port = port
        self.channel = channel

    @property
    def _username(self):
        return self.username

    @_username.setter
    def _username(self, value):
        self.username = value

    @property
    def _channel(self):
        return self.channel

    @_channel.setter
    def _channel(self, value):
        self.channel = value

    def connect(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.server, self.port))

    def get_response(self):
        return self.conn.recv(512).decode("utf-8")

    def send_command(self, command, message):
        command = "{} {}\r\n".format(command, message).encode("utf-8")
        self.conn.send(command)

    def sendMsg(self, message):
        command = "PRIVMSG {}".format(self.channel)
        message = ":" + message
        self.send_command(command, message)

    def join_channel(self):
        command = "JOIN"
        channel = self.channel
        self.send_command(command, channel)


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("520x640")
    window.title(" Internet Relay Chat (IRC) client ")
    label = tk.Label(text="Welcome to Radebe-IRC")
    descrp = "Type your username and channel to join. channel must start with#"
    ds = tk.Label(text=descrp, bd=5)
    label.pack(pady=30, padx=30)
    ds.pack(pady=30, padx=30)
    _nickname = StringVar()
    _channel = StringVar()
    _cmd = StringVar()
    label.pack(pady=30, padx=30)

    username = ""
    channel = ""
    command = ""
    client = MyClient(username, channel)
    _msg = StringVar()

    lbl_nickname = tk.Label(text='Nickname:')
    lbl_nickname.pack(pady=10, padx=10)
    ent_nickname = tk.Entry(textvariable=_nickname)
    ent_nickname.pack(pady=10, padx=10)

    lbl_nickname = tk.Label(text='Channel:')
    lbl_nickname.pack(pady=10, padx=10)
    ent_channel = tk.Entry(textvariable=_channel)
    ent_channel.pack(pady=10, padx=30)

    button = tk.Button(window, text="Join the channel",
                       command=lambda: threading.Thread(target=go()))
    exitB = tk.Button(window, text="Exit",
                      command=lambda: threading.Thread(ExitApplication()))
    inf = "To send message type "
    info = tk.Label(text='Channel:')
    button.pack()
    exitB.pack()

    def set_cmd():
        global command
        # ck = False
        # threading.Thread(irc_command(ck, username))
        command = _msg.get()
        print(command)
        _command(command)

    def new_winF():  # new window
        newwin = tk.Toplevel(window)
        newwin.geometry("420x440")
        newwin.focus_set()
        newwin.title(" Internet Relay Chat")
        m_lbl = tk.Label(newwin, text="Send message to the channel")
        m_lbl.pack(pady=10, padx=30)
        msg = tk.Entry(newwin, textvariable=_msg)
        msg.pack(pady=10, padx=30)
        global client

        button = tk.Button(newwin, text="send", command=lambda: threading.
                           Thread(set_cmd()))
        leave = tk.Button(newwin, text="leave channel",
                          command=lambda: threading.
                          Thread(_command("/quit")))
        button.pack()
        leave.pack()

    def errorMsg():
        mb.showerror("Error", "Enter your username and the channel")

    def ExitApplication():
        MsgBox = tk.messagebox.askquestion("Exit Application",
                                           "Exit the application?",
                                           icon="warning")
        if MsgBox == 'yes':
            window.destroy()
            exit(0)

    def go():
        global username, channel
        username = _nickname.get()
        channel = _channel.get()
        global command
        command = ""
        joined = False

        client._username = username
        client._channel = channel
        client.connect()
        if not username and not channel or channel[0] != '#':
            threading.Thread(target=errorMsg())
            # exit(0)
        else:
            username = _nickname.get()
            channel = _channel.get()
            threading.Thread(new_winF())
            threading.Thread(target=irc_command(joined, username))
            threading.Thread(target=_command(command))

    def irc_command(check, username):
        while(check is False):
            resp = client.get_response()
            print(resp.strip())
            if "No Ident response" in resp:
                client.send_command("NICK", username)
                client.send_command(
                    "USER", "{} * * :{}".format(username, username))

            # join the channel!
            if "376" in resp:
                client.join_channel()

            # username already in use? try to use username with _
            if "433" in resp:
                username = "_" + username
                client.send_command("NICK", username)
                client.send_command(
                    "USER", "{} * * :{}".format(username, username))

            # if PING send PONG with name of the server
            if "PING" in resp:
                client.send_command("PONG", ":" + resp.split(":")[1])

            # joined
            if "366" in resp:
                check = True

    def _command(cmd):
        while(cmd != "/quit"):
            cmd = input("< {}> ".format(username)).strip()
            if cmd == "/quit":
                client.send_command("QUIT", "до свидания!")
            client.sendMsg(cmd)

            response_thread = threading.Thread(target=print_response)
            response_thread.daemon = True
            response_thread.start()

    window.mainloop()
