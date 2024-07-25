from bs4 import BeautifulSoup

# read content of the index html and put it into the src file as a string
with open("scrap_tutorial/lesson1/blank/index.html") as file:
    src = file.read()
print(src)