#!/usr/bin/env python3
"""
Launcher for the Aeolian 3D Sand, Dune & Drift Simulator.
Starts a local HTTP server and opens the Three.js WebGL simulation in your browser.
"""
import http.server
import os
import socketserver
import threading
import webbrowser
from pathlib import Path

PORT = 8088
DIRECTORY = Path(__file__).resolve().parent


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

    def log_message(self, format, *args):
        pass


def main():
    os.chdir(DIRECTORY)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), QuietHandler) as httpd:
        url = f"http://127.0.0.1:{PORT}/index.html"
        print(f"🏜️  Aeolian 3D Sand Simulator running at: {url}")
        print("Press Ctrl+C to stop.")
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")


if __name__ == "__main__":
    main()
