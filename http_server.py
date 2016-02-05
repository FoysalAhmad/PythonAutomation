from __future__ import print_function
import SimpleHTTPServer
import BaseHTTPServer
import SocketServer
import json
import os

PORT = 8000
file_count = 1

class HTTPWithPostRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        with open('index.html') as f:
            self.wfile.write(f.read())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        print("POST command received")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()

        self.ensure_dir('posts')

        global file_count
        with open('posts/file_%04d.txt' % file_count, 'w') as outfile:
            outfile.write(self.data_string)
        file_count += 1
        print(file_count)
        print(self.data_string)
        # for now, just return index.html
        with open('index.html') as f:
            self.wfile.write(f.read())

    def ensure_dir(self, f):
        if not os.path.exists(f):
            os.makedirs(f)


handler = HTTPWithPostRequestHandler # SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), handler)
print("Hosting port on", PORT)

httpd.serve_forever()


