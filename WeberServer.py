import http.server
import socketserver
import os
import json
import io
from time import gmtime, strftime

class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_HEAD(s):
        print(" ... do_HEAD",s.__class__)
        #s.print_info()
        super().do_HEAD()

    def do_GET(self):
        print(" ... do_GET")
        #inputData = self.rfile.readline().strip()
        #inputData= self.raw_requestline
        inputData = self.path
        print (inputData)
        #super().do_GET()

        print('Get request received')

        if self.path == "/dirlist":
            self.w_dirlist()
        elif self.path == "/exel":
            self.w_dirlist()
        elif self.path == "/txt":
            self.w_HelloWord()
        else:
            print("no vlaid path found")
            #self.w_HTML()
            super().do_GET()


        return

    def w_HTML(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def w_HelloWord(self):
        self.wfile.write("<body><p>This is a test.</p>".encode('utf8'))
        dt = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        print(dt);
        self.wfile.write("<p>Request was processed at: %s</p>".encode('utf8') % dt.encode('utf8'))
        self.wfile.write("</body></html>".encode('utf8'))
        return

    def w_dirlist(self):
        print("w_dirlist")
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        dirlist = os.listdir('.')  # Change the path here
        str = json.dumps(dirlist).encode('utf8')
        print(str)
        self.wfile.write(json.dumps(dirlist).encode('utf8'))
        return

    def w_startPage(self):
        # Send headers
        #self.send_header('Content-type', 'text/html')
        #self.end_headers()
        self.wfile.write("<html >".encode('utf8'))
        self.wfile.write("  <head >".encode('utf8'))
        self.wfile.write("     <title>Sample Hello, World  Application</title>".encode('utf8'))
        self.wfile.write("  </head >".encode('utf8'))
        self.wfile.write("</html >".encode('utf8'))



PORT = 8000

#Handler = http.server.SimpleHTTPRequestHandler
Handler = MyHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
