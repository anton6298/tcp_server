class Server():
    host = 'localhost'
    port = 12345
    password = "123"

    def start(self, host, port, password):
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))

        print("Opened on IP:",host, ". Port:", port, ". Password:", password, ". Waiting for clients connect...")
        while True:
            s.listen(1)
            conn, addr = s.accept()
            print('Client connected by', addr,". Checking password...")
            con = conn.recv(1024)
            if con.decode() == password:
                conn.sendall(b'OK')
                print("Password is right! Success connect!")
                while True:
                    try:
                        data = conn.recv(1024)

                        if not data:
                            pass
                        else:
                            print("Client send: "+str(data.decode()))
                            #conn.sendall(input().encode())

                    except socket.error:
                        print("Error Occured.")
                        conn.close()
                        break
            else:
                conn.sendall(b'Incorrect password! Disconnecting!')
                conn.close()


class Client():
    host = "localhost"
    port = 12345
    password = "123"

    def start(self, host, port, password):
        import socket, sys
        print("Trying to connect to server", host, "on port", port, ".")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host,port))
        except:
            print("Cannot connect to server! Invalid IP or port.")
            input("Press Enter to continue...")
            sys.exit()
        print("Successfully connected! Trying to auth...")
        s.sendall(password.encode())
        con = s.recv(1024)
        if con == b'OK':
            print("Password is valid! Send a message!")
            while True:
                s.sendall(input().encode())
                #data = s.recv(1024)
                #print("Received", repr(data.decode()))
        else:
            print("Incorrect password!")
            input("Press Enter to continue...")
            sys.exit()

        s.close()
