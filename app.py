import requests as rs
from bs4 import BeautifulSoup as bs
import re

def web_crawler(url):
    elements_h1_and_p = {}
    response = rs.get(url)

    soup = bs(response.text, 'html.parser')
    links_results = soup.find_all('a', href=re.compile("^https://"))

    for result in links_results:
        a_url = result.get('href')
        if (a_url not in elements_h1_and_p):
            elements_h1_and_p[a_url] = []
        
        current_response = rs.get(a_url)

        current_soup = bs(current_response.text, 'html.parser')

        current_h1_results = current_soup.find_all('h1')
        current_p_results = current_soup.find_all('p')

        elements_h1_and_p[a_url].extend(current_h1_results)
        elements_h1_and_p[a_url].extend(current_p_results)
    return elements_h1_and_p

print(web_crawler("https://www.python.org/")) 