import requests
import tkinter as tk
import random

# VeevoTech API credentials
hash_key = '531b4c9aa92f2f84881c161d1766e678'
base_url = 'https://api.veevotech.com/v3/sendsms'

# Variable to store the generated OTP
generated_otp = None

def send_otp():
    global generated_otp  # Access the global variable
    # Generate OTP
    generated_otp = generate_otp()
    
    # Prepare the request payload
    payload = {
        'hash': hash_key,
        'receivernum': phone_entry.get(),
        'medium': 1,
        'sendernum': 'Default',
        'textmessage': 'Your OTP is: ' + str(generated_otp),  # Include generated OTP in the message
    }

    # Send the POST request to the VeevoTech API
    response = requests.post(base_url, json=payload)
    response_data = response.json()
    
    # Check if the SMS was successfully sent
    if response_data['STATUS'] == 'SUCCESSFUL':
        print("OTP Sent")
    else:
        print("Failed to send OTP")

def generate_otp():
    # Generate a random 4-digit OTP
    return random.randint(1000, 9999)

def verify_otp():
    # Get the entered OTP from the entry widget
    entered_otp = otp_entry.get()

    # Check if an OTP has been generated and entered
    if generated_otp is None:
        result_label.config(text="Please generate OTP first")
        return

    # Compare entered OTP with the generated OTP
    if entered_otp == str(generated_otp):
        result_label.config(text="OTP Verified Successfully!")
    else:
        result_label.config(text="Invalid OTP")

# Create the Tkinter window
root = tk.Tk()
root.title("Phone Number Verification")

# Create UI elements
phone_label = tk.Label(root, text="Enter Phone Number:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

otp_button = tk.Button(root, text="Send OTP", command=send_otp)
otp_button.pack()

otp_label = tk.Label(root, text="Enter OTP:")
otp_label.pack()
otp_entry = tk.Entry(root)
otp_entry.pack()

verify_button = tk.Button(root, text="Verify OTP", command=verify_otp)
verify_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()
