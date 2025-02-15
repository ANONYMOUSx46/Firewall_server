import http.server
import socketserver

class FirewallHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/tomcatwar.jsp":
            self.send_error(403, "Forbidden")
        else:
            http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if "suffix=%>//" in self.headers or \
           "c1=Runtime" in self.headers or \
           "c2=<%" in self.headers or \
           "DNT=1" in self.headers or \
           "Content-Type=application/x-www-form-urlencoded" in self.headers:
            self.send_error(403, "Forbidden")
        else:
            http.server.SimpleHTTPRequestHandler.do_POST(self)

def main():
    PORT = 8000
    with socketserver.TCPServer(("", PORT), FirewallHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()