import qrcode
from PIL import Image
import qrcode.constants
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4
                 )
qr.add_data("I'm kedarnatha shivukumar aareddy changler bidar distic")
qr.make(fit=True)
img=qr.make_image(fill_color="black")
img.save("kedra2_qrcode.png")