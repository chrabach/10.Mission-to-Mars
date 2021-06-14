#!/usr/bin/env python
# coding: utf-8




#10.3.3
Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd



# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)




#10.3.3
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)




# Convert the browser html to a soup object and then quit the browser
#10.3.3
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


#10.3.3
slide_elem.find('div', class_='content_title')


#10.3.3
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


#10.3.3
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images




#10.3.4
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


#10.3.4
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()





#10.3.4
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')



#10.3.4
# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel



#10.3.4
# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ## Mars Facts

#10.3.5
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df




#10.3.5
df.to_html()



browser.quit()





