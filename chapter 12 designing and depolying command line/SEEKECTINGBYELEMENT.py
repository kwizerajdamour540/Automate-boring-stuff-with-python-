import requests, bs4

# Download the webpage
res = requests.get('https://nostarch.com/')
res.raise_for_status()

# Parse the HTML content
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Select all paragraph elements
p_elements = soup.select('p')

print(f"Total paragraphs found: {len(p_elements)}")

# Get the raw text inside the first paragraph tag
print(p_elements[0].getText())