from path import Path
from qrcode_img import QRCode
from convert import png_to_svg



text = 'Hello'

path_to_download = Path().joinpath("example", "11.png")
path_to_save = Path().joinpath("example", "1example.png")


qrcode = QRCode(text)

qrcode.gen_qr_code(path_to_download, path_to_save)


svg_pixel = png_to_svg(path_to_save)


f = open("test.txt", "w")

f.write(svg_pixel)

f.close()
