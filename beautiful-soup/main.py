

# Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages 
# that can be used to extract data from HTML, which is useful for web scraping. 

# Web scraping is the process of extracting information from a website from the website's underlying HTML code. 



#                                         ILLUSTRATION
#                               ---------------------------------


from bs4 import BeautifulSoup                                            
import lxml

with open('website.html', encoding="utf8") as file:
    file_content = file.read()

soup = BeautifulSoup(file_content, 'html.parser')

print(soup.title)              ---------->         <title>Angela's Personal Site</title>                   # This prints the title of the html file
print(soup.title.string)       ---------->           Angela's Personal Site                                # This prints the string in the title of the html file
print(soup.title.name)         ---------->           title                                                 # This prints the name of the title which is "title"
