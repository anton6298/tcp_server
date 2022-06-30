from easy_tcp_server import Server

s = Server()
s.host = "localhost"                                           #Server code
s.port = 12345
s.password = "123"
s.start(host=s.host, port=s.port, password=s.password)

