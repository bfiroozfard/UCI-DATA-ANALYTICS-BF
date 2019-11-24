from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


def init_browser():
    
    executable_path = {"executable_path":"D:/learnpython/chromedriver.exe "}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    # part #1, NEWS,

    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    news_title=soup.find('div',class_='content_title').get_text()
    news_p=soup.find('div',class_='article_teaser_body').get_text()

    #     # Close the browser after scraping
    browser.quit()
    browser = init_browser()

    #  part#2:featured_image 
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    feature=soup.find(class_='button fancybox')
    relative_image_path=feature["data-fancybox-href"]
    featured_image_url= "https://www.jpl.nasa.gov/" + relative_image_path
    browser.quit()

    browser = init_browser()

    # part#3, current waether 
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    
    mars_weather=soup.find('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()
    
    browser.quit()

    #part#4: mars Facts
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df=tables[0]
    df.columns=['Description','values']
    df.set_index('Description',drop=True,inplace=True)
    df.to_html('table.html')

    #mars #5: images 
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]
   
    
    

    # Store data in a dictionary
    mars_data = {
        "news_t": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "weather": mars_weather,
        "fact_table": 'tablw.html',
        "hem_image": hemisphere_image_urls,
        
    }

    
    return mars_data
