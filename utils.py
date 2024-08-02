from datetime import datetime

def format_message(sender, message):
    return f"{sender}: {message} [{current_time()}]"

def current_time():
    return datetime.now().strftime("%H:%M:%S")
