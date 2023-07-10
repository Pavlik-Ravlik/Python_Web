from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import urllib.parse
import mimetypes
import pathlib
import json
import socket
import threading
import os


PORT = 3000
SOCKET_PORT = 5000


class HttpHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        
        if pr_url.path == '/':
            self.send_html_file('index.html')
        
        elif pr_url.path == '/message.html':
            self.send_html_file('message.html')

        else:
            
            if pathlib.Path().joinpath(pr_url.path[1:]).exists():
                self.send_static()
            
            else:
                self.send_html_file('error.html', status=404)


    def do_POST(self):
        filename = 'storage/data.json'
        date = datetime.now()
        
        data = self.rfile.read(int(self.headers['Content-Length']))
        data_parse = urllib.parse.unquote_plus(data.decode())
        data_dict = {username: message for username, message in [
            el.split('=') for el in data_parse.split('&')]}

        data_dict_date = {str(date): data_dict}

        try:
            if os.path.exists(filename) and os.path.getsize(filename) > 0:
                with open(filename, 'r') as file:
                    existing_data = json.load(file)
                data_dict_date.update(existing_data)
        except json.decoder.JSONDecodeError:
            existing_data = {}

        with open(filename, 'w') as file:
            json.dump(data_dict_date, file, ensure_ascii=False, indent=4)

        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()

        
    def send_html_file(self, filename, status=200, content_type='text/html'):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        file_path = os.path.join(os.path.dirname(__file__), filename)
        
        with open(file_path, 'rb') as fd:
            self.wfile.write(fd.read())
    

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        
        if mt:
            self.send_header("Content-type", mt[0])
        
        else:
            self.send_header("Content-type", 'text/plain')
        self.end_headers()
        
        with open(f'.{self.path}', 'rb') as file:
            self.wfile.write(file.read())


def run_http_server(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ('', PORT)
    http = server_class(server_address, handler_class)
    
    try:
        print(f'Starting Http server in port {PORT}')       
        http.serve_forever()
    
    except KeyboardInterrupt:
        http.server_close()


def run_socket_server():
    server_address = ('', SOCKET_PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)

    try:
        print(f'Starting Socket server in port {SOCKET_PORT}')
        
        while True:
            data, address = sock.recvfrom(1024)
            sock.sendto(data, address)
    
    except KeyboardInterrupt:
        print('Destroy server')
    
    finally:
        sock.close()


if __name__ == '__main__':

    http_thread = threading.Thread(target=run_http_server)
    http_thread.start()

    run_socket_server()
