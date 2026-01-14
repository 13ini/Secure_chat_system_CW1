#cli client

import socket
import threading
from encryption import encrypt_message, decrypt_message

HOST = '127.0.0.1'
PORT = 12345
client_socket = None

def receive_messages():
    while True:
        try:
            encrypted_msg = client_socket.recv(1024)
            if not encrypted_msg:
                break
            decrypted_msg = decrypt_message(encrypted_msg)
            print(f"\n[Friend]: {decrypted_msg}")
        except:
            break

def connect_to_server():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        print("\n✅ Connected to the server!")
        threading.Thread(target=receive_messages, daemon=True).start()
    except Exception as e:
        print(f"❌ Connection failed: {e}")

def send_message():
    if not client_socket:
        print("\n❌ Not connected to the server!")
        return
    message = input("\nEnter message: ")
    if message:
        encrypted_msg = encrypt_message(message)
        client_socket.send(encrypted_msg)

def disconnect():
    global client_socket
    if client_socket:
        client_socket.close()
    print("\n📴 Disconnected from the server.")
    exit()

def main_menu():
    while True:
        print("\n🔹 MENU 🔹")
        print("1. Connect to Server")
        print("2. Send Message")
        print("3. Disconnect")
        print("4. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == "1":
            connect_to_server()
        elif choice == "2":
            send_message()
        elif choice == "3":
            disconnect()
        elif choice == "4":
            print("\n👋 Exiting...")
            break
        else:
            print("\n❌ Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()


