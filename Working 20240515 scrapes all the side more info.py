import requests
from bs4 import BeautifulSoup
import json

def extract_text_after_link(tag):
    if tag.name == 'a':
        return tag.get_text(strip=True)
    elif tag.name == 'abbr':
        return tag['title'].split('@')[0].strip()

def parse_player_count(player_count_text):
    parts = player_count_text.split(' - ')
    try:
        if len(parts) == 2:
            return int(parts[0]), int(parts[1])
        elif len(parts) == 1:
            return int(parts[0]), int(parts[0])
    except ValueError:
        return 1, 1  # Default to 1 if the parsing fails

def scrape_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract item name from URL
        item_name = url.split('/')[-1]

        # Initialize dictionary to store item data
        item_data = {'Name': item_name}

        # Extracting data based on specified patterns
        patterns = {
            'Links': 'td:contains("Links") + td a',
            'Status': 'td:contains("Status") + td a',
            'Code license': 'td:contains("Code license") + td a',
            'Published': 'td:contains("Published") + td abbr',
            'Release date': 'td:contains("Release date") + td abbr',
            'Authors': 'td:contains("Author") + td a',
            'Multiplayer': 'td:contains("Multiplayer") + td a',
            'Platforms': 'td:contains("Platforms") + td a',
            'Languages': 'td:contains("Languages") + td a',
            'Asset license': 'td:contains("Asset license") + td a',
            'Genre': 'td:contains("Genre") + td a',
            'Inputs': 'td:contains("Inputs") + td a',
            'Mentions': 'td:contains("Mentions") + td a',
            'Rating': '[itemprop="ratingValue"]',
            'Category': 'td:contains("Category") + td a',
            'Tags': 'td:contains("Tags") + td a',
            'Player count': 'td:contains("Player count") + td',
            'Average session': 'td:contains("Average session") + td a',
            'Made with': 'td:contains("Made with") + td a',
            'Updated': 'td:contains("Updated") + td abbr',
            'Accessibility': 'td:contains("Accessibility") + td a',
            'Publisher': 'td:contains("Publisher") + td a'
        }

        for key, value in patterns.items():
            elements = soup.select(value)
            if elements:
                if key == 'Rating':
                    item_data[key] = float(elements[0]['content'])
                elif key == 'Player count':
                    player_count_text = elements[0].get_text(strip=True)
                    min_count, max_count = parse_player_count(player_count_text)
                    item_data['PlCoMin'] = min_count
                    item_data['PlCoMax'] = max_count
                else:
                    item_data[key] = [extract_text_after_link(elem) for elem in elements]

        return item_data

def main():
    # Read URLs from the TXT file
    with open('G:/Dropbox/Public/unique_item_links.txt', 'r') as file:
        urls = file.readlines()

    scraped_data = []

    # Loop through each URL
    for url in urls:
        url = url.strip()  # Remove leading/trailing whitespace
        item_data = scrape_url(url)
        if item_data:
            scraped_data.append(item_data)

    # Write scraped data to JSON file
    with open('G:/Dropbox/Public/Full json list 6212.json', 'w') as json_file:
        json.dump(scraped_data, json_file, indent=4)

if __name__ == "__main__":
    main()
