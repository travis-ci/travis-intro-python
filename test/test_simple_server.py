import socket
import sys
import thread
import unittest

sys.path.append('lib')

import server

class TestServer(unittest.TestCase):

	def start_server(args):
		server.start()

	def test_port_is_open(self):
		thread.start_new_thread( self.start_server, () )
		s = socket.socket()

		self.assertIsNone(s.connect(('localhost', 8000)))

if __name__ == '__main__':
	unittest.main()
