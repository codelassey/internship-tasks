import requests
from bs4 import BeautifulSoup

# Step 1: Ask the user to input the URL they want to scrape
url = input("Enter the URL of the webpage you want to scrape (including 'http://' or 'https://'): ").strip()

# Step 2: Try to fetch the HTML content from the URL
try:
    # I sent a GET request to the webpage to get its content
    response = requests.get(url)
    
    # Step 3: I checked if the request was successful by looking at the status code
    if response.status_code == 200:
        # Step 4: I used BeautifulSoup to parse the HTML content I got from the request
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 1. Headlines (H1 and H2)
        headlines = soup.find_all(['h1', 'h2'])
        print("\nHeadlines found on the page:")
        if headlines:
            for idx, headline in enumerate(headlines, start=1):
                print(f"{idx}: {headline.get_text().strip()}")
        else:
            print("No headlines found on the page.")
        
        # 2. Prices (e.g., spans with class 'price')
        prices = soup.find_all('span', class_='price')
        print("\nPrices found on the page:")
        if prices:
            for idx, price in enumerate(prices, start=1):
                print(f"{idx}: {price.get_text().strip()}")
        else:
            print("No prices found on the page.")
        
        # 3. Paragraphs (Main text content)
        paragraphs = soup.find_all('p')
        print("\nParagraphs found on the page:")
        if paragraphs:
            for idx, paragraph in enumerate(paragraphs[:5], start=1):  # Limiting to first 5 for brevity
                print(f"{idx}: {paragraph.get_text().strip()}")
        else:
            print("No paragraphs found on the page.")
        
        # 4. Images (src attributes)
        images = soup.find_all('img')
        print("\nImage URLs found on the page:")
        if images:
            for idx, image in enumerate(images[:5], start=1):  # Limiting to first 5 for brevity
                print(f"{idx}: {image.get('src')}")
        else:
            print("No images found on the page.")
        
        # 5. Links (a tags with href attributes)
        links = soup.find_all('a', href=True)
        print("\nLinks found on the page:")
        if links:
            for idx, link in enumerate(links[:5], start=1):  # Limiting to first 5 for brevity
                print(f"{idx}: {link.get('href')}")
        else:
            print("No links found on the page.")
        
        # 6. Meta Description
        meta_description = soup.find('meta', attrs={'name': 'description'})
        print("\nMeta Description found on the page:")
        if meta_description and meta_description.get('content'):
            print(meta_description['content'])
        else:
            print("No meta description found on the page.")
        
        # 7. List Items (li tags)
        list_items = soup.find_all('li')
        print("\nList items found on the page:")
        if list_items:
            for idx, item in enumerate(list_items[:5], start=1):  # Limiting to first 5 for brevity
                print(f"{idx}: {item.get_text().strip()}")
        else:
            print("No list items found on the page.")
    
    else:
        # If the request was not successful, I let the user know and show the status code
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        print("Please check if the URL is correct or try again later.")
        
except requests.RequestException as e:
    # If an error happened while making the request, I catch it and print the error message
    print(f"An error occurred: {e}")
