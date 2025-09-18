QR Code Generator

A simple Python QR Code Generator that can create different types of QR codes, such as text, phone numbers, WhatsApp chat links, website URLs, and UPI payment codes.

Features

🔹 Generate QR codes for any text or number

🔹 Generate QR codes for phone numbers (call directly when scanned)

🔹 Generate QR codes for WhatsApp chats with pre-filled messages

🔹 Generate QR codes for website links

🔹 Generate UPI payment QR codes

Installation

Clone the repository:

git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator


Install the required package:

pip install qrcode[pil]

Usage

Run the script:

python qr_generator.py


Choose the type of QR code you want to generate:

1. Any text or number
2. Phone number
3. Direct WhatsApp chat
4. Website link
5. UPI payment QR code


Example:

For text:

enter your text or number data to make qr code: HelloWorld


→ Generates HelloWorld.png

For WhatsApp chat:

enter your direct opening whatsapp chat: 919876543210
you can enter your msg automatically: Hello%20there


→ Generates a QR that opens WhatsApp chat with a pre-filled message.

For UPI payment:

enter your upi id: yourupi@bank
enter your name: John
enter amount: 100
enter currency: INR


→ Generates John.png for UPI payment.

Example Output

When scanned, the QR code will directly open the respective action (call, WhatsApp, link, or UPI payment).

Requirements

Python 3.x

qrcode library (pip install qrcode[pil])

License

This project is licensed under the MIT License – feel free to use and modify it.
