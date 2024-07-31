import unittest
import sys

sys.path.append(".")

from api import API, Server, IpSpeed

class APITest(unittest.TestCase):
    def test_server(self):
        server = Server("219.100.37.68", "utsunomiya", "tochigi", "japan", "tcp", 22, "https://ovpn-host.net/219.100.37.68_tcp_22.ovpn")
        ip, city, region, country, proto, port = server
        self.assertEqual((ip, city, region, country, proto, port), ("219.100.37.68", "utsunomiya", "tochigi", "japan", "tcp", 22))

    def test_apis(self):
        self.assertEqual(API.apis, {"ipspeed": IpSpeed})
        class TestAPI(API):
            pass
        self.assertEqual(API.apis["testapi"], TestAPI)

if __name__ == "__main__":
    unittest.main()
