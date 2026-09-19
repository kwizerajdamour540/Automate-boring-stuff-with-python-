import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

# Open a local file in write-binary mode ('wb')
with open('RomeoAndJuliet.txt', 'wb') as file:
    # Process 100,000 bytes at a time
    for chunk in res.iter_content(100000):
        file.write(chunk)

print("File saved successfully!")