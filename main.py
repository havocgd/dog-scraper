from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    user_input = request.json.get('query')
    results = []

    # Example: scrape Gumtree dogs page
    url = "https://www.gumtree.com.au/s-dogs/c18497"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    for listing in soup.select('.user-ad-row'):
        title = listing.select_one('.user-ad-title').text.strip()
        link = "https://www.gumtree.com.au" + listing.select_one('a')['href']
        results.append({'title': title, 'link': link})

    return jsonify(results)

if __name__ == '__main__':
    app.run()
