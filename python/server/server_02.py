#!/usr/bin/env python3
"""
License: MIT License
Copyright (c) 2023 Miel Donkers

Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

hostName = "localhost"
serverPort = 8080

lines = [
    "<html>\n",
    "<head>\n",
    "<title>server_02</title>\n",
    "<script type = 'text/javascript'>\n",
    "function sayHello() {\n",
    "yourUrl='/'\n",
    "value='123'\n",
    "var xhr = new XMLHttpRequest();\n",
    "xhr.open('POST', yourUrl, true);\n",
    "xhr.setRequestHeader('Content-Type', 'application/json');\n",
    "xhr.send(JSON.stringify({\n",
        "value: value\n",
    "}));\n"
    "console.log('sayHello')\n",
    "}\n",
    "</script>\n",
    "</head>\n",
    "<body>\n",
    "<p>This is an example web server.</p>\n",
    " <input type = 'button' onclick = 'sayHello()' value = 'Say Hello' />\n"
    "</body>\n",
    "</html>"
]
htmlstring = "".join(lines)


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        logging.info(
            "GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers)
        )
        self._set_response()
        # self.wfile.write("GET request for {}".format(self.path).encode("utf-8"))
        self.wfile.write(htmlstring.encode("utf-8"))



    def do_POST(self):
        content_length = int(
            self.headers["Content-Length"]
        )  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        logging.info(
            "POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
            str(self.path),
            str(self.headers),
            post_data.decode("utf-8"),
        )

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    logging.info("Starting httpd...\n")
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info("Stopping httpd...\n")


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
