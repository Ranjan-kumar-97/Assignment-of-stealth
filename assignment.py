import requests
from bs4 import BeautifulSoup
import json

def frequency_of_words(url):
    # Fetching the web page content from the URL
    web_page = requests.get(url)
    soup = BeautifulSoup(web_page.content, 'html.parser')

    # Extracting all text from the Web page
    text_data = soup.get_text()

    # Removing all non-alphanumeric characters and converting them  into lowercase
    text_data = ''.join(c for c in text_data if c.isalnum() or c.isspace())
    text_data = text_data.lower()

    # Spliting the text into words and counting the frequency of their occurance
    words = text_data.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Format the output as a dictionary of words and their frequencies
    output = {}
    for word, count in word_counts.items():
        output[word] = count

    # Sort the dictionary by frequency (descending) and then alphabetically (ascending)
    output = dict(sorted(output.items(), key=lambda x: (-x[1], x[0])))

    return json.dumps(output)



#Example run
print(frequency_of_words("https://en.wikipedia.org/wiki/Stealth_startup"))