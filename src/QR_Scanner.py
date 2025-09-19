from PIL import Image, ImageDraw, ImageFont
import qrcode
import datetime

# Details
ticket_id = "T12345"
bus_id = "BUS101"
Departure = "City A"
destination = "Market"
date = "2025-09-17"
price = "₹15"
time_now = datetime.datetime.now().strftime("%H:%M:%S")

# QR Data
ticket_data = f"{ticket_id}|{bus_id}|{date}"
qr = qrcode.make(ticket_data).resize((350, 350))

# Ticket canvas
ticket_img = Image.new("RGB", (400, 620), "white")
draw = ImageDraw.Draw(ticket_img)

# Font
try:
    font_big = ImageFont.truetype("arial.ttf", 22)
    font_small = ImageFont.truetype("arial.ttf", 16)
except:
    font_big = ImageFont.load_default()
    font_small = ImageFont.load_default()

font_large = ImageFont.truetype("arial.ttf", size=36)  # Adjust font path and size as needed

# Header
draw.text((140, 20), "PRTC", fill="black", font=font_large)
draw.text((87, 70), f"QR Ticket No: {ticket_id}", fill="black", font=font_big)

# Paste QR
ticket_img.paste(qr, (25, 90))

# Details under QR
y = 440
draw.text((40, y),   f"Fare: {price}", font=font_small, fill="black"); y+=30
draw.text((40, y),   f"Journey : {Departure} >> {destination}", font=font_small, fill="black"); y+=30
draw.text((40, y),   f"Date: {date}  Time: {time_now}", font=font_small, fill="black"); y+=40


draw.line((20, y, 380, y), fill="black", width=2); y+=20

draw.text((80, y), "Please preserve this ticket till exit.", font=font_small, fill="black")

ticket_img.save("bus_ticket.png")
print("Ticket saved as bus_ticket.png")

import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

# Ticket image (jo tu already banata hai)
ticket_path = "bus_ticket.png"
img = Image.open(ticket_path)

# Tkinter window
root = tk.Tk()
root.title("Your Bus Ticket")

# Show image in window
ticket_img = ImageTk.PhotoImage(img)
label = tk.Label(root, image=ticket_img)
label.pack(pady=10)

# Download/save function
def download_ticket():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        img.save(file_path)

# Button
save_btn = tk.Button(root, text="Download Ticket", command=download_ticket)
save_btn.pack(pady=10)

root.mainloop()
