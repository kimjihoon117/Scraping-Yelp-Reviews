pip install bs4

import requests
import pandas as pd
from bs4 import BeautifulSoup

site = requests.get('https://www.yelp.com/biz/iron-age-glenview-glenview?osq=iron+age')
html = site.text
soup = BeautifulSoup(html, 'html.parser')

comment_list = []
comments = soup.find_all('span', class_='raw__09f24__T4Ezm')
for comment in comments:
    x = comment.text.replace("\xa0", "")
    comment_list.append(x)

name_list = []
names = soup.find_all('a', class_='css-1m051bw')
for name in names:
    x = name.text
    # because Cherry O. wrote 2 previous comments:
    if x == "Cherry O.":
        name_list.extend(['Cherry O.', 'Cherry O.'])
    else:
        name_list.append(x)

dates_list = []
dates = soup.find_all('span', class_='css-chan6m')
for date in dates:
    x = date.text
    dates_list.append(x)

ultimate_list = list(zip(name_list, dates_list, comment_list))

final_dataframe = pd.DataFrame(ultimate_list, columns=['이름      ', '리뷰 작성 날짜    ', '                      식당 리뷰'])
print(final_dataframe)
