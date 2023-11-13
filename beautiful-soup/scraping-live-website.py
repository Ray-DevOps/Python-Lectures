

# In order to scrape a live website with Beautiful Soup, we start by importing the "requests" module,
# and then use the get() method to obtain the HTML code of the website


import requests

response = requests.get("https://news.ycombinator.com/news")

print(response.text)           ---------->      # This returns the complete HTML code of the website same as if you right-clicked on the
                                                # website and took "inspect".



################################################################# ILLUSTRATION 1 ###############################################################
#                                                            ---------------------------


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




################################################################# ILLUSTRATION 2 ###############################################################
#                                                            ---------------------------

# In this second example, we build an application that requests the user to enter any date in the past, and then uses BeautifulSoup to scrap the 
# the billboard top 100 to get the top 100 songs on the billboard for that particular date.


from bs4 import BeautifulSoup
import requests

date = input("What date would you like to travel to? Enter in format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url)

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titles = soup.find_all("div", class_="o-chart-results-list-row-container")

song_list = [ ]
artist_list = [ ]

for title in titles:
    song_title = title.find("h3", id="title-of-a-story").text
    song_title = song_title.strip()
    song_list.append(song_title)

    singer = title.select(".c-label")[1].text
    singer = singer.strip()
    artist_list.append(singer)

billboard_dic = dict(list(zip(artist_list, song_list)))

print('Artist | Song')
for artist, song in billboard_dic.items():
    print(f'{artist} | {song}')

