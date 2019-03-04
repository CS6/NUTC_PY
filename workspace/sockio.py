#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# -*- recv data/events from sensors, ant-plus, and buttons -*-

import socket
import sys
import os



server_address = '/tmp/movit.sock'

# Make sure the socket does not already exist
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise


def serve_forever():
    # Create a UDS socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # Bind the socket to the address
    print('starting up on {}'.format(server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:

        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()

        # pid = os.fork()
        # if pid == 0:  # child
        #     sock.close()  # close child copy
        #     handle_request(connection)
        #     connection.close()
        #     os._exit(0)  # child exits here
        # else:  # parent
        #     connection.close()  # close parent copy and loop over


        try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                # data = connection.recv(16)
                data = connection.recv(1024)
                print('received {!r}'.format(data))
                print("decoded: ", data.decode())
                if data:
                    print("We've got data")
                    # print('sending data back to the client')
                    # connection.sendall(data)
                else:
                    print('no data from', client_address)
                    break

        finally:
            # Clean up the connection
            connection.close()

if __name__ == '__main__':
    serve_forever()