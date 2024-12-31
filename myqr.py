pip install qrcode
import qrcode as qr
img=qr.make("https://www.linkedin.com/in/abhiudai-shahi-6274b6255/")
img.save('Abhi-Linkedin.png')
