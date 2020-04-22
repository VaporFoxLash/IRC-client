import socket


# validate channel
def _channel_(channel):
    if channel.startswith("#") is False and channel.startswith("!") is False:
        return "#" + channel
    return channel


# msg helper using a thread
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
