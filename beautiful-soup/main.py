

# Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages 
# that can be used to extract data from HTML, which is useful for web scraping. 

# Web scraping is the process of extracting information from a website from the website's underlying HTML code. 



#                                         ILLUSTRATION
#                               ---------------------------------

#  In this illustration, we use Beautiful Soup to extract data from the site website.html, which is located
#  [here] (https://github.com/Ray-DevOps/Python-Notes/blob/main/beautiful-soup/website.html)

from bs4 import BeautifulSoup                               # We start by importing the Beautiful Soup class from the Beautiful Soup 4 (bs4) module.                                       

with open('website.html', encoding="utf8") as file:
    file_content = file.read()

soup = BeautifulSoup(file_content, 'html.parser')          # In some cases, we may have to use the 'lxml' instead of 'html.parser' in which case we import lxml



print(soup.title)              ---------->           <title>Angela's Personal Site</title>                 # This prints the title of the html file
print(soup.title.string)       ---------->           Angela's Personal Site                                # This prints the string in the title of the html file
print(soup.title.name)         ---------->           title                                                 # This prints the name of the title which is "title"

print(soup)                    ---------->           # This will print out the entire HTML code
print(soup.prettify())         ---------->           # This will print out the entire HTML code with the proper indentation to make it easier to read

print(soup.p)                  ---------->           # This will print out the first paragraph in the HTML code
print(soup.a)                  ---------->           # This will print out the first anchor tag in the HTML code
print(soup.li)                 ---------->           # This will print out the first paragraph in the HTML code
print(soup.ol)                 ---------->           # This will print out the first ordered list in the HTML code
print(soup.ul)                 ---------->           # This will print out the first unordered list in the HTML code

