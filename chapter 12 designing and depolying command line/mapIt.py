import webbrowser, sys, pyperclip

# Check if command-line arguments were passed
if len(sys.argv) > 1:
    # Get address from command line (sys.argv[0] is the script name)
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

# Open Google Maps in the browser
webbrowser.open('https://www.google.com/maps/place/' + address)