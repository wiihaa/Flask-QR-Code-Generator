# QR Code Generator (Flask)

A simple Flask web app that generates QR codes from text or URLs and lets users download them as PDF files.

---

## 🚀 Features

- Generate QR codes directly in the browser  
- Download as high-quality PDF  
- Fast and lightweight (no external services required)

---

## 🛠️ Installation
```bash
git clone https://github.com/wiihaa/Flask-QR-Code-Generator.git
cd Flask-QR-Code-Generator
python -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py

Visit [http://localhost:5001](http://localhost:5001) in your browser.
```
---

## 📦 Requirements

Flask>=3.0.0
qrcode[pil]>=7.4.2
reportlab>=4.1.0


---

## 📄 Usage

1. Enter any URL or text.  
2. Click **Generate**.  
3. A PDF file with your QR code will download automatically.

---