#!/usr/bin/python
"""
.....................IRC-client.........................

.......................Radebe...........................

"""


import socket, ssl


server = "irc.freenode.net"  # Server
port = 7000  # Port
channel = "#menlug"  # Channel
nickname = "lordmaibi"


def ping():
    ircsock.send("PONG :pingis\n")


def sendmsg(chan , msg):
    ircsock.send("PRIVMSG " + chan + " :" + msg + "\n")


def joinchannel(chan):
    ircsock.send(("JOIN " + chan + "\n").encode())


def hello():
    ircsock.send("PRIVMSG " + channel + " :Hello!\n")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))  # connect to the server using the port 7000
ircsock = ssl.wrap_socket(s)
ircsock.send(("USER " + nickname + " " + nickname + " " + nickname + " hi \n").encode())  # user authentication
ircsock.send(("NICK " + nickname + "\n").encode())  # assign the nickname to the client

joinchannel(channel)  # Join the channel using the functions previously defined

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
