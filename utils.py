from PIL import Image, ImageDraw, ImageFont
import numpy as np
import imgaug.augmenters as imageAugmenters
import cv2
import os
import random
from config import *

def load_glyphs():
    glyph_map = {}
    with open(GLYPH_LIST, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) ==2:
                glyph, latin = parts
                glyph_map[glyph] = latin
    return glyph_map
    
def random_font():
    return ImageFont.truetype(random.choice(FONTS), FONT_SIZE)

def render_glyph(glyph):
    img = Image.new('L', IMAGE_SIZE, 255)
    draw = ImageDraw.Draw(img)
    font = random_font()
    bbox = draw.textbbox((0, 0), glyph, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((IMAGE_SIZE[0]-w)//2, (IMAGE_SIZE[1]-h)//2), glyph, fill=0, font=font) 
    return img

def augment_image(image):
    image = np.array(image)
    seq = imageAugmenters.Sequential([
        imageAugmenters.Affine(rotate=(-15, 15), scale=(0.9, 1.1), translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)}),
        imageAugmenters.AdditiveGaussianNoise(scale=8),
        imageAugmenters.MotionBlur(k=3),
    ])
    return seq(image=image)