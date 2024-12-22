import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the website
url = "https://www.google.com/search?q=olive+garden&sca_esv=e1265ee66efd81f4&sxsrf=ADLYWIKcreSfVvoAJ5MxIwIfuM5-686XEg%3A1733979205603&ei=RWxaZ9PFJPijptQPusTN0Ao&gs_ssp=eJzj4tTP1Tcwii_LM1NgNGB0YPDiyc_JLEtVSE8sSknNAwBxBAhS&oq=olive&gs_lp=Egxnd3Mtd2l6LXNlcnAiBW9saXZlKgIIADIOEC4YgAQYsQMY0QMYxwEyCxAAGIAEGJECGIoFMggQABiABBixAzIIEAAYgAQYyQMyCxAAGIAEGJIDGIoFMgsQABiABBiSAxiKBTIIEC4YgAQYsQMyDhAuGIAEGLEDGNEDGMcBMhQQLhiABBixAxjRAxiDARjHARiKBTIIEC4YgAQYsQMyHRAuGIAEGLEDGNEDGMcBGJcFGNwEGN4EGOAE2AEBSNQlULYIWLkRcAB4AJABAJgByAGgAfgFqgEFMC41LjG4AQHIAQD4AQGYAgegAtwZqAISwgIHECMYJxjqAsICDRAuGNEDGMcBGCcY6gLCAhMQABiABBhDGLQCGIoFGOoC2AEBwgIcEC4YgAQY0QMYQxi0AhjHARjIAxiKBRjqAtgBAcICChAjGIAEGCcYigXCAgoQABiABBhDGIoFwgIOEC4YgAQYsQMYgwEYigXCAgsQABiABBixAxiDAcICBRAAGIAEwgIREC4YgAQYkQIY0QMYxwEYigXCAgUQLhiABMICDhAAGIAEGLEDGIMBGIoFwgIgEC4YgAQYkQIY0QMYxwEYigUYlwUY3AQY3gQY4ATYAQHCAh0QLhiABBixAxiDARiKBRiXBRjcBBjeBBjgBNgBAZgD0gHxBQAOhq8VrSciugYGCAEQARgBkgcJMC41LjEuOC0xoAf_1QE&sclient=gws-wiz-serp"  # Replace with the website URL
response = requests.get(url)

# Step 2: Check if the request was successful
if response.status_code == 200:
    # Step 3: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 4: Extract specific data (e.g., titles, links)
    # Example: Find all <h1> tags
    titles = soup.find_all('h2')
    for i, title in enumerate(titles, start=1):
        print(f"Title {i}: {title.text.strip()}")
        spantitles = soup.find_all('span')
        for i,spantitle in enumerate(spantitles,start=1):
            print(f"Title {i}: {spantitle.text.strip()}")
         
  
    # # Example: Find all hyperlinks
    # links = soup.find_all('a', href=True)
    # for link in links:
    #     print(f"Link: {link['href']}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
