import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)


def start():
	print("Starting server at http://localhost:" + str(PORT))
	httpd.serve_forever()

if __name__ == "__main__":
	start()
