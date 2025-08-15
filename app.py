from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Weather Dashboard coming soon!"

app.run(debug=True, port=3000)







# from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler

# class setupWebServer(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()
#         self.wfile.write('Hello Server World')


# if __name__ == "__main__":
#     hostName = "localhost"
#     serverPort = 8081
#     webServer = HTTPServer((hostName, serverPort), SimpleHTTPRequestHandler)
#     print(f"Server started http://{hostName}:{serverPort}")
#     try:
#         webServer.serve_forever()
#     except KeyboardInterrupt:
#         pass
#     webServer.server_close()
#     print("Server Stopped")