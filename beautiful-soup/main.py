

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

print(soup.p)                      ---------->           # This will print out the first paragraph in the HTML code
print(soup.find_all(name="p"))     ---------->           # This will print out all the paragraphs in the HTML code

print(soup.a)                      ---------->           # This will print out the first anchor tag in the HTML code
print(soup.find_all(name="a"))     ---------->           # This will print out all the anchor tags in the HTML code

print(soup.li)                     ---------->           # This will print out the first paragraph in the HTML code
print(soup.ol)                     ---------->           # This will print out the first ordered list in the HTML code
print(soup.ul)                     ---------->           # This will print out the first unordered list in the HTML code
print(soup.find_all(name="ul"))    ---------->           # This will print out all the unordered lists in the HTML code


# Suppose you wanted to print only the texts in the anchor tags, you would loop through all the anchor tags, and use the
# getText() method to print them out, as shown below.

for tags in all_anchor_tags:
    print(tags.getText())      
    
        |
        ↓

   The App Brewery
   My Hobbies
   Contact Me



# Suppose you wanted to print only the links in the anchor tags, you would loop through all the anchor tags, and use the
# get() method to print the "href" as the links are the href values:

for tags in all_anchor_tags:
    print(tags.get("href"))      
    
        |
        ↓

https://www.appbrewery.co/
https://angelabauer.github.io/cv/hobbies.html
https://angelabauer.github.io/cv/contact-me.html



# While the find_all() method prints every element that matches a criteria, the find() method can be used to find a particular
# element that matches a particular criteria (such as a heading with a specific name, or paragraph with specific ID)


heading = soup.find(name="h1", id="name")
print(heading)             ---------->        <h1 id="name">Angela Yu</h1>

section_heading = soup.find(name="h3", class_="heading")                                          # Eventhough the name of the actual attribute in the HTLM file is "class",
print(section_heading)     ---------->       <h3 class="heading">Books and Teaching</h3>       # we add _ so that it doesn't clash with the "class" keyword for creating classes in Python
print(section_heading.getText())        ---------->       Books and Teaching                       # To print only the text contained in the heading
print(section_heading.name)             ---------->       h3                                       # To get just the name of the tag
print(section_heading.get("class"))     ---------->       ['heading']                              # To get the value of the "class" attribute















