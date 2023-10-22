import http.server
import socketserver

PORT = 8000  # You can choose any available port
DIRECTORY = "/home/sandesh/mqtt_project"  # Specify the directory where your files are

Handler = http.server.SimpleHTTPRequestHandler
Handler.directory = DIRECTORY  # Set the directory for the handler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT} from {DIRECTORY}")
    httpd.serve_forever()
