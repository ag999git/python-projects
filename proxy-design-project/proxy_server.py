
# ---------- proxy_server.py ----------
from real_server import RealServer

class ProxyServer:
    """Acts as a middleman between client and the real server."""

    def __init__(self):
        self.__real_server = RealServer()  # Private attribute

    def connect(self, client_name):
        print(f"ProxyServer: Client '{client_name}' connected.")
        print("ProxyServer: Forwarding request to RealServer...\n")
        self.__real_server.fetch_python_page()


