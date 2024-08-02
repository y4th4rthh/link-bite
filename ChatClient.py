import socket
import threading
import tkinter as tk
from datetime import datetime
import logging
from utils import format_message, current_time

class Chat2:
    def __init__(self, host='localhost', port=12345):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((host, port))
        except ConnectionError as e:
            logging.error("Failed to connect to server: %s", e)
            return

        self.window = tk.Tk()
        self.window.title("Chat-2")
        self.window.geometry("700x700")
        self.window.configure(bg="#333333")

        # Chat area
        self.chat_area = tk.Text(self.window, state='disabled', wrap=tk.WORD, bg="#1e1e1e", fg="#FFFFFF", font=("Arial", 12))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Message entry
        self.message_entry = tk.Entry(self.window, width=40, font=("Arial", 12), bg="#4d4d4d", fg="#FFFFFF")
        self.message_entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)

        # Send button
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message, bg="#00796b", fg="#FFFFFF", font=("Arial", 12, "bold"))
        self.send_button.pack(side=tk.RIGHT, padx=10, pady=10)

        threading.Thread(target=self.receive_messages, daemon=True).start()
        self.window.mainloop()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    self.chat_area.config(state='normal')
                    self.chat_area.insert(tk.END, f"{self.format_message('Chat-1', message, align='right')}\n")
                    self.chat_area.yview(tk.END)  # Auto-scroll to latest message
                    self.chat_area.config(state='disabled')
            except ConnectionResetError:
                logging.error("Connection reset by server")
                break

    def send_message(self):
        message = self.message_entr
