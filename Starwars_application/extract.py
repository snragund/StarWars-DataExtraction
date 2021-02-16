"""Import modules"""
import requests
from bs4 import BeautifulSoup
import re
from simple_colors import *


"""Data Extraction and sorting"""
url = 'https://en.m.wikipedia.org/wiki/List_of_Star_Wars_spacecraft'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(re.compile('^h[1-6]$'))


"""Get Starship names with Hyperdrive rating"""
output = []
Ratings = ['Class 1.5', 'Class 0.7','high-performance T-14','Longe Voltrans tri-arc CD-3.2','Class 1']

# Function to fetch Starships data with it's name and Hyperdrive rating
def get_names():
    for names in soup.find_all("h3"):
        a = names.text.strip()
        if a == "Dooku's solar sailerEdit":
            output.append(a + '----->'+ Ratings[0])
        elif a == 'Naboo Royal CruiserEdit':
            output.append(a + '----->'+ Ratings[1])
        elif a == 'Naboo Royal Starship':
            output.append(a + '----->'+ Ratings[2])
        elif a == 'Republic Cruiser (Consular-class cruiser)Edit':
            output.append(a + '----->'+ Ratings[3])
        elif a == 'Techno Union Starship (Hardcell-class Interstellar Transport)Edit':
            output.append(a + '----->'+ Ratings[4])
        else:
            output.append(a + '----->'+"Hyperdrive rating is not available")
        
    return output

# Printing list of Ship names and Hyperdrive rating
names_list = get_names()
print("List of all the Names\n")
print(names_list)

