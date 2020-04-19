#!/usr/bin/python
"""
.....................IRC-client.........................

.......................Radebe...........................

"""


import socket, ssl
import tkinter as tk
from tkinter import *


LARGE_FONT= ("Verdana", 12)
server = "irc.freenode.net"  # Server
port = 7000  # Port
channel = "#menlug"  # Channel
nickname = "lordmaibi"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connectT():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))

ircsock = ssl.wrap_socket(s)


def joinchannel(chan):
    ircsock.send(("JOIN " + chan + "\n").encode())


# joinchannel(channel)

def auth(nick):
    connectT()
    global ircsock
    ircsock = ssl.wrap_socket(s)
    ircsock.send(("USER " + nick + " " + nick + " " + nick + " hi \n").encode())  # user authentication
    ircsock.send(("NICK " + nick + "\n").encode())  # assign the nickname to the client



def ping():
    ircsock.send("PONG :pingis\n")


def sendmsg(chan , msg):
    ircsock.send("PRIVMSG " + chan + " :" + msg + "\n")


def hello():
    ircsock.send("PRIVMSG " + channel + " :Hello!\n")


class irc_client():
    pass

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.configure(background="light green")
        container.configure(width=400, height=400)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=100)
        container.grid_columnconfigure(0, weight=10)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.configure(background="light green")
        frame.configure(width=400, height=400)
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        _nickname = StringVar()
        label = tk.Label(self, text="Welcome to Radebe-IRC", font=LARGE_FONT)
        label.pack(pady=30,padx=30)

        label1 = tk.Label(self, text="Enter nickname to ", font=LARGE_FONT)
        label1.pack(pady=10,padx=10)

        lbl_nickname = tk.Label(self, text='Nickname:', font=LARGE_FONT)
        lbl_nickname.pack(pady=10,padx=10)
        ent_nickname = tk.Entry(self, textvariable=_nickname)
        ent_nickname.pack(pady=10,padx=10)

        button = tk.Button(self, text="Connect to freenode server",
                            command=lambda: controller.show_frame(PageOne))
        button.bind("<Button-1>", auth(str(_nickname)))
        button.pack()
        # ircmsg = ircsock.recv(2048)  # receive data from the server
        # ircmsg = ircmsg.strip(('\n\r').encode())
        msg = tk.Message(self, text="Connecting to " + server)
        msg.pack()

        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        _channel = StringVar()

        lbl_channel = tk.Label(self, text='channel:', font=LARGE_FONT)
        lbl_channel.pack(pady=10,padx=10)
        ent_channel = tk.Entry(self, textvariable=_channel)
        ent_channel.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Join channel",
                            command=lambda: controller.show_frame(PageTwo))
        button1.bind("<Button-1>",joinchannel(str(_channel)))
        button1.pack()

        button2 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        button1 = tk.Button(self, text="Join channel",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()



app = SeaofBTCapp()
while 1:
    ircmsg = ircsock.recv(2048)  # receive data from the server
    ircmsg = ircmsg.strip(('\n\r').encode())  # removing any unnecessary linebreaks.
    print(ircmsg)  # print what's coming from the server

    print("Send message to " + channel)
    mssg = str(input())
    ircsock.send(mssg.encode())

if ircmsg.find(":Hello " + nickname) != -1: # reply to message
    # hello()
    print("Send message to " + channel)
    mssg = str(input())
    ircsock.send(mssg.encode())

if ircmsg.find("PING :") != -1:  # respond to server's ping
    ping()
app.mainloop()

# joinchannel(channel)  # Join the channel using the functions previously defined
