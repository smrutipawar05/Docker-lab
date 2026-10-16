from http.server import HTTPServer,BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if(self.path=="/health"):
            self.send_response(200)
            self.send_header("Content-Type","text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        elif(self.path=="/"):
            self.send_response(200)
            self.send_header("Content-Type","text/plain")
            self.end_headers()
            self.wfile.write(b"Hello from Docker.")
        else:
            self.send_response(404)
            self.send_header("Content-Type","text/plain")
            self.end_headers()
            self.wfile.write(b"Failed")

server=HTTPServer(("0.0.0.0", 8000),RequestHandler)
server.serve_forever()
