import qrcode
from PIL import Image, ImageDraw
from path import Path


class QRCode:
    COEFF = 10
    BLACK_LINE = (0, 0, 0, 230)
    WHITE_LINE_BEFORE = (255, 255, 255, 50)
    WHITE_LINE_AFTER = (255, 255, 255, 230)

    def __init__(self, text: str) -> None:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=1,
        )
        qr.add_data(text)
        qr.make(fit=True)
        self.img = qr.get_matrix()
        self.coeff = self.COEFF
        self.coeff_small = round(self.COEFF / 3)
        self.length_qr = len(self.img) * self.COEFF
        self.back_im = Image.new("RGBA", (self.length_qr, self.length_qr), (0, 0, 0, 0))
        self.idraw = ImageDraw.Draw(self.back_im, "RGBA")
    
    def gen_qr_code(self, path_to_download: Path, path_to_save: Path = None) -> bool:

        background = Image.open(
            path_to_download
        ).resize(
            (self.length_qr, self.length_qr)
        ).convert("RGBA")


        background = self.__get_qr_code_with_img(background)
        if path_to_save is not None:
            path_to_download = path_to_save

        background.save(path_to_download)
        return True
    
    def __get_qr_code_with_img(self, background):
        x = 0
        y = 0
        for string in self.img:
            for i in string:
                if i:
                    self.idraw.rectangle(
                        (
                            x + self.coeff_small,
                            y + self.coeff_small,
                            x + self.coeff - self.coeff_small,
                            y + self.coeff - self.coeff_small,
                        ),
                        fill=self.BLACK_LINE,
                    )

                else:
                    self.idraw.rectangle(
                        (
                            x + self.coeff_small,
                            y + self.coeff_small,
                            x + self.coeff - self.coeff_small,
                            y + self.coeff - self.coeff_small,
                        ),
                        fill=self.WHITE_LINE_AFTER,
                    )
                x += self.coeff
            x = 0
            y += self.coeff
        self.idraw.rectangle((0, 0, self.coeff * 9, self.coeff * 9), fill=self.WHITE_LINE_BEFORE)
        self.idraw.rectangle((self.length_qr - self.coeff * 9, 0, self.length_qr, self.coeff * 9), fill=self.WHITE_LINE_BEFORE)
        self.idraw.rectangle((0, self.length_qr - self.coeff * 9, self.coeff * 9, self.length_qr), fill=self.WHITE_LINE_BEFORE)
        self.idraw.rectangle(
            (
                self.length_qr - self.coeff * 10,
                self.length_qr - self.coeff * 9,
                self.length_qr - self.coeff * 6,
                self.length_qr - self.coeff * 6,
            ),
            fill=self.WHITE_LINE_BEFORE,
        )

        self.idraw.rectangle((self.coeff, self.coeff, self.coeff * 8, self.coeff * 2), fill=self.BLACK_LINE)
        self.idraw.rectangle(
            (self.length_qr - self.coeff * 8, self.coeff, self.length_qr - self.coeff, self.coeff * 2), fill=self.BLACK_LINE
        )
        self.idraw.rectangle((self.coeff, self.coeff * 7, self.coeff * 8, self.coeff * 8), fill=self.BLACK_LINE)
        self.idraw.rectangle(
            (self.length_qr - self.coeff * 8, self.coeff * 7, self.length_qr - self.coeff, self.coeff * 8), fill=self.BLACK_LINE
        )
        self.idraw.rectangle(
            (self.coeff, self.length_qr - self.coeff * 8, self.coeff * 8, self.length_qr - self.coeff * 7), fill=self.BLACK_LINE
        )
        self.idraw.rectangle(
            (self.coeff, self.length_qr - self.coeff * 2, self.coeff * 8, self.length_qr - self.coeff), fill=self.BLACK_LINE
        )
        self.idraw.rectangle(
            (
                self.length_qr - self.coeff * 8,
                self.length_qr - self.coeff * 8,
                self.length_qr - self.coeff * 7,
                self.length_qr - self.coeff * 7,
            ),
            fill=self.BLACK_LINE,
        )
        self.idraw.rectangle((self.coeff * 3, self.coeff * 3, self.coeff * 6, self.coeff * 6), fill=self.BLACK_LINE)
        self.idraw.rectangle(
            (self.length_qr - self.coeff * 6, self.coeff * 3, self.length_qr - self.coeff * 3, self.coeff * 6),
            fill=self.BLACK_LINE,
        )
        self.idraw.rectangle(
            (self.coeff * 3, self.length_qr - self.coeff * 6, self.coeff * 6, self.length_qr - self.coeff * 3),
            fill=self.BLACK_LINE,
        )
        self.idraw.rectangle((self.coeff, self.coeff, self.coeff * 2, self.coeff * 8), fill=self.BLACK_LINE)
        self.idraw.rectangle((self.coeff * 7, self.coeff, self.coeff * 8, self.coeff * 8), fill=self.BLACK_LINE)

        self.idraw.rectangle(
            (self.length_qr - self.coeff * 2, self.coeff, self.length_qr - self.coeff, self.coeff * 8), fill=self.BLACK_LINE
        )
        self.idraw.rectangle(
            (self.length_qr - self.coeff * 8, self.coeff, self.length_qr - self.coeff * 7, self.coeff * 8), fill=self.BLACK_LINE
        )

        self.idraw.rectangle(
            (self.coeff, self.length_qr - self.coeff * 8, self.coeff * 2, self.length_qr - self.coeff), fill=self.BLACK_LINE
        )
        self.idraw.rectangle(
            (self.coeff * 7, self.length_qr - self.coeff * 8, self.coeff * 8, self.length_qr - self.coeff), fill=self.BLACK_LINE
        )

        self.idraw.rectangle(
            (
                self.length_qr - self.coeff * 10,
                self.length_qr - self.coeff * 10,
                self.length_qr - self.coeff * 9,
                self.length_qr - self.coeff * 5,
            ),
            fill=self.BLACK_LINE,
        )
        self.idraw.rectangle(
            (
                self.length_qr - self.coeff * 6,
                self.length_qr - self.coeff * 10,
                self.length_qr - self.coeff * 5,
                self.length_qr - self.coeff * 5,
            ),
            fill=self.BLACK_LINE,
        )

        self.idraw.rectangle(
            (
                self.length_qr - self.coeff * 10,
                self.length_qr - self.coeff * 10,
                self.length_qr - self.coeff * 6,
                self.length_qr - self.coeff * 9,
            ),
            fill=self.BLACK_LINE,
        )
        self.idraw.rectangle(
            (
                self.length_qr - self.coeff * 10,
                self.length_qr - self.coeff * 6,
                self.length_qr - self.coeff * 6,
                self.length_qr - self.coeff * 5,
            ),
            fill=self.BLACK_LINE,
        )

        background.paste(self.back_im, (0, 0), self.back_im)
        return background
