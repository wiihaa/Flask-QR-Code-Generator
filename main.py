from flask import Flask, render_template, request, send_file, Response
import qrcode
from io import BytesIO
from reportlab.pdfgen import canvas
import os
import qrcode.image.svg

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data_to_encode = request.form['url']
    

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,
    )
    qr.add_data(data_to_encode)
    qr.make(fit=True)
    # qr_img = qr.make_image(fill_color="black", back_color="white" if white_background else None)
    qr_img = qr.make_image(fill_color="black", back_color='white')

    # Save QR code as PNG (temporary file)
    temp_png = BytesIO()
    qr_img.save(temp_png, format='PNG')
    temp_png.seek(0)

    # Calculate square canvas size based on QR code size
    canvas_size = max(qr_img.width, qr_img.height)

    # Create PDF with QR code
    pdf_buffer = BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=(canvas_size, canvas_size))

    # Save QR code image to a temporary file
    temp_image_path = 'temp_qr.png'
    qr_img.save(temp_image_path, format='PNG')

    # Draw the image from the temporary file
    c.drawImage(temp_image_path, 0, 0, width=canvas_size, height=canvas_size)

    # Clean up temporary file
    os.remove(temp_image_path)

    c.save()

    # Set up response headers
    pdf_buffer.seek(0)
    response = Response(pdf_buffer, content_type='application/pdf')
    response.headers['Content-Disposition'] = f'attachment; filename={data_to_encode.replace(" ", "_")}_qr_code.pdf'
    return response
    


    

if __name__ == "__main__":
    app.run(debug=True, port=5001)
