import sys
import operator
from collections import deque
from io import StringIO

from PIL import Image


def svg_header(width, height):
    return """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
            <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
            "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
            <svg width="%d" height="%d"
                xmlns="http://www.w3.org/2000/svg" version="1.1">
        """ % (
        width,
        height,
    )


def rgba_image_to_svg_pixels(im):
    s = StringIO()
    s.write(svg_header(*im.size))

    width, height = im.size
    for x in range(width):
        for y in range(height):
            here = (x, y)
            rgba = im.getpixel(here)
            s.write(
                """  <rect x="%d" y="%d" width="1" height="1" style="fill:rgb%s; fill-opacity:%.3f; stroke:none;" />\n"""
                % (x, y, rgba[0:3], float(rgba[3]) / 255)
            )
    s.write("""</svg>\n""")
    return s.getvalue()


def png_to_svg(filename):
    im_rgba = Image.open(filename).convert("RGBA")

    return rgba_image_to_svg_pixels(im_rgba)
