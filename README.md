# link-bite

This chat application is implemented in Python using `tkinter` for the graphical user interface (GUI). It demonstrates a basic chat system where two instances can communicate with each other over a network. One instance acts as `Chat-1` (server) and the other as `Chat-2` (client).

## Features

- Real-time messaging between `Chat-1` and `Chat-2`.
- GUI designed to resemble WhatsApp's chat interface.
- Messages are aligned based on the sender: `Chat-1` messages are aligned to the right, while `Chat-2` messages are aligned to the left.

## Prerequisites

- Python 3.x (included in the Python standard library)
- `psutil` (optional, for checking port usage)

## Installation

### 1. Clone the Repository

Clone the repository to your local machine:

git clone <repository-url>
cd chat_app

### 2. Set Up the Environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### 3. Install Dependencies

pip install psutil

### 4. Start py files

python ChatServer.py

python ChatClient.py


