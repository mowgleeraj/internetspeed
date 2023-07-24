import tkinter as tk
from tkinter import ttk
import speedtest

def get_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping

    download_label.config(text=f"Download: {download_speed:.2f} Mbps")
    upload_label.config(text=f"Upload: {upload_speed:.2f} Mbps")
    ping_label.config(text=f"Ping: {ping} ms")

# Create the main window
root = tk.Tk()
root.title("Internet Speed Test")
root.geometry("300x200")
root.resizable(False, False)

# Create the frames
header_frame = ttk.Frame(root)
speed_frame = ttk.Frame(root)

# Pack the frames
header_frame.pack(pady=10)
speed_frame.pack(pady=20)

# Create the header label
header_label = ttk.Label(header_frame, text="Internet Speed Test", font=("Helvetica", 16))
header_label.pack()

# Create the labels to display the internet speed
download_label = ttk.Label(speed_frame, font=("Helvetica", 14))
upload_label = ttk.Label(speed_frame, font=("Helvetica", 14))
ping_label = ttk.Label(speed_frame, font=("Helvetica", 14))

download_label.pack(pady=5)
upload_label.pack(pady=5)
ping_label.pack(pady=5)

# Create the test button
test_button = ttk.Button(root, text="Test Speed", command=get_speed)
test_button.pack(pady=10)

# Run the main event loop
root.mainloop()
