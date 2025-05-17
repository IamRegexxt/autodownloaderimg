import os
import requests
from PIL import Image
from io import BytesIO
from google_images_search import GoogleImagesSearch

api_key = ''
search_engine_id = ''
gis = GoogleImagesSearch(api_key, search_engine_id)

save_dir = 'data/Unknown'
os.makedirs(save_dir, exist_ok=True)


# Your diverse search terms
search_terms = [
    "bean leaf", "wheat plant", "rice plant disease", "tomato leaf spot",
    "grass background", "shrub", "wild plant leaves", "weeds in farm",
    "muddy farm road", "soil texture", "cloudy sky", "water puddle", "farm rocks",
    "hand holding leaf", "farm equipment", "concrete wall texture", "tractor parts",
    "blurry plant photo", "overexposed plant image", "out of focus leaves",
    "wood grain", "textile texture", "paper surface", "laptop keyboard", "clothing fabric"
]

image_count = 0
max_images = 50

for term in search_terms:
    print(f"🔍 Searching: {term}")
    gis.search({'q': term, 'num': 5})
    for image in gis.results() :
        if image_count >= max_images:
            break
        try:
            response = requests.get(image.url, timeout=5)
            img = Image.open(BytesIO(response.content)).convert("RGB")
            img = img.resize((224, 224))
            img.save(os.path.join(save_dir, f"unknown_{image_count}.jpg"))
            image_count += 1
        except Exception:
            continue
    if image_count >= max_images:
        break

print(f"\n✅ Downloaded {image_count} images to: {save_dir}")
