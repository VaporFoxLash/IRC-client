# from irc_functions import _channel_
# from irc_functions import print_response
import irc_functions
from irc_functions import MyClient


def print_response():
    resp = client.get_response()
    if resp:
        msg = resp.strip().split(":")
        print("< {}> {}".format(msg[1].split("!")[0], msg[2].strip()))


def set_cmd(self, cmd):
    # ck = False
    # threading.Thread(irc_command(ck, username))
    cmd = "/quit"
    print(cmd)
    # _command(cmd)
    return cmd


def go(username, channel):
    # global command
    command = ""
    print(username)
    client = irc_functions.MyClient(username, channel)
    joined = False

    client._username = username
    client._channel = channel
    client.connect()
    if not username and not channel or channel[0] != '#':
        threading.Thread(target=self.errorMsg())
        # exit(0)
    else:
        # username = _nickname.get()
        # channel = _channel.get()
        # threading.Thread(self.new_window())
        threading.Thread(
            target=irc_functions.irc_command(joined, username, client)
        )
        threading.Thread(target=irc_functions._command(command))
