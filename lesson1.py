from bs4 import BeautifulSoup

# read content of the index html and put it into the src file as a string
with open("scrap_tutorial/lesson1/blank/index.html") as file:
    src = file.read()
# print(src)
soup = BeautifulSoup(src, 'lxml')
""" title = soup.title.string
print(title) """
# .find() .findall()
""" h1 = soup.find_all('h1')
print(h1)
for element in h1:
    print(element.text) """
""" user_name = soup.find('div', class_='user__name')
print(user_name.text.strip()) """
""" user_name = soup.find(class_ = 'user__name').find('span').text
print(user_name) """
""" user_name = soup.find('div', {'class' : 'user__name', 'id': "aaa"}).find('span').text
print(user_name) """
""" user_info_spans = soup.find('div', {'class':'user__info'}).find_all('span')
print(user_info_spans) """
""" for item in user_info_spans:
    print(item.text) """
#print(user_info_spans[2].text)
""" social_links = soup.find('div', {'class': 'social__networks'}).find('ul').find_all('a')
print(social_links) """
all_a = soup.find_all('a')
print(all_a)

for item in all_a:
    item_url = item.get('href')
    print(item_url)