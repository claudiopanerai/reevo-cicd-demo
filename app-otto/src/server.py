#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json
import math
from socketserver import ThreadingMixIn

hostName = "0.0.0.0"
serverPort = int(os.environ.get('SERVER_PORT', '8000'))
developerName = os.environ.get('DEVELOPER_NAME', "Davide")
podName = os.environ.get('POD_NAME', "Nome Pod non trovato")
status = { "code": 200, "healthy": "OK"}


class Handler(BaseHTTPRequestHandler):
  def do_GET(self):
    match self.path:
      case "/":
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        content = open('index.html', 'rb').read()
        self.wfile.write(content)
      case "/index":
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        content = open('index.html', 'rb').read()
        self.wfile.write(content)
      case "/index.html":
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        content = open('index.html', 'rb').read()
        self.wfile.write(content)
      case "/index.js":
        self.send_response(200)
        self.send_header("Content-type", "text/javascript")
        self.end_headers()
        content = open('index.js', 'rb').read()
        self.wfile.write(content)
      case "/developer-name":
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        content = {}
        content['developerName'] = developerName
        self.wfile.write(json.dumps(content).encode())
      case "/healthz":
        self.send_response(status["code"])
        self.send_header("Content-type", "application/json")
        self.end_headers()
        content = {}
        content['status'] = status["healthy"]
        self.wfile.write(json.dumps(content).encode())
      case "/break":
        status["code"] = 500
        status["healthy"] = "KO"
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        content = {}
        content['result'] = "OK"
        self.wfile.write(json.dumps(content).encode())
      case "/load":
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        content = {}
        content['result'] = "OK"
        self.wfile.write(json.dumps(content).encode())
        for i in range(0,10000000):
          a = math.sqrt(64*64*64*64*64)
      case "/pod-name":
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        content = {}
        content['podName'] = podName
        self.wfile.write(json.dumps(content).encode())
      case _:
        self.send_response(404)
    return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
  """Handle requests in a separate thread."""

if __name__ == "__main__":
  webServer = ThreadedHTTPServer((hostName, serverPort), Handler)
  print("Server started http://%s:%s" % (hostName, serverPort))

  try:
    webServer.serve_forever()
  except KeyboardInterrupt:
    pass

  webServer.server_close()
  print("Server stopped.")