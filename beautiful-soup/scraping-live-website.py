

# In order to scrape a live website with Beautiful Soup, we start by importing the "requests" module,
# and then use the get() method to obtain the HTML code of the website


import requests

response = requests.get("https://news.ycombinator.com/news")

print(response.text)           ---------->      # This returns the complete HTML code of the website same as if you right-clicked on the
                                                # website and took "inspect".


#                     ILLUSTRATION
#               ---------------------------

# In this illustration, we scrap a website that lists the top 100 movies of all time, and create a text file with a list of
# the movies and titles


from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titles = soup.find_all(name="h3", class_="title")

title_list = [ ]

for title in titles:
    x = title.get_text()
    title_list.append(x)

title_list.reverse()

with open('movies.txt','w', encoding="utf-8") as file:
    for title in title_list:
        file.write(f"{title}\n")            --------->        movies.txt

The output is the movies.txt file [here] (https://github.com/Ray-DevOps/Python-Notes/blob/main/beautiful-soup/movies.txt)
