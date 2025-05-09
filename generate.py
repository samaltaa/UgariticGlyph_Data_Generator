import os 
import numpy as np 
from tqdm import tqdm
from utils import *


def make_output_dir(labels):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for label in labels:
            os.makedirs(os.path.join(OUTPUT_DIR, label), exist_ok=True)


def save_image(image: Image.Image, label: str, count: int):
    label_dir = os.path.join(OUTPUT_DIR, label)
    os.makedirs(label_dir, exist_ok=True)
    
    # Convert NumPy array to PIL Image if needed
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    
    image_path = os.path.join(label_dir, f"{label}_{count}.png")
    image.save(image_path)



def generate_image_data():
    glyphs_map = load_glyphs()
    make_output_dir(glyphs_map.values())

    for glyph in tqdm(glyphs_map):
        latin = glyphs_map[glyph]
        count = 0
        while count < IMAGES_PER_GLYPH:
            img = render_glyph(glyph)
            save_image(img, latin, count)
            count += 1

            for _ in range (AUGMENTATIONS_PER_IMAGE):
                augmented_img = augment_image(img)
                save_image(augmented_img, latin, count)
                count += 1

if __name__ == "__main__":
    generate_image_data()