QR Code Generator

<a href="https://qrcodemaker-opal.vercel.app/" target="_blank"> Official Website </a>

A simple Python QR Code Generator that can create different types of QR codes, such as text, phone numbers, WhatsApp chat links, website URLs, and UPI payment codes.

Features

🔹 Generate QR codes for any text or number

🔹 Generate QR codes for phone numbers (call directly when scanned)

🔹 Generate QR codes for WhatsApp chats with pre-filled messages

🔹 Generate QR codes for website links

# QR Code Maker

QR Code Maker is a small, open-source Python app for generating QR codes for text, phone numbers, WhatsApp chats, website URLs, and UPI payments. It includes both a GUI and a console interface.

## Table of Contents

- Features
- Requirements
- Installation
- Running the app
- Usage examples
- Building a Windows executable
- Project structure
- Contributing
- License & Contact

## Features

- Generate QR codes from plain text or numbers
- Phone-number QR codes (tel: links)
- WhatsApp chat QR codes with optional pre-filled message
- Web link QR codes (http/https)
- UPI payment QR codes (India)
- GUI and CLI options; standalone Windows executable available in `dist/` when built

## Requirements

- Python 3.8 or newer (recommended)
- Dependencies (install below): `qrcode`, `Pillow` (PIL), and `pywin32` for Windows clipboard support

## Installation

Clone the repository and set up a Python virtual environment (recommended):

```bash
git clone https://github.com/shirshadip/qr_code_maker.git
cd qr_code_maker
python -m venv .venv
.venv\Scripts\activate   # Windows
# or: source .venv/bin/activate  # macOS / Linux
pip install --upgrade pip
pip install qrcode pillow pywin32
```

Windows users can also run `download.bat` to get a packaged executable (if available in `dist/`).

## Running the app

- GUI (Windows):

```bash
python "gui_app/qrcode maker.py"
```

- Console UI (CLI):

```bash
python cui_app/main.py
```

- Alternatively, some builds include a top-level `main.py` that launches the preferred interface:

```bash
python main.py
```

## Usage examples

- Plain text: enter text and generate a QR image (PNG)
- Phone: provide a phone number to create a `tel:` QR code
- WhatsApp: provide country code + number and optional message (URL-encoded) to open a chat
- UPI: provide `upi_id`, `payee_name`, and optionally an `amount` to generate a payment QR

Example (WhatsApp message):

```
Phone: 919876543210
Message: Hello%20there
```

When scanned, the QR opens WhatsApp chat with the pre-filled message.

## Building an executable (optional)

To create a standalone Windows executable using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=icon.ico "gui_app/qrcode maker.py"
```

The generated executable will appear in `dist/`.

## Project structure

Below is a simplified view of the repository layout:

```
qr_code_maker/
├── .git/
├── .github/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── documentation/
│   ├── index.css
│   └── README.md
├── gui_app/
│   └── qrcode maker.py
├── cui_app/
│   └── main.py
├── dist/       # optional built executables
├── build/
├── icon.ico
├── logo.png
├── index.html  # documentation site
├── main.py
├── main.spec
└── QrcodeMaker.spec
```

## Contributing

Contributions are welcome — please read `CONTRIBUTING.md` for guidelines. Open issues for bugs or feature requests, and submit pull requests from feature branches.

## License

This project is licensed under the MIT License — see `LICENSE` for details.

## Contact

For support or questions, contact: shirshadiphere@gmail.com
