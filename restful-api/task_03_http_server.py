import http.server
import socketserver
import json

PORT = 8000


class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content_Type", "text/plain; charset=utf-8")
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content_Type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content_Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content_Type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content_Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serveur lancé sur le port {PORT}")
    httpd.serve_forever()