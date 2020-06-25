import socket


# validate channel
def _channel_(channel):
    if channel.startswith("#") is False and channel.startswith("!") is False:
        return "#" + channel
    return str(channel)


# msg helper using a thread
def print_response():
    resp = client.get_response()
    if resp:
        msg = resp.strip().split(":")
        print("< {}> {}".format(msg[1].split("!")[0], msg[2].strip()))
    return resp


def NameLength(name):
    return len(name)

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

class MyClient:

    def __init__(self, username, channel,
                 server="irc.freenode.net", port=6667):
        self.username = username
        self.server = server
        self.port = port
        self.channel = channel

    # @property
    # def server(self):
    #     return self.server

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
        flag = False
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.conn.connect((self.server, self.port))
            flag = True
        except socket.timeout:
            print("Couldn't connect")
        return flag

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
