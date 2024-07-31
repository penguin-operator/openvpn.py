import unittest
import sys

sys.path.append(".")

import util.cli as cli

class TestCli(unittest.TestCase):
    def test_matchtype(self):
        self.assertEqual(cli.matchtype("true"), True)
        self.assertEqual(cli.matchtype("false"), False)
        self.assertEqual(cli.matchtype("1"), 1)
        self.assertEqual(cli.matchtype("1.5"), 1.5)
        self.assertEqual(cli.matchtype("foo"), "foo")

    def test_argparse(self):
        self.assertEqual(cli.argparse(), ([], {}))
        self.assertEqual(cli.argparse("check"), (["check"], {}))
        self.assertEqual(cli.argparse("install", "package"), (["install", "package"], {}))
        self.assertEqual(cli.argparse("install", "-o=foo"), (["install"], {"-o": "foo"}))
        self.assertEqual(cli.argparse("install", "-o", "foo"), (["install"], {"-o": "foo"}))
        self.assertEqual(cli.argparse("install", "-s"), (["install"], {"-s": True}))
        self.assertEqual(cli.argparse("build", "-j", "11"), (["build"], {"-j": 11}))
        self.assertEqual(cli.argparse("top", "-d=0.1"), (["top"], {"-d": 0.1}))

if __name__ == "__main__":
    unittest.main()
