# Web Scraper

This Python script allows you to scrape headlines, prices, images, links, meta descriptions, and other common elements from a webpage. It is designed to be flexible and extensible, enabling users to gather structured data from various types of websites.

## Features
- Scrapes **Headlines** (h1 and h2 tags)
- Scrapes **Prices** (elements with `class="price"`)
- Extracts **Paragraphs** (p tags) for main content
- Gathers **Image URLs** (img src attributes)
- Collects **Links** (a href attributes)
- Retrieves **Meta descriptions** for page summaries
- Collects **List items** (li tags) for structured lists

## Requirements
- Python 3
- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

## Installation

To run this script, you need to install the required packages. You can install them using:

```bash
pip install requests
pip install beautifulsoup4
pip install bs4
```
## How To Use
> To organize my github page, I removed the projects as standalone repos to this page. You can download the py file and not necessarily having to download the whole repo. Thanks

Download the `webscrapper.py` file from this page.

Run the script:
```bash
python3 web_scrapper.py
```
### Caution
This project is intended for **educational purposes only**. Unauthorized web scrapping may violate website terms of service or legal regulations. Always get permission before scrapping.
