import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    
urls = ["https://www.trustpilot.com/review/netflix.com"]
    
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept-Language': 'en-US, en;q=0.5',
# }

while len(urls) != 0:
        # get the page to visit from the list
        current_url = urls.pop()
        
        # crawling logic
        response = requests.get(current_url)
        soup = BeautifulSoup(response.content, "html.parser")
        # link_elements = soup.find_all(class_="review")
        reviews = soup.find_all('div', class_='styles_reviewCardInner__EwDq2')
        for review in reviews:
            review_text=review.find('p',{'class':'typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn'}).text.strip()
            print(review_text)
            print("")
        # print(f"link_elements: {soup}")
        # for link_element in link_elements:
        #     url = link_element['href']
        #     if "https://www.scrapingcourse.com/ecommerce/" in url:
        #         urls.append(url)


        # for review in reviews:
        #     review_text = review.find('span', {'data-hook': 'review-body'}).text.strip()  # Adjust the selector based on structure
        #     print(review_text)