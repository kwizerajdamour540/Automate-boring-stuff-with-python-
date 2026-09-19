import requests, bs4

# Download the webpage
res = requests.get('https://nostarch.com/')
res.raise_for_status()

# Parse the HTML content
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Select all anchor <a> tags
link_elements = soup.select('a')

for link in link_elements[:]: #loopimg for all links
    url = link.get('href')
    text = link.getText()
    print(f"Link Text: {text} | URL: {url}")