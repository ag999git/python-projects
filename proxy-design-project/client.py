
# ---------- client.py ----------
from proxy_server import ProxyServer

# Create a proxy server instance
proxy = ProxyServer()

# Clients connect via proxy
proxy.connect("Alice")
proxy.connect("Bob")


