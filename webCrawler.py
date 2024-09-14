import requests
from bs4 import BeautifulSoup
    
urls = ["https://www.amazon.in/Campus-Mens-Wells-Running-Shoes/dp/B08VGSPZFY/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.21cd7b3c-a701-455d-b388-500ed414b938&dib=eyJ2IjoiMSJ9.jhAawmui1haYLBD1R-nJI1ZXNxu53N92aRYDrmcw_L9vPEgkGpwN2p2MU3ZGR0kwJ7BO3j_fBFG59n5cPCV1X2APxUGDEdSg9QlZYo_aYMlYvLkSKPvm8EX1TbC6ce6d-oloBaj4KawV8MywIeVAr2uYb6D-zjSQsIwqiPhCvFDct_LjRwTDTGl7XkHUJUuzbC1J8ieknquD0r5M2e7M025pHkv7oYjKrDrJigJ2zFLYl7FC1YqOj48c1i8CJKruaAl1CSfX1QgZvm3pPVCTIxpMobKx8I1IdqpKnI6n3_0.GS_i81k81hq74Fef2UTVsXXDGBaQR1G4csR-EEO-KHs&dib_tag=se&pd_rd_r=aa8f2762-78ec-4251-8faf-98fdc30fcdff&pd_rd_w=B1QqP&pd_rd_wg=mOVAt&pf_rd_p=21cd7b3c-a701-455d-b388-500ed414b938&pf_rd_r=WSVQ88Y40167M9Q4ZMZY&qid=1726289097&refinements=p_72%3A1318477031%2Cp_36%3A60000-%2Cp_n_feature_nineteen_browse-bin%3A11301363031&rnid=11301362031&s=apparel&sr=1-1&th=1&psc=1"]
    
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5',
}


while len(urls) != 0:
        # get the page to visit from the list
        current_url = urls.pop()
        
        # crawling logic
        response = requests.get(current_url,headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        # link_elements = soup.find_all(class_="review")
        reviews = soup.find_all('div', class_='a-section review aok-relative')
        print(f"link_elements: {soup}")
        # for link_element in link_elements:
        #     url = link_element['href']
        #     if "https://www.scrapingcourse.com/ecommerce/" in url:
        #         urls.append(url)

