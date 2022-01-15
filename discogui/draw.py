"""
drawing rectangles for debugging
"""


from PIL import Image, ImageDraw

from discogui.screenrect import ScreenRect


def draw_textrect(im, rect, text=None, color="red"):
    """
    draw rectangle and text in center
    """
    im = im.copy()
    draw = ImageDraw.Draw(im)
    draw.rectangle(rect, outline=color, fill=None)
    if text:
        rtext = ScreenRect(draw.textsize(text))
        rtext.center = ScreenRect(rect).center
        draw.text(rtext.topleft, text, fill=color)
    return im


def draw_indexed_rect_list(im, lsrect, color="red"):
    """
    draw rectangles and index in center
    """
    index = 0
    for x in lsrect:
        im = draw_textrect(im, x, str(index), color=color)
        index += 1
    return im


def _test():
    im = Image.new("RGB", (522, 222), "grey")
    x = draw_indexed_rect_list(
        im,
        [
            (1, 111, 111, 61),
            (221, 1, 111, 61),
        ],
    )
    x.save("rect.png")


if __name__ == "__main__":
    _test()
