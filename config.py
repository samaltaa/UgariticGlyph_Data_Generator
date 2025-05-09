import os 

GLYPH_LIST = "glyphs.txt"
FONT_DIR = "fonts/"
OUTPUT_DIR = "output/"

IMAGE_SIZE = (64, 64)
FONT_SIZE = 48
IMAGES_PER_GLYPH = 500

AUGMENTATIONS_PER_IMAGE = 5
FONTS = [os.path.join(FONT_DIR, f) for f in os.listdir(FONT_DIR) if f.endswith('.ttf')]