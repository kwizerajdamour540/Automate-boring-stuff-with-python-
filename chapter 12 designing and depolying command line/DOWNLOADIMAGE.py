import os
import requests
from bs4 import BeautifulSoup

# Step 1: Get search term and prepare folder
search_term = input('Enter a search term for images: ')
folder_name = f'downloaded_{search_term}'
os.makedirs(folder_name, exist_ok=True)

# Step 2: Fetch the search results page
url = f'https://imgur.com/search?q={search_term}'
headers = {'User-Agent': 'Mozilla/5.0'}  # Helps prevent being blocked by basic bot filters
res = requests.get(url, headers=headers)
res.raise_for_status()

# Step 3: Parse HTML and locate image tags
soup = BeautifulSoup(res.text, 'html.parser')
image_tags = soup.select('.post img')  # Selects <img> tags inside post containers

if not image_tags:
    print('No images found.')
else:
    print(f'Found {len(image_tags)} images. Downloading...')

    # Step 4: Download and save images (limiting to top 10)
    for i, img in enumerate(image_tags[:10]):
        img_url = img.get('src')
        
        # Ensure scheme is complete (handles relative URLs starting with //)
        if img_url.startswith('//'):
            img_url = 'https:' + img_url

        try:
            print(f'Downloading image #{i+1}: {img_url}')
            img_res = requests.get(img_url)
            img_res.raise_for_status()

            # Save image chunk by chunk
            image_path = os.path.join(folder_name, f'image_{i+1}.jpg')
            with open(image_path, 'wb') as file:
                for chunk in img_res.iter_content(100000):
                    file.write(chunk)

        except Exception as err:
            print(f'Could not download {img_url}: {err}')

print('Done!')