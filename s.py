# ChatGPT Like App using Python

import tkinter as tk
from datetime import datetime

# Window
root = tk.Tk()
root.title("Mini ChatGPT")
root.geometry("500x600")

# Chat Area
chat_area = tk.Text(root, font=("Arial", 14))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Answer Function
def chatbot_response(user):

    user = user.lower()

    if "hello" in user or "hi" in user:
        return "Hello! 😊"

    elif "how are you" in user:
        return "I am fine!"

    elif "your name" in user:
        return "My name is Mini ChatGPT."

    elif "time" in user:
        return datetime.now().strftime("Current Time: %H:%M:%S")

    elif "date" in user:
        return datetime.now().strftime("Today's Date: %d-%m-%Y")

    elif "python" in user:
        return "Python is a programming language."

    else:
        return "Sorry, I don't understand."

# Send Message
def send_message():

    user_message = entry_box.get()

    if user_message.strip() != "":

        chat_area.insert(tk.END, "You: " + user_message + "\n")

        bot_reply = chatbot_response(user_message)

        chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n")

    entry_box.delete(0, tk.END)

# Entry Box
entry_box = tk.Entry(root, font=("Arial", 14))
entry_box.pack(padx=10, pady=10, fill=tk.X)

# Send Button
send_button = tk.Button(root, text="Send", font=("Arial", 14), command=send_message)
send_button.pack(pady=5)

# Run App
root.mainloop()