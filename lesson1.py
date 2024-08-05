import re
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
""" all_a = soup.find_all('a')
print(all_a)

for item in all_a:
    item_text = item.text
    item_url = item.get('href')
    print(f'{item_text}: {item_url}') """
# .find_parent() .find_parents()
""" post_div = soup.find(class_='post__text').find_parent('div', 'user__post')
print(post_div) """
# post_divs = soup.find(class_='post__text').find_parents('div', 'user__post__info')
# print(post_divs)
# .next_element .previous_element
""" div_next = soup.find('div', {'class' : 'post__title'}).next_element.next_element\
.text
print(div_next)
div_find_next = soup.find('div', {'class' : 'post__title'}).find_next().text
print(div_find_next) """
# find_next_sibling() .find_previous_sibling()
""" next_sib = soup.find(class_ = 'post__title').find_next_sibling()
print(next_sib) 
prev_sib = soup.find(class_ = 'post__date').find_previous_sibling()
print(prev_sib)
post_title = soup.find(class_ = 'post__date').find_previous_sibling().find_next()\
.text
print(post_title) """

#links = soup.find(class_="some__links").find_all("a")
links = soup.find(class_="some__links").find_all("a")
# print(links)
""" for link in links:
    link_href = link.get('href')
    link_href1 = link['href']
    link_data_attr = link.get("data-attr")
    link_data_attr1 = link['data-attr']
    link_text = link.text
    
    print(f'{link_text}: {link_href1}')
    print(link_data_attr1)  """
""" find_text = soup.find("a", text=re.compile("Одежда"))
print(find_text) """

find_all_clothes = soup.find_all(text = re.compile("([Оо]дежда)"))
print(find_all_clothes)