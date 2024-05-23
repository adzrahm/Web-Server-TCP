import socket

def create_http_request(filename):
    return f"GET /{filename} HTTP/1.1\r\nHost: localhost\r\n\r\n"

def main():
    serverName = '127.0.0.1'  # Menggunakan IP loopback untuk memastikan koneksi lokal
    serverPort = 8090

    try:
        # Create a TCP client socket
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the server
        clientSocket.connect((serverName, serverPort))

        # Define the filename you want to request
        filename = 'tubes.html'  # Ubah ini ke 'style.css' untuk meminta file CSS

        # Create an HTTP GET request
        request = create_http_request(filename)

        # Send the request to the server
        clientSocket.send(request.encode())

        # Receive the response from the server
        response = clientSocket.recv(4096)
        response_parts = response.split(b'\r\n\r\n', 1)
        headers = response_parts[0]
        body = response_parts[1] if len(response_parts) > 1 else b''

        # Print the response
        print("Response headers received from the server:")
        print(headers.decode())
        print("\nResponse body received from the server:")
        print(body.decode())

    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the socket
        clientSocket.close()

if __name__ == '__main__':
    main()
