import requests
from bs4 import BeautifulSoup
import lxml

amazon_html = "https://www.amazon.com/dp/1801077266/ref=sspa_dk_detail_2?psc=1&pd_rd_i=1801077266&pd_rd_w=3EVKt" \
              "&content-id=amzn1.sym.bff6e147-54ad-4be3-b4ea-ec19ea6167f7&pf_rd_p=bff6e147-54ad-4be3-b4ea" \
              "-ec19ea6167f7&pf_rd_r=KG6RDCNVB9GH87CJYQXJ&pd_rd_wg=d4kYI&pd_rd_r=2b720d02-3090-4978-b6b4-003ab4c1bb51" \
              "&s=books&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy "

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 " \
             "Safari/537.36"
accept_language = "en-US,en;q=0.9"

http_headers = {
                "User_Agent": user_agent,
                "Accept_Language": accept_language
                }

response = requests.get(amazon_html, headers=http_headers)
response.raise_for_status()
print(response.text)

