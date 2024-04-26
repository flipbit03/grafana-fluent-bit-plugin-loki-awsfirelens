import json
from pathlib import Path
import socket
import os
import time
import msgpack

def main():
    test_socket_path = (Path.cwd() / ".s")
    test_socket_path.mkdir(exist_ok=True)

    # Define the path for the Unix socket
    client_socket = test_socket_path / "fluent.sock"
    
    # Do sudo chmod o=rwx
    os.system(f"sudo chmod o=rwx {client_socket}")

    # Connect to the unix socket
    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_socket.connect(str(client_socket))

    try:
        while True:
            # Create a JSON object with the current timestamp
            #payload = {"a": time.time()}
            payload = json.loads((Path.cwd() / "buildtools" / "test_log.json").read_text())
            
            # FluentBit Sock expects data in MessagePack format
            # as an array pf 3 elements: 
            # [str(tag), int(timestamp), record]
            wire_data = ["test", int(time.time()), payload]

            # Dump data to MessagePack
            data_messagepack = msgpack.packb(wire_data)

            # Send data to the server
            server_socket.send(data_messagepack)
            print("Sent:", payload)
            # Wait for 1 second
            time.sleep(10)
    except KeyboardInterrupt:
        print("Server is shutting down.")

if __name__ == "__main__":
    main()
