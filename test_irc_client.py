import unittest
import irc_functions
import socket
# from irc_client import NameLength


class TestIrc(unittest.TestCase):

    # client = irc_functions.MyClient()
    server = "irc.freenode.net"
    port = 6667

    def test_connect(self):
        fl = irc_functions.connect()
        self.assertAlmostEqual(fl, True)

    def test_NameLength(self):
        res = irc_functions.NameLength("name")
        self.assertAlmostEqual(res, 4)

    def test_channel(self):
        res = irc_functions._channel_("python")
        self.assertAlmostEqual(res, "#python")

    def test_print_response(self):
        resp = irc_functions.MyClient.get_response(self)
        # testResp = server.conn.recv(512).decode("utf-8")
        pass

    def test_connect(self):
        # res = irc_functions.MyClient.connect()
        # self.conn = socket.socket
        # self.assertAlmostEqual(res, con)
        pass

    def test_get_response(self):
        # self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.conn.connect((self.server, self.port))
        # res = irc_functions.MyClient.get_response(self)
        pass

    def test_send_command(self):
        pass

    def test_sendMsg(self):
        pass

    def test_join_channel(self):
        pass


if __name__ == '__main__':
    unittest.main()
