from easy_tcp_server import Client

c = Client()
c.host = "localhost"                                           #Client code
c.port = 12345                                             
c.password = "123"
c.start(host=c.host, port=c.port, password=c.password)
