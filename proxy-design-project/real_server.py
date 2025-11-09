
# ---------- real_server.py ----------
import requests

class RealServer:
    """The actual server that performs the real work."""

    def fetch_python_page(self):
        url = "https://www.python.org/"
        print("RealServer: Fetching data from Python.org...")

        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("RealServer: Successfully accessed Python.org!")
                print("\n--- Showing first few lines of content ---")
                print(response.text[:300])  # Show preview
                print("\n--- End of preview ---\n")
            else:
                print(f"RealServer: Could not reach the link. Status code: {response.status_code}")
        except Exception as e:
            print("RealServer: Error while fetching data:", e)

