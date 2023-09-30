import os
import time
from instagrapi import Client
from decouple import config

# Get Instagram credentials from the .env file
USERNAME = config('INSTAGRAM_USERNAME')
PASSWORD = config('INSTAGRAM_PASSWORD')

# List of custom messages
custom_messages = [
    "HAHAHAHAHA",
    "Bosan do",
    "Hmmm lapar la",
    "AFIQ!!!"
    # Add more messages as needed
]

# Utility Functions

def generate_cookie(username, password):
    cl = Client()
    cl.login(username, password)
    cl.dump_settings(f"{username}.json")

def send_notification(username, password, note_text):
    cl = Client()
    cl.load_settings(f"{username}.json")
    cl.login(username, password)
    cl.create_note(note_text, 0)

def main():
    if USERNAME is None or PASSWORD is None:
        print("Instagram credentials not provided in .env file.")
        return

    if os.path.exists(f"{USERNAME}.json"):
        print("Using existing cookies")
    else:
        generate_cookie(USERNAME, PASSWORD)
        print("Cookies generated")

    previous_note_index = -1

    while True:
        current_hour = int(time.strftime("%H"))
        
        # Change the note every hour
        note_index = (current_hour % len(custom_messages))
        if note_index != previous_note_index:
            note_text = custom_messages[note_index]
            print(send_notification(USERNAME, PASSWORD, note_text))
            previous_note_index = note_index

        # Sleep for an hour
        time.sleep(3600)  # 3600 seconds = 1 hour

if __name__ == "__main__":
    main()
