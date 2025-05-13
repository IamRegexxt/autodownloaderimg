from bing_image_downloader import downloader
import shutil
import os
from PIL import Image

search_terms = [
    "bean leaf", "wheat plant", "rice plant disease", "tomato leaf spot",
    "grass background", "shrub", "wild plant leaves", "weeds in farm",
    "muddy farm road", "soil texture", "cloudy sky", "water puddle", "farm rocks",
    "hand holding leaf", "farm equipment", "concrete wall texture", "tractor parts",
    "blurry plant photo", "overexposed plant image", "out of focus leaves",
    "wood grain", "textile texture", "paper surface", "laptop keyboard", "clothing fabric"
]

save_dir = "data/Unknown"
os.makedirs(save_dir, exist_ok=True)

image_count = 0
max_images = 50

for term in search_terms:
    print(f"Downloading: {term}")
    downloader.download(term, limit=5, output_dir='temp_images', adult_filter_off=True, force_replace=False, timeout=30)

    term_folder = os.path.join("temp_images", term)
    if os.path.exists(term_folder):
        for filename in os.listdir(term_folder):
            if image_count >= max_images:
                break
            try:
                path = os.path.join(term_folder, filename)
                img = Image.open(path).convert("RGB")
                img = img.resize((224, 224))
                img.save(os.path.join(save_dir, f"unknown_{image_count}.jpg"))
                image_count += 1
            except Exception:
                continue
        shutil.rmtree(term_folder)

print(f"\n Downloaded and processed {image_count} Unknown images.")
