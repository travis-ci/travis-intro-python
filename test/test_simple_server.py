import socket
import sys
import thread

sys.path.append('lib')

import server

def start_server():
	server.start()

def test_port_is_open():
	thread.start_new_thread( start_server, () )
	s = socket.socket()

	try:
		s.connect(('localhost', 8001))
	except Exception:
		pytest.fail("Unable to connect to localhost:8000")
