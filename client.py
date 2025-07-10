import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print("\n" + message)
        except:
            print("Connection closed by server.")
            sock.close()
            break

def send_messages(sock, username):
    while True:
        message = input()
        full_message = f"{username}: {message}"
        sock.send(full_message.encode('utf-8'))

def main():
    host = "127.0.0.1"
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    username = input("Enter your name: ")

    print(f"Connected to server as {username}. Start chatting!\n")

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
    send_messages(client, username)

if __name__ == "__main__":
    main()
