import requests
import sys
from web_scrapper import WebScrappingException
from bs4 import BeautifulSoup as bs


def get_page(full_link):

    """Generate web page for the given link"""
    try:
        web_page = requests.get(full_link).text
        return web_page

    except Exception as e:
        raise WebScrappingException(e,sys) from e



def get_one_page_details(html_page):
    """ This function will return the list of all the products in the html_page"""
    try:
        product_list = html_page.find_all('div', {'class' : ['_2kHMtA', '_1fQZEK']})
        return product_list

    except Exception as e:
        pass


def get_url_list(details, base_link) -> list:
    """ This funtion returns list of urls from the detail"""
    try:
        url_list = []

        for i in range(0,len(details)-1):
            product_url = base_link + (details[i].a['href'])
            url_list.append(product_url)
        return url_list

    except Exception as e:
        pass

def web_parser(source):

    try:
        html_page = bs(source,'html.parser')
        return html_page

    except Exception as e:
        pass


def get_review_details(urls):

    """ The function returns the list of reviews and other related details"""

    try:
        review = []
        for i in range(urls):
            user = (web_parser(urls[i]).find_all('div', {'class': 'col _2wzgFH'})[i].find('p', class_ = "_2sc7ZR _2V5EHH").text)
            ratings = (web_parser(urls[i]).find_all('div', {'class': 'col _2wzgFH'})[i].find('div', class_ = "_3LWZlK _1BLPMq").text)
            comment = (web_parser(urls[i]).find_all('div', {'class': 'col _2wzgFH'})[i].find('div', class_ = "t-ZTKy").text)
            location = (web_parser(urls[i]).find_all('div', {'class': 'col _2wzgFH'})[i].find('p', class_ = "_2mcZGG").text.split(',')[1].strip())
            date = (web_parser(urls[i]).find_all('div', {'class': 'col _2wzgFH'})[i].find_all('p', class_ = "_2sc7ZR")[1].text)
            #print()
            mydict = {'Customer Name' : user, 'Ratings': ratings, 'Comment' : comment, 'Location': location, 'Date': date}
            review.append(mydict)
    
    except:
        pass






def revs(search_string):

    """This function will returns the list of reviews and the other details"""

    try:
        base_link = 'https://www.flipkart.com/search?q='
        full_link = base_link + search_string
        headers = {'user_agent' : \
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
        source_page = get_page(full_link)
        flipkart_html = web_parser(source_page)
        one_page_details = get_one_page_details(flipkart_html)
        url_list = get_url_list(one_page_details, base_link)
        reiews = get_review_details(url_list)

    except Exception as e:
        raise WebScrappingException(e,sys) from e