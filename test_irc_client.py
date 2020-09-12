import unittest
import irc_functions


class TestIrc(unittest.TestCase):

    def test_channel(self):
        res = irc_functions._channel_("python")
        self.assertAlmostEqual(res, "#python")

    def test_print_response(self):
        # res = irc_client.print_response()
        pass


if __name__ == '__main__':
    unittest.main()
