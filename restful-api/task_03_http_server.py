#!/usr/bin/python3
"""Instructions:."""

import http.server
import socketserver


class LocalHandler(http.server.BaseHTTPRequestHandler):
    """"""

    def do_GET(self) -> None:
        """Handlig Different Endpoints:."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(
                b'{"name": "John", "age": 30, "city": "New York"}'
            )
        elif self.path == "/status":
            self.send_response(200, "OK")
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/info":
            self.send_response(200, "Ok")
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(
                b'{"version": "1.0", "description": "A simple API built with http.server"}'
            )
        else:
            self.send_response(404, "Not Found")
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


Handler = LocalHandler
PORT = 8000
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
