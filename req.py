import requests

user = 'Kittu_xD'

url = "https://twitter.com/"
xhr_url = 'https://twitter.com/K_a_r_t_i_k__'
headers = {  

"Host": "twitter.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "none",
"Sec-Fetch-User":"?1",
"Connection": "keep-alive",
'Cookie': 'guest_id_marketing=v1%3A163740615194012447; guest_id_ads=v1%3A163740615194012447; personalization_id="v1_nBPARZuYVgG1mXAQgVJ2gA=="; guest_id=v1%3A163740615194012447; ct0=2075be8e503c794914e256ed4a16745a; gt=1462013490172874759; _ga=GA1.2.1417602700.1637406153; _gid=GA1.2.54192838.1637406153; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D'


 }


with requests.Session() as session:
    response = session.get(xhr_url,headers=headers)
    print(response.content)
